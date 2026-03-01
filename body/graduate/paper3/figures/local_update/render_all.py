# ParaView rendering script for local update figures
# Renders PCB and micro partition visualizations with high quality settings

from paraview.simple import *
import os
import json
import sys
import subprocess

# Disable automatic camera reset
paraview.simple._DisableFirstRenderCameraReset()

# Add figures path for plot_style_config
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "figures"))

# Load color presets and style config
try:
    from plot_style_config import get_paraview_rgb_points

    STYLE_CONFIG_AVAILABLE = True
except ImportError:
    STYLE_CONFIG_AVAILABLE = False
    print("Warning: plot_style_config not available, using fallback presets")

try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    presets_path = os.path.join(
        current_dir, "../../comparison-figures/color_presets.json"
    )
    with open(presets_path, "r") as f:
        presets = json.load(f)
    PARTITION_PRESET = presets.get("partition", "Fast")
    COLOR_SCHEME = presets.get("scheme", "blue_orange")
    print(f"Loaded preset: {PARTITION_PRESET}, scheme: {COLOR_SCHEME}")
except Exception as e:
    print(f"Warning: Could not load color presets: {e}")
    PARTITION_PRESET = "Cool to Warm"
    COLOR_SCHEME = "blue_orange"

# Output directory
SOURCE_DATA_DIR = os.path.join(PROJECT_ROOT, "source_data", "local_update")
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Data paths from source_data
PCB_ORIGIN_PARTITION = os.path.join(SOURCE_DATA_DIR, "PCB/origin/Partition_Summary.vtk")
PCB_UPDATED_PARTITION = os.path.join(
    SOURCE_DATA_DIR, "PCB/updated/Partition_Summary.vtk"
)
MICRO_ORIGIN_PARTITION = os.path.join(
    SOURCE_DATA_DIR, "micro/origin/Partition_Summary.vtk"
)
MICRO_UPDATED_PARTITION = os.path.join(
    SOURCE_DATA_DIR, "micro/updated/Partition_Summary.vtk"
)

# Settings
EXPOSURE = 3.0
RESOLUTION = [2048, 1024]


def get_bounds_and_camera(vtk_path, view_direction="Z"):
    """Get the bounding box and compute camera settings for a VTK file"""
    reader = LegacyVTKReader(registrationName="temp_reader", FileNames=[vtk_path])
    reader.UpdatePipeline()

    bounds = reader.GetDataInformation().GetBounds()
    # bounds = (xmin, xmax, ymin, ymax, zmin, zmax)

    center = [
        (bounds[0] + bounds[1]) / 2,
        (bounds[2] + bounds[3]) / 2,
        (bounds[4] + bounds[5]) / 2,
    ]

    # Calculate the diagonal for camera distance
    dx = bounds[1] - bounds[0]
    dy = bounds[3] - bounds[2]
    dz = bounds[5] - bounds[4]

    Delete(reader)

    return bounds, center, (dx, dy, dz)


def render_partition_with_camera(
    vtk_path, output_path, partition_field, camera_settings
):
    """Render a partition VTK file to PNG with specified camera settings"""

    # Create reader
    reader = LegacyVTKReader(registrationName="reader", FileNames=[vtk_path])

    # Get active view
    renderView = GetActiveViewOrCreate("RenderView")

    # Hide axes/orientation widget
    renderView.OrientationAxesVisibility = 0
    renderView.CenterAxesVisibility = 0

    # === High quality rendering settings ===
    renderView.Exposure = EXPOSURE
    renderView.UseToneMapping = 1

    # Extract surface first (convert UnstructuredGrid to PolyData)
    extractSurface = ExtractSurface(registrationName="extractSurface", Input=reader)

    # Generate surface normals for smooth shading
    normals = GenerateSurfaceNormals(registrationName="normals", Input=extractSurface)

    # Show data with normals
    display = Show(normals, renderView, "GeometryRepresentation")
    display.Representation = "Surface"

    # Color by partition field
    ColorBy(display, ("POINTS", partition_field))

    # Apply colormap
    lut = GetColorTransferFunction(partition_field)
    display.RescaleTransferFunctionToDataRange(True, False)

    if PARTITION_PRESET == "custom" and STYLE_CONFIG_AVAILABLE:
        data_min = lut.RGBPoints[0]
        data_max = lut.RGBPoints[-4]
        rgb_points = get_paraview_rgb_points(COLOR_SCHEME, data_min, data_max)
        lut.RGBPoints = rgb_points
        lut.ColorSpace = "Lab"
    else:
        lut.ApplyPreset(PARTITION_PRESET, True)

    display.SetScalarBarVisibility(renderView, False)
    display.RescaleTransferFunctionToDataRange(False, True)

    # Apply fixed camera settings
    renderView.CameraPosition = camera_settings["position"]
    renderView.CameraFocalPoint = camera_settings["focal_point"]
    renderView.CameraViewUp = camera_settings["view_up"]
    renderView.CameraParallelScale = camera_settings["parallel_scale"]
    renderView.CameraParallelProjection = 1  # Use parallel projection for consistency

    # Set view size
    renderView.ViewSize = RESOLUTION

    # Render
    Render()

    # Save screenshot with transparency
    SaveScreenshot(
        filename=output_path,
        viewOrLayout=renderView,
        ImageResolution=RESOLUTION,
        TransparentBackground=1,
    )

    print(f"Saved: {output_path}")

    # Trim whitespace using ImageMagick
    try:
        subprocess.run(
            ["convert", "-trim", output_path, output_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f"Trimmed: {output_path}")
    except Exception as e:
        print(f"Warning: Could not trim {output_path}: {e}")

    # Clean up
    Delete(normals)
    Delete(extractSurface)
    Delete(reader)


# === Compute camera settings for PCB ===
print("Computing PCB camera settings...")
pcb_bounds, pcb_center, pcb_size = get_bounds_and_camera(PCB_ORIGIN_PARTITION)
pcb_camera = {
    "position": [pcb_center[0], pcb_center[1] + 5.0, pcb_center[2]],  # View from +Y
    "focal_point": pcb_center,
    "view_up": [0, 0, 1],
    "parallel_scale": max(pcb_size[0], pcb_size[2]) * 0.6,
}

# === Compute camera settings for Micro ===
print("Computing Micro camera settings...")
micro_bounds, micro_center, micro_size = get_bounds_and_camera(MICRO_ORIGIN_PARTITION)
micro_camera = {
    "position": [
        micro_center[0],
        micro_center[1],
        micro_center[2] + 5.0,
    ],  # View from +Z
    "focal_point": micro_center,
    "view_up": [0, 1, 0],
    "parallel_scale": max(micro_size[0], micro_size[1]) * 0.6,
}

print(f"PCB center: {pcb_center}, size: {pcb_size}")
print(f"Micro center: {micro_center}, size: {micro_size}")

# Render all PCB images with fixed camera
print("Rendering PCB origin primal partition...")
render_partition_with_camera(
    PCB_ORIGIN_PARTITION,
    os.path.join(OUTPUT_DIR, "pcb_origin_primal.png"),
    "partition_0",
    pcb_camera,
)

print("Rendering PCB origin dual partition...")
render_partition_with_camera(
    PCB_ORIGIN_PARTITION,
    os.path.join(OUTPUT_DIR, "pcb_origin_dual.png"),
    "partition_1",
    pcb_camera,
)

print("Rendering PCB updated primal partition...")
render_partition_with_camera(
    PCB_UPDATED_PARTITION,
    os.path.join(OUTPUT_DIR, "pcb_updated_primal.png"),
    "partition_0",
    pcb_camera,
)

print("Rendering PCB updated dual partition...")
render_partition_with_camera(
    PCB_UPDATED_PARTITION,
    os.path.join(OUTPUT_DIR, "pcb_updated_dual.png"),
    "partition_1",
    pcb_camera,
)

# Render all Micro images with fixed camera
print("Rendering Micro origin primal partition...")
render_partition_with_camera(
    MICRO_ORIGIN_PARTITION,
    os.path.join(OUTPUT_DIR, "micro_origin_primal.png"),
    "partition_0",
    micro_camera,
)

print("Rendering Micro origin dual partition...")
render_partition_with_camera(
    MICRO_ORIGIN_PARTITION,
    os.path.join(OUTPUT_DIR, "micro_origin_dual.png"),
    "partition_1",
    micro_camera,
)

print("Rendering Micro updated primal partition...")
render_partition_with_camera(
    MICRO_UPDATED_PARTITION,
    os.path.join(OUTPUT_DIR, "micro_updated_primal.png"),
    "partition_0",
    micro_camera,
)

print("Rendering Micro updated dual partition...")
render_partition_with_camera(
    MICRO_UPDATED_PARTITION,
    os.path.join(OUTPUT_DIR, "micro_updated_dual.png"),
    "partition_1",
    micro_camera,
)

print("All renderings complete!")
