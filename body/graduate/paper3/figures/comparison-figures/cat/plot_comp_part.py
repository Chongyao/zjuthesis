import os
import sys

# Add parent directory to path to import pv_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pv_utils import (
    setup_view,
    load_vtk,
    plot_field,
    ensure_symlinks,
    post_process_image,
    load_json,
    apply_preset,
)
from paraview.simple import (
    GetLayout,
    QuerySelect,
    ExtractSelection,
    Show,
    Hide,
    ClearSelection,
    Delete,
    SaveScreenshot,
    ColorBy,
    SetActiveSource,
    GetColorTransferFunction,
)

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
MODEL_NAME = "cat"
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
SOURCE_DIR = os.path.join(PROJECT_ROOT, "source_data", "cat")
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Presets
PRESETS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "color_presets.json"
)
PRESETS = load_json(PRESETS_PATH)
PARTITION_PRESET = PRESETS.get("partition", "custom")
COLOR_SCHEME = PRESETS.get("scheme", "teal_coral")

# Trace resolution: [2146, 1110]
IMG_RES = [2146, 1110]

# Define the sequence of plots: (Field Name, Output Filename, Camera Params)
PLOT_SEQUENCE = [
    (
        "partition_2",
        "comp-2.png",
        {
            "CameraPosition": [
                17.57652338436137,
                200.8450735085944,
                -14.20469364511201,
            ],
            "CameraFocalPoint": [
                15.312673887873107,
                13.140267050164566,
                30.37993403961364,
            ],
            "CameraViewUp": [
                -0.01779473002082546,
                0.23126222749893346,
                0.9727287030388881,
            ],
            "CameraParallelScale": 60.42335509416216,
        },
    ),
    (
        "partition_3",
        "comp-3.png",
        {
            "CameraPosition": [
                172.96370507501433,
                69.52937874556517,
                40.56605783103739,
            ],
            "CameraFocalPoint": [
                21.223822937926126,
                21.603635935870273,
                30.368216034427945,
            ],
            "CameraViewUp": [
                -0.06499981559196516,
                -0.006530809133101347,
                0.9978639048011896,
            ],
            "CameraParallelScale": 60.42335509416216,
        },
    ),
    (
        "partition_4",
        "comp-4.png",
        {
            "CameraPosition": [
                -13.060542549731295,
                -141.5298459362483,
                30.098841384449408,
            ],
            "CameraFocalPoint": [
                20.358858010202646,
                14.383373488714561,
                30.375078430445814,
            ],
            "CameraViewUp": [
                0.016726048454316342,
                -0.005356626946958351,
                0.9998457610305976,
            ],
            "CameraParallelScale": 60.42335509416216,
        },
    ),
    (
        "partition_5",
        "comp-5.png",
        {
            "CameraPosition": [
                -168.85196885506087,
                23.528630524909016,
                44.770376829394976,
            ],
            "CameraFocalPoint": [
                23.453623838326568,
                17.069671049067843,
                30.52786057479183,
            ],
            "CameraViewUp": [
                0.07157416317909487,
                -0.06389545415032435,
                0.9953866133840339,
            ],
            "CameraParallelScale": 60.42335509416216,
        },
    ),
]


# -----------------------------------------------------------------------------
# Execution
# -----------------------------------------------------------------------------
def main():
    # 1. Setup View with Basic Settings
    # Load camera config like plot.py
    camera_file = os.path.join(CURRENT_DIR, "camera.json")
    camera_params = load_json(camera_file)
    # Exposure is handled by pv_utils (default 3.0), allowing centralized adjustment
    # camera_params["Exposure"] = 2.0

    renderView1 = setup_view(camera_params)

    # Set Layout Size to match image resolution (prevents LOD artifacts)
    layout = GetLayout()
    layout.SetSize(IMG_RES[0], IMG_RES[1])

    # 2. Ensure Data
    vtk_file = f"{MODEL_NAME}.vtk"

    # 3. Load Data
    vtk_path = os.path.join(SOURCE_DIR, vtk_file)
    catvtk = load_vtk(vtk_path, vtk_file)

    if not catvtk:
        print("Error: Could not load data.")
        return

    # 4. Prepare Selections (Partition 0 and 1)
    selections = []
    HIGHLIGHT_DEFS = [
        ("partition_0", [1.0, 0.4, 0.7]),  # Pink/Magenta
        ("partition_1", [1.0, 0.8, 0.0]),  # Bright Yellow/Gold
    ]

    print("Creating persistent highlights...")
    for field, color in HIGHLIGHT_DEFS:
        SetActiveSource(catvtk)
        QuerySelect(
            QueryString=f"({field} == max({field}))", FieldType="POINT", InsideOut=0
        )

        selection = ExtractSelection(Input=catvtk)
        sel_display = Show(selection, renderView1, "UnstructuredGridRepresentation")
        sel_display.Representation = "Point Gaussian"
        sel_display.GaussianRadius = 0.5

        ColorBy(sel_display, None)
        sel_display.AmbientColor = color
        sel_display.DiffuseColor = color
        print(f"  - {field}: color={color}")

        selections.append((selection, sel_display))
        ClearSelection()

    # 5. Process Backgrounds and Save
    for bg_field, filename, cam_params in PLOT_SEQUENCE:
        print(f"Overlaying highlights on {bg_field} -> {filename}")

        # Update Camera for this specific shot
        for key, val in cam_params.items():
            setattr(renderView1, key, val)

        # Show Background
        catvtkDisplay = Show(catvtk, renderView1, "UnstructuredGridRepresentation")
        catvtkDisplay.ComputePointNormals = 1
        ColorBy(catvtkDisplay, ("POINTS", bg_field))

        # Apply Preset & Rescale
        apply_preset(
            bg_field, PARTITION_PRESET, data_range=(0.0, 2.0), scheme=COLOR_SCHEME
        )
        catvtkDisplay.SetScalarBarVisibility(renderView1, False)

        # Save
        output_path = os.path.join(CURRENT_DIR, filename)
        SaveScreenshot(
            output_path,
            viewOrLayout=renderView1,
            ImageResolution=IMG_RES,
        )
        post_process_image(output_path)

    # 6. Cleanup
    for sel, disp in selections:
        Hide(sel, renderView1)
        Delete(sel)
        del disp

    print("Comparison plots completed.")


if __name__ == "__main__":
    main()
