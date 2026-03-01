import os
import sys

# Add parent directory to path to import pv_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pv_utils import setup_view, load_vtk, plot_field, ensure_symlinks, load_json
from paraview.simple import (
    GetLayout,
    WarpByVector,
    Show,
    GetColorTransferFunction,
    GetOpacityTransferFunction,
    SetActiveSource,
)

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
MODEL_NAME = "board"
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
SOURCE_DATA_DIR = os.path.join(PROJECT_ROOT, "source_data", "board")
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Presets
PRESETS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "color_presets.json"
)
PRESETS = load_json(PRESETS_PATH)
EIGENVEC_PRESET = PRESETS.get("eigenvec", "custom")
PARTITION_PRESET = PRESETS.get("partition", "custom")
COLOR_SCHEME = PRESETS.get("scheme", "teal_coral")

# Resolution
IMG_RES = [2146, 1138]

# Camera Settings
CAMERA_PARAMS = {
    "ViewSize": [2146, 1138],
    "OrientationAxesVisibility": 0,
    "CenterOfRotation": [-540.6607746676073, 717.9851895607225, 8.669921443453415],
    "UseToneMapping": 1,
    "UseAmbientOcclusion": 1,
    "CameraPosition": [-530.1605656876959, -600.64988908855, 1636.3144257240035],
    "CameraFocalPoint": [-540.6607746676068, 717.9851895607239, 8.669921443455895],
    "CameraViewUp": [0.9992600967502463, -0.026477006128579228, -0.02789672362761444],
    "CameraFocalDisk": 1.0,
    "CameraParallelScale": 542.1709428953639,
}

# Source Data Paths
MODE_GT_PATH = os.path.join(SOURCE_DATA_DIR, "mode_gt.vtk")
PARTITION_PATH = os.path.join(SOURCE_DATA_DIR, "Partition_Summary.vtk")

# Eigenmode indices to render
EIGENMODE_INDICES = [7, 103, 199]


# -----------------------------------------------------------------------------
# Execution
# -----------------------------------------------------------------------------
def render_partitions(renderView1):
    """Render primal and dual partition views."""
    print("Rendering partitions...")

    if not os.path.exists(PARTITION_PATH):
        print(f"Warning: {PARTITION_PATH} not found. Skipping partitions.")
        return

    partition_data = load_vtk(PARTITION_PATH, "Partition_Summary.vtk")

    # Render primal partition
    print("  Rendering primal-partition.png...")
    plot_field(
        renderView1,
        partition_data,
        "partition_0",
        PARTITION_PRESET,
        os.path.join(CURRENT_DIR, "primal-partition.png"),
        resolution=IMG_RES,
        compute_normals=False,
        scheme=COLOR_SCHEME,
    )

    # Render dual partition
    print("  Rendering dual-partition.png...")
    plot_field(
        renderView1,
        partition_data,
        "partition_1",
        PARTITION_PRESET,
        os.path.join(CURRENT_DIR, "dual-partition.png"),
        resolution=IMG_RES,
        compute_normals=False,
        scheme=COLOR_SCHEME,
    )

    print("  Partitions rendered successfully.")


def render_eigenmodes(renderView1):
    """Render eigenmode visualizations."""
    print("Rendering eigenmodes...")

    if not os.path.exists(MODE_GT_PATH):
        print(f"Error: {MODE_GT_PATH} not found. Skipping eigenmodes.")
        return

    mode_gt = load_vtk(MODE_GT_PATH, "mode_gt.vtk")

    for idx in EIGENMODE_INDICES:
        field_name = f"eigenvec_{idx}"
        output_file = os.path.join(CURRENT_DIR, f"eig-{idx}.png")

        print(f"  Rendering {field_name} -> eig-{idx}.png...")

        # Create warp
        warp = WarpByVector(Input=mode_gt)
        warp.Vectors = ["POINTS", field_name]
        warp.ScaleFactor = 2000.0

        # Render
        plot_field(
            renderView1,
            warp,
            field_name,
            EIGENVEC_PRESET,
            output_file,
            resolution=IMG_RES,
            compute_normals=True,
            scheme=COLOR_SCHEME,
        )

    print("  Eigenmodes rendered successfully.")


def main():
    """Main rendering function."""
    print("=" * 60)
    print("Board Model Renderer")
    print("=" * 60)

    # Setup View
    renderView1 = setup_view(CAMERA_PARAMS)

    # Set Layout Size
    layout = GetLayout()
    layout.SetSize(IMG_RES[0], IMG_RES[1])

    # Render all images
    render_partitions(renderView1)
    render_eigenmodes(renderView1)

    print("=" * 60)
    print("All rendering completed successfully!")
    print("=" * 60)
    print("\nGenerated files:")
    for f in ["primal-partition.png", "dual-partition.png"] + [
        f"eig-{i}.png" for i in EIGENMODE_INDICES
    ]:
        fpath = os.path.join(CURRENT_DIR, f)
        if os.path.exists(fpath):
            print(f"  ✓ {f}")
        else:
            print(f"  ✗ {f} (failed)")


if __name__ == "__main__":
    main()
