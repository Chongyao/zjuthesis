import os
import sys
import json
import re
from PIL import Image, ImageOps
from collections import defaultdict

# Add parent directory to path to import pv_utils
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../comparison-figures")
    ),
)

from pv_utils import setup_view, load_vtk, plot_field, ensure_symlinks, load_json
from paraview.simple import GetLayout

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
SOURCE_DATA_DIR = os.path.join(PROJECT_ROOT, "source_data", "interface-modes-example")
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = "render_config.json"

# Load Presets
PRESETS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "comparison-figures",
    "color_presets.json",
)
PRESETS = load_json(PRESETS_PATH)
EIGENVEC_PRESET = PRESETS.get("eigenvec", "Fast")
COLOR_SCHEME = PRESETS.get("scheme", "blue_orange")

# Trace resolution: [2328, 1358]
IMG_RES = [2328, 1358]


# -----------------------------------------------------------------------------
# Execution
# -----------------------------------------------------------------------------
def main():
    config_path = os.path.join(CURRENT_DIR, CONFIG_FILE)
    if not os.path.exists(config_path):
        print(f"Error: Config file {CONFIG_FILE} not found.")
        return

    with open(config_path, "r") as f:
        config = json.load(f)

    # 1. Setup View (Default)
    # We might update this per model if camera params differ
    renderView1 = None
    layout = None

    for entry in config:
        vtk_file = entry["vtk"]
        camera_params = entry.get("camera", {})
        plots = entry.get("plots", [])

        print(f"Processing {vtk_file}...")

        # Update or Create View
        if renderView1 is None or camera_params:
            # If explicit camera params provided, use them.
            # Note: setup_view creates a NEW view/session logic usually,
            # but pv_utils.setup_view calls GetActiveViewOrCreate.
            # So calling it again updates the existing view.
            renderView1 = setup_view(camera_params)
            renderView1.Exposure = 2.0

            if layout is None:
                layout = GetLayout()
                layout.SetSize(IMG_RES[0], IMG_RES[1])

        # 2. Ensure Data (Symlink check - simplistic here, assumes file exists or symlinked manually)
        # We can try ensure_symlinks if we know source dir, but json doesn't specify it.
        # Assuming files are present in current dir or are absolute paths.

        # 3. Load Data from source_data directory
        vtk_path = os.path.join(SOURCE_DATA_DIR, vtk_file)

        vtk_source = load_vtk(vtk_path, vtk_file)

        if not vtk_source:
            print(f"  Error: Could not load {vtk_file}")
            continue

        # 4. Plot Modes
        for plot in plots:
            field = plot["field"]
            output = plot["output"]
            preset = plot.get("preset", EIGENVEC_PRESET)  # Allow override or default

            print(f"  Plotting {field} -> {output}")

            plot_field(
                renderView1,
                vtk_source,
                field,
                preset,
                os.path.join(CURRENT_DIR, output),
                resolution=IMG_RES,
                compute_normals=False,
                scheme=COLOR_SCHEME,
            )

    print("Batch rendering completed.")

    # 5. Post-processing: Add borders, concatenate, and cleanup
    print("\nPost-processing images...")
    post_process_images(CURRENT_DIR, config)


def post_process_images(directory, config, border_width=2, border_color="black"):
    """
    Add borders to images, concatenate same-prefix images horizontally,
    and delete individual images.
    """
    # Collect all output files and group by prefix
    # Pattern: prefix-N.png where N is a number
    pattern = re.compile(r"^(.+)-(\d+)\.png$")

    groups = defaultdict(list)

    for entry in config:
        for plot in entry.get("plots", []):
            output = plot["output"]
            match = pattern.match(output)
            if match:
                prefix = match.group(1)
                index = int(match.group(2))
                groups[prefix].append((index, output))

    for prefix, files in groups.items():
        # Sort by index
        files.sort(key=lambda x: x[0])

        images_with_border = []
        file_paths = []

        for _, filename in files:
            filepath = os.path.join(directory, filename)
            if not os.path.exists(filepath):
                print(f"  Warning: {filename} not found, skipping...")
                continue

            # Load and add border
            img = Image.open(filepath)
            if img.mode == "P":
                img = img.convert("RGBA")
            img_with_border = ImageOps.expand(
                img, border=border_width, fill=border_color
            )
            images_with_border.append(img_with_border)
            file_paths.append(filepath)

        if not images_with_border:
            continue

        # Concatenate horizontally
        total_width = sum(img.width for img in images_with_border)
        max_height = max(img.height for img in images_with_border)

        combined = Image.new("RGB", (total_width, max_height))
        x_offset = 0
        for img in images_with_border:
            combined.paste(img, (x_offset, 0))
            x_offset += img.width

        # Save combined image
        combined_path = os.path.join(directory, f"{prefix}-combined.png")
        combined.save(combined_path)
        print(f"  Created: {prefix}-combined.png")

        # Delete individual images
        for filepath in file_paths:
            os.remove(filepath)
            print(f"  Deleted: {os.path.basename(filepath)}")


if __name__ == "__main__":
    main()
