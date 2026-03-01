import os
import json
import subprocess
import sys

# Try importing paraview.simple, but allow partial loading for utils if not in pvbatch
try:
    from paraview.simple import *

    PARAVIEW_AVAILABLE = True
except ImportError:
    PARAVIEW_AVAILABLE = False

# Import plot_style_config for unified colormap support
try:
    sys.path.insert(
        0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "figures")
    )
    from plot_style_config import (
        get_paraview_rgb_points,
        get_paraview_partition_colors,
        apply_paraview_colormap,
        get_style,
    )

    STYLE_CONFIG_AVAILABLE = True
except ImportError:
    STYLE_CONFIG_AVAILABLE = False

# -----------------------------------------------------------------------------
# IO & System Utils
# -----------------------------------------------------------------------------


def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)


def ensure_symlinks(source_dir, target_dir, filenames):
    """
    Ensures that files exist in target_dir, symlinking from source_dir if needed.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for f in filenames:
        src = os.path.join(source_dir, f)
        dst = os.path.join(target_dir, f)

        if not os.path.exists(dst):
            if os.path.exists(src):
                try:
                    os.symlink(src, dst)
                    print(f"Linked {src} -> {dst}")
                except OSError as e:
                    print(f"Failed to link {src}: {e}")
            else:
                print(f"Warning: Source file {src} not found.")


def post_process_image(file_path):
    """
    Trims whitespace and converts white background to transparent
    using ImageMagick's convert tool.
    """
    if not os.path.exists(file_path):
        return

    try:
        # Check if convert/magick is available
        # Using 'convert' as requested, though 'magick' is newer
        cmd = ["convert", "-trim", "-transparent", "white", file_path, file_path]
        print(f"Post-processing: {file_path}")
        subprocess.run(
            cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        print(f"Error post-processing {file_path}")
    except FileNotFoundError:
        print("Error: 'convert' command not found.")


# -----------------------------------------------------------------------------
# ParaView Utils
# -----------------------------------------------------------------------------


def setup_view(camera_params=None):
    """Initialize standard view settings and apply camera if provided."""
    if not PARAVIEW_AVAILABLE:
        raise ImportError("ParaView python modules not found")

    paraview.simple._DisableFirstRenderCameraReset()
    view = GetActiveViewOrCreate("RenderView")

    # Standard visual settings
    view.OrientationAxesVisibility = 0
    view.UseToneMapping = 1
    view.UseAmbientOcclusion = 1
    view.Exposure = 3.0

    if camera_params:
        for key, value in camera_params.items():
            try:
                setattr(view, key, value)
            except AttributeError:
                print(f"Warning: Could not set camera property {key}")

    return view


def load_vtk(path, name):
    if not os.path.exists(path):
        print(f"Error: File {path} not found")
        return None
    return LegacyVTKReader(registrationName=name, FileNames=[path])


def apply_preset(field_name, preset_name, data_range=None, scheme=None):
    """Apply a color preset to the LookupTable of a field.

    If preset_name is 'custom' and scheme is provided, uses unified colormap.
    """
    if not preset_name:
        return None

    lut = GetColorTransferFunction(field_name)

    if preset_name == "custom" and scheme and STYLE_CONFIG_AVAILABLE:
        if data_range:
            apply_paraview_colormap(lut, scheme, data_range[0], data_range[1])
        else:
            current_range = lut.RGBPoints[0], lut.RGBPoints[-4]
            apply_paraview_colormap(lut, scheme, current_range[0], current_range[1])
    else:
        lut.ApplyPreset(preset_name, True)
        if data_range:
            lut.RescaleTransferFunction(data_range[0], data_range[1])

    return lut


def plot_field(
    view,
    source,
    field_name,
    preset_name,
    output_path,
    representation="Surface",
    resolution=[2146, 1358],
    transparent=False,
    compute_normals=False,
    data_range=None,
    scheme=None,
):
    """Generic function to plot a scalar field on a source.

    Set preset_name='custom' and provide scheme to use unified colormap.
    """
    display = Show(source, view, "UnstructuredGridRepresentation")
    display.Representation = representation

    if representation == "Surface" and compute_normals:
        display.ComputePointNormals = 1

    ColorBy(display, ("POINTS", field_name))

    if data_range:
        apply_preset(field_name, preset_name, data_range=data_range, scheme=scheme)
    else:
        display.RescaleTransferFunctionToDataRange(True, False)
        apply_preset(field_name, preset_name, scheme=scheme)

    display.SetScalarBarVisibility(view, False)

    SaveScreenshot(
        output_path,
        viewOrLayout=view,
        ImageResolution=resolution,
        TransparentBackground=1 if transparent else 0,
    )

    Hide(source, view)

    post_process_image(output_path)
