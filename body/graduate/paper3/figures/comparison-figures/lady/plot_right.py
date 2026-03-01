import os
import sys

# Add parent directory to path to import pv_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pv_utils import setup_view, load_vtk, plot_field, ensure_symlinks, load_json
from paraview.simple import GetLayout

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
MODEL_NAME = "lady"
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
SOURCE_DATA_DIR = os.path.join(PROJECT_ROOT, "source_data", "lady")
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Presets
PRESETS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "color_presets.json"
)
PRESETS = load_json(PRESETS_PATH)
PARTITION_PRESET = PRESETS.get("partition", "custom")
EIGENVEC_PRESET = PRESETS.get("eigenvec", "custom")
COLOR_SCHEME = PRESETS.get("scheme", "blue_orange")

# Trace resolution: [1048, 666]
IMG_RES = [1048, 666]

# Camera Settings from Trace
CAMERA_PARAMS = {
    "ViewSize": [1048, 666],
    "OrientationAxesVisibility": 0,
    "CenterOfRotation": [
        -0.00037429880344985733,
        2.100755660006115e-05,
        10.46037182685125,
    ],
    "CameraPosition": [-0.00037429880344985733, -57.550328526139445, 10.46037182685125],
    "CameraFocalPoint": [
        -0.00037429880344985733,
        2.100755660006115e-05,
        10.46037182685125,
    ],
    "CameraViewUp": [0.0, 0.0, 1.0],
    "CameraFocalDisk": 1.0,
    "CameraParallelScale": 14.89512651162751,
}

MODES_TO_PLOT = [1, 25, 47]


# -----------------------------------------------------------------------------
# Execution
# -----------------------------------------------------------------------------
def main():
    # 1. Setup View
    renderView1 = setup_view(CAMERA_PARAMS)

    # Set Layout Size
    layout = GetLayout()
    layout.SetSize(IMG_RES[0], IMG_RES[1])

    # Load combined Partition_Summary.vtk (contains both Partition 0 and Partition 1)
    partition_summary_path = os.path.join(SOURCE_DATA_DIR, "Partition_Summary.vtk")

    if os.path.exists(partition_summary_path):
        partition_source = load_vtk(partition_summary_path, "Partition_Summary.vtk")

        print("Plotting Primal Partition (partition_0)...")
        plot_field(
            renderView1,
            partition_source,
            "partition_0",
            PARTITION_PRESET,
            os.path.join(CURRENT_DIR, "right-primal-partition.png"),
            resolution=IMG_RES,
            compute_normals=True,
            scheme=COLOR_SCHEME,
        )

        print("Plotting Dual Partition (partition_1)...")
        plot_field(
            renderView1,
            partition_source,
            "partition_1",
            PARTITION_PRESET,
            os.path.join(CURRENT_DIR, "right-dual-partition.png"),
            resolution=IMG_RES,
            compute_normals=True,
            transparent=False,
            scheme=COLOR_SCHEME,
        )
    else:
        print("Warning: Partition_Summary.vtk not found.")

    print("Plotting Eigenmodes...")
    mode_gt_path = os.path.join(SOURCE_DATA_DIR, "mode_gt.vtk")
    if os.path.exists(mode_gt_path):
        modes_source = load_vtk(mode_gt_path, "mode_gt.vtk")

        for mode in MODES_TO_PLOT:
            field = f"eigenvec_{mode}"
            output = f"eig-{mode}.png"
            print(f"  {field} -> {output}")

            plot_field(
                renderView1,
                modes_source,
                field,
                EIGENVEC_PRESET,
                os.path.join(CURRENT_DIR, output),
                resolution=IMG_RES,
                compute_normals=False,  # Often false for modes to avoid grid artifacts
                scheme=COLOR_SCHEME,
            )
    else:
        print("Warning: mode_gt.vtk not found.")

    print("Rendering completed.")


if __name__ == "__main__":
    main()
