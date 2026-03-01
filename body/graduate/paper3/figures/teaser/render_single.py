#!/usr/bin/env pvbatch
"""
Render a single mode shape from a VTK file.

Usage:
    pvbatch --mesa render_single.py --input file.vtk --mode mode_0 --output out.png [options]

Camera modes:
    --auto-camera: Compute camera automatically based on submesh bounds (close-up view)
    Or specify manually: --camera-position, --camera-focal-point, --camera-view-up, --camera-parallel-scale
"""

import argparse
import os
import math
import json

import paraview

paraview.compatibility.major = 6
paraview.compatibility.minor = 0

from paraview.simple import *


def parse_args():
    parser = argparse.ArgumentParser(
        description="Render a single mode shape from a VTK file."
    )

    parser.add_argument("--input", required=True, help="Path to input VTK file")
    parser.add_argument("--mode", required=True, help="Mode field name (e.g., mode_0)")
    parser.add_argument("--output", required=True, help="Path to output PNG file")

    parser.add_argument(
        "--auto-camera",
        action="store_true",
        help="Auto-compute camera based on submesh bounds (close-up view)",
    )
    parser.add_argument(
        "--camera-position", default=None, help='Camera position as "x,y,z"'
    )
    parser.add_argument(
        "--camera-focal-point", default=None, help='Camera focal point as "x,y,z"'
    )
    parser.add_argument(
        "--camera-view-up",
        default="0,1,0",
        help='Camera view up vector as "x,y,z" (default: 0,1,0 = Y-up)',
    )
    parser.add_argument(
        "--camera-parallel-scale",
        type=float,
        default=None,
        help="Camera parallel scale",
    )

    parser.add_argument(
        "--warp-ratio",
        type=float,
        default=0.5,
        help="Max displacement as ratio of submesh bbox max axis (default: 0.5)",
    )

    parser.add_argument(
        "--view-size",
        default="2146,1358",
        help='Output image size as "width,height" (default: 2146,1358)',
    )

    parser.add_argument(
        "--opacity", type=float, default=1.0, help="Warped mesh opacity (default: 1.0)"
    )
    parser.add_argument(
        "--show-original",
        action="store_true",
        help="Show original (unwarped) mesh (hidden by default)",
    )
    parser.add_argument(
        "--original-color",
        default="0.855,0.855,0.855",
        help='Original mesh color as "r,g,b" (default: gray)',
    )

    parser.add_argument(
        "--background",
        default="1.0,1.0,1.0",
        help='Background color as "r,g,b" (default: white)',
    )

    parser.add_argument(
        "--exposure",
        type=float,
        default=2.0,
        help="Tone mapping exposure (default: 2.0)",
    )
    parser.add_argument(
        "--no-tone-mapping", action="store_true", help="Disable tone mapping"
    )
    parser.add_argument(
        "--no-ambient-occlusion", action="store_true", help="Disable ambient occlusion"
    )

    # Load default preset from color_presets.json
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        presets_path = os.path.join(
            current_dir, "../../comparison-figures/color_presets.json"
        )
        with open(presets_path, "r") as f:
            presets = json.load(f)
        default_colormap = presets.get("eigenvec", "Fast")
    except Exception:
        default_colormap = "Fast"

    parser.add_argument(
        "--colormap",
        default=default_colormap,
        help=f"ColorTransferFunction preset name (default: {default_colormap})",
    )
    parser.add_argument(
        "--custom-colormap",
        default=None,
        help="Custom colormap as JSON: [[val,r,g,b], ...] where val in [0,1], rgb in [0,1]",
    )
    parser.add_argument(
        "--preset-file",
        default=None,
        help="Path to a ParaView JSON preset file to import",
    )

    return parser.parse_args()


def parse_vector(s):
    return [float(x.strip()) for x in s.split(",")]


def compute_max_displacement_magnitude(reader, mode_name):
    calculator = Calculator(Input=reader)
    calculator.Function = f"mag({mode_name})"
    calculator.ResultArrayName = "displacement_magnitude"
    UpdatePipeline()

    info = calculator.GetDataInformation()
    array_info = info.GetPointDataInformation().GetArrayInformation(
        "displacement_magnitude"
    )
    mag_range = array_info.GetComponentRange(0)
    max_mag = mag_range[1]

    Delete(calculator)
    return max_mag


def compute_submesh_bbox(reader):
    bounds = reader.GetDataInformation().GetBounds()
    return bounds


def compute_auto_camera(bounds, view_up):
    """Compute camera parameters based on submesh bounds (close-up view like original script)."""
    center = [
        (bounds[0] + bounds[1]) / 2,
        (bounds[2] + bounds[3]) / 2,
        (bounds[4] + bounds[5]) / 2,
    ]

    bbox_sizes = [
        bounds[1] - bounds[0],
        bounds[3] - bounds[2],
        bounds[5] - bounds[4],
    ]

    diagonal = math.sqrt(sum(s**2 for s in bbox_sizes))
    camera_distance = diagonal * 1.5

    direction = [-0.6611853, -0.0257855, -0.0863267]
    dir_mag = math.sqrt(sum(d**2 for d in direction))
    norm_dir = [d / dir_mag for d in direction]

    position = [center[i] + norm_dir[i] * camera_distance for i in range(3)]
    parallel_scale = diagonal / 2

    return {
        "position": position,
        "focal_point": center,
        "view_up": view_up,
        "parallel_scale": parallel_scale,
    }


def compute_warp_scale(reader, mode_name, warp_ratio):
    max_displacement = compute_max_displacement_magnitude(reader, mode_name)
    bounds = compute_submesh_bbox(reader)
    bbox_sizes = [bounds[1] - bounds[0], bounds[3] - bounds[2], bounds[5] - bounds[4]]
    bbox_max_axis = max(bbox_sizes)

    if max_displacement < 1e-10:
        return 1.0, bbox_max_axis

    scale = (bbox_max_axis * warp_ratio) / max_displacement
    return scale, bbox_max_axis


def main():
    args = parse_args()

    view_size = [int(x) for x in args.view_size.split(",")]
    original_color = parse_vector(args.original_color)
    view_up = parse_vector(args.camera_view_up)
    background_color = parse_vector(args.background)

    paraview.simple._DisableFirstRenderCameraReset()

    reader = LegacyVTKReader(FileNames=[args.input])
    UpdatePipeline()

    warp_scale, bbox_max_axis = compute_warp_scale(reader, args.mode, args.warp_ratio)

    if args.auto_camera:
        bounds = compute_submesh_bbox(reader)
        cam = compute_auto_camera(bounds, view_up)
        camera_position = cam["position"]
        camera_focal_point = cam["focal_point"]
        camera_parallel_scale = cam["parallel_scale"]
    else:
        camera_position = parse_vector(args.camera_position)
        camera_focal_point = parse_vector(args.camera_focal_point)
        camera_parallel_scale = args.camera_parallel_scale

    warp = WarpByVector(Input=reader)
    warp.Vectors = ["POINTS", args.mode]
    warp.ScaleFactor = warp_scale
    UpdatePipeline()

    materialLibrary = GetMaterialLibrary()

    renderView = CreateView("RenderView")
    renderView.ViewSize = view_size
    renderView.OrientationAxesVisibility = 0
    renderView.CenterOfRotation = camera_focal_point

    if not args.no_tone_mapping:
        renderView.UseToneMapping = 1
        renderView.Exposure = args.exposure

    if not args.no_ambient_occlusion:
        renderView.UseAmbientOcclusion = 1

    renderView.CameraPosition = camera_position
    renderView.CameraFocalPoint = camera_focal_point
    renderView.CameraViewUp = view_up
    renderView.CameraParallelScale = camera_parallel_scale
    renderView.CameraFocalDisk = 1.0
    renderView.Background = background_color
    renderView.UseColorPaletteForBackground = 0
    renderView.OSPRayMaterialLibrary = materialLibrary

    SetActiveView(renderView)

    if args.show_original:
        originalDisplay = Show(reader, renderView, "UnstructuredGridRepresentation")
        originalDisplay.Representation = "Surface"
        originalDisplay.AmbientColor = original_color
        originalDisplay.DiffuseColor = original_color
        originalDisplay.ColorArrayName = [None, ""]
        originalDisplay.ComputePointNormals = 1

    warpDisplay = Show(warp, renderView, "UnstructuredGridRepresentation")
    warpDisplay.Representation = "Surface"
    warpDisplay.ColorArrayName = ["POINTS", args.mode]
    warpDisplay.Opacity = args.opacity
    warpDisplay.ComputePointNormals = 1

    modeLUT = GetColorTransferFunction(args.mode)

    if args.preset_file:
        ImportPresets(filename=args.preset_file)

    if args.custom_colormap:
        import json

        colormap_data = json.loads(args.custom_colormap)
        rgb_points = []
        max_mag = compute_max_displacement_magnitude(reader, args.mode)
        for val, r, g, b in colormap_data:
            rgb_points.extend([val * max_mag, r, g, b])
        modeLUT.RGBPoints = rgb_points
    else:
        modeLUT.ApplyPreset(args.colormap, True)
        max_mag = compute_max_displacement_magnitude(reader, args.mode)
        modeLUT.RescaleTransferFunction(0, max_mag)
    warpDisplay.LookupTable = modeLUT

    renderView.ResetCamera()

    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    RenderAllViews()
    SaveScreenshot(args.output, renderView, ImageResolution=view_size)

    print(
        f"Saved: {args.output} (warp_scale={warp_scale:.6f}, bbox={bbox_max_axis:.4f})"
    )

    Delete(warp)
    Delete(reader)
    Delete(renderView)


if __name__ == "__main__":
    main()
