#!/usr/bin/env pvbatch
import os
import json
import subprocess
import paraview

paraview.compatibility.major = 6
paraview.compatibility.minor = 0

from paraview.simple import (
    _DisableFirstRenderCameraReset,
    CreateView,
    CreateLayout,
    GetMaterialLibrary,
    SetActiveView,
    LegacyVTKReader,
    WarpByVector,
    Show,
    GetColorTransferFunction,
    RenderAllViews,
    SaveScreenshot,
    Delete,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def trim_image(image_path):
    if not os.path.exists(image_path):
        return

    try:
        cmd = ["convert", "-trim", image_path, image_path]
        subprocess.run(
            cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        print(f"    ✓ Trimmed: {os.path.basename(image_path)}")
    except subprocess.CalledProcessError:
        print(f"    ⚠ Trim failed: {os.path.basename(image_path)}")
    except FileNotFoundError:
        print(f"    ⚠ ImageMagick 'convert' not found, skipping trim")


def setup_view(config):
    _DisableFirstRenderCameraReset()

    materialLibrary = GetMaterialLibrary()

    renderView = CreateView("RenderView")

    camera_params = config["camera"]
    for key, value in camera_params.items():
        setattr(renderView, key, value)

    renderView.OSPRayMaterialLibrary = materialLibrary

    SetActiveView(renderView)

    layout = CreateLayout()
    layout.AssignView(0, renderView)
    res = config["resolution"]
    layout.SetSize(res[0], res[1])

    return renderView


def compute_field_range(reader, field_name):
    from paraview.simple import UpdatePipeline, Calculator

    calc = Calculator(Input=reader)
    calc.Function = f"mag({field_name})"
    calc.ResultArrayName = "magnitude"
    UpdatePipeline()

    info = calc.GetDataInformation()
    array_info = info.GetPointDataInformation().GetArrayInformation("magnitude")
    mag_range = array_info.GetComponentRange(0)

    Delete(calc)
    return mag_range[1]


def render_mode(
    renderView, reader, mode_config, colormap_config, output_dir, resolution
):
    field_name = mode_config["field_name"]
    warp_scale = mode_config["warp_scale"]
    output_name = mode_config["output_name"]

    print(f"  Rendering {field_name}...")

    warp = WarpByVector(Input=reader)
    warp.Vectors = ["POINTS", field_name]
    warp.ScaleFactor = warp_scale

    display = Show(warp, renderView, "UnstructuredGridRepresentation")
    display.Representation = "Surface"
    display.ColorArrayName = ["POINTS", field_name]

    if colormap_config.get("compute_normals", True):
        display.ComputePointNormals = 1

    lut = GetColorTransferFunction(field_name)
    preset_name = colormap_config.get("preset", "Fast")
    lut.ApplyPreset(preset_name, True)

    max_mag = compute_field_range(reader, field_name)
    lut.RescaleTransferFunction(0, max_mag)

    display.LookupTable = lut

    RenderAllViews()

    output_path = os.path.join(output_dir, output_name)
    SaveScreenshot(output_path, renderView, ImageResolution=resolution)

    print(f"    ✓ Saved: {output_path}")

    trim_image(output_path)

    display.Visibility = 0
    Delete(warp)


def main():
    print("=" * 70)
    print("Whole Model Mode Shape Renderer")
    print("=" * 70)

    config = load_config()
    print(f"\nLoaded config: {CONFIG_PATH}")
    print(f"Data source: {config['data_source']}")
    print(f"Modes to render: {len(config['modes'])}")

    renderView = setup_view(config)

    data_path = config["data_source"]
    if not os.path.exists(data_path):
        print(f"ERROR: Data file not found: {data_path}")
        return 1

    reader = LegacyVTKReader(FileNames=[data_path])

    output_dir = config.get("output_dir", ".")
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    resolution = config["resolution"]
    colormap_config = config["colormap"]

    print("\nRendering modes...")
    for mode_config in config["modes"]:
        render_mode(
            renderView, reader, mode_config, colormap_config, output_dir, resolution
        )

    Delete(reader)

    print("\n" + "=" * 70)
    print("All rendering completed successfully!")
    print("=" * 70)
    print("\nGenerated files:")
    for mode_config in config["modes"]:
        output_path = os.path.join(output_dir, mode_config["output_name"])
        if os.path.exists(output_path):
            print(f"  ✓ {mode_config['output_name']}")
        else:
            print(f"  ✗ {mode_config['output_name']} (failed)")

    return 0


if __name__ == "__main__":
    exit(main())
