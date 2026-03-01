#!/usr/bin/env python3
"""
All-in-one script: Render selected modes and stitch them into final figures.
No intermediate files are kept - only final stitched images are saved.

Usage:
    python3 render_and_stitch.py --preset "Fast"
    python3 render_and_stitch.py --preset "Cool to Warm"
    python3 render_and_stitch.py --custom-colormap '[[0,0.2,0.4,0.8],[0.5,1,1,1],[1,0.8,0.4,0.2]]'
"""

import os
import re
import json
import shutil
import subprocess
import argparse
import tempfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from PIL import Image

# ============================================================================
# Configuration
# ============================================================================

PVBATCH = (
    "/home/zcy/Applications/ParaView-6.0.1-MPI-Linux-Python3.12-x86_64/bin/pvbatch"
)
RENDER_SCRIPT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "render_single.py"
)
SELECTED_MODES_JSON = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "selected_modes.json"
)
OUTPUT_DIR = "final_stitched"

WARP_RATIO = 0.07
VIEW_SIZE = [2146, 1358]
CAMERA_VIEW_UP = [0, 1, 0]
MAX_WORKERS = 8
GAP = 20  # Gap between stitched images

FILE_PATTERNS = {
    "primal_interior_modes": "interior_modes_primal_sub{}.vtk",
    "dual_interior_modes": "interior_modes_dual_sub{}.vtk",
    "primal_interface_modes": "interface_modes_primal_sub{}.vtk",
    "dual_interface_modes": "interface_modes_dual_sub{}.vtk",
}

PRESET_SLUGS = {
    "Fast": "fast",
    "Cool to Warm": "coolwarm",
}

# ============================================================================
# Helper Functions
# ============================================================================


def load_selected_modes():
    with open(SELECTED_MODES_JSON, "r") as f:
        config = json.load(f)

    data_dir = config["data_source"]
    whitelist = []

    for category, cat_config in config["categories"].items():
        vtk_pattern = cat_config["vtk_pattern"]

        for mode_entry in cat_config["modes"]:
            sub_index = mode_entry["submesh"]
            mode_index = mode_entry["mode"]

            vtk_filename = vtk_pattern.format(sub_index)
            vtk_path = os.path.join(data_dir, vtk_filename)

            if not os.path.exists(vtk_path):
                print(f"Warning: VTK not found: {vtk_path}")
                continue

            whitelist.append(
                {
                    "category": category,
                    "sub_index": sub_index,
                    "mode_index": mode_index,
                    "mode_name": f"mode_{mode_index}",
                    "vtk_path": vtk_path,
                    "output_filename": f"sub_{sub_index}_mode_{mode_index}.png",
                }
            )

    return whitelist


def extract_whitelist():
    return load_selected_modes()


def get_submesh_index(filename):
    """Extract submesh index from filename for sorting."""
    match = re.search(r"sub_(\d+)", filename)
    return int(match.group(1)) if match else -1


def render_task(task):
    """Execute single render task."""
    vtk_path = task["vtk_path"]
    mode_name = task["mode_name"]
    output_path = task["output_path"]
    colormap = task.get("colormap")
    custom_colormap = task.get("custom_colormap")
    preset_file = task.get("preset_file")

    cmd = [
        PVBATCH,
        "--mesa",
        RENDER_SCRIPT,
        f"--input={vtk_path}",
        f"--mode={mode_name}",
        f"--output={output_path}",
        f"--warp-ratio={WARP_RATIO}",
        f"--view-size={VIEW_SIZE[0]},{VIEW_SIZE[1]}",
        "--auto-camera",
        f"--camera-view-up={CAMERA_VIEW_UP[0]},{CAMERA_VIEW_UP[1]},{CAMERA_VIEW_UP[2]}",
    ]

    if custom_colormap:
        cmd.append(f"--custom-colormap={custom_colormap}")
    elif colormap:
        cmd.append(f"--colormap={colormap}")
        if preset_file:
            cmd.append(f"--preset-file={preset_file}")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return (output_path, False, result.stderr[:200])
    else:
        return (output_path, True, "OK")


def stitch_category(category_name, temp_dir):
    """Stitch images from a category into a single vertical strip."""
    src_path = os.path.join(temp_dir, category_name)
    if not os.path.exists(src_path):
        return None

    files = [f for f in os.listdir(src_path) if f.endswith(".png")]
    sorted_files = sorted(files, key=get_submesh_index)

    if not sorted_files:
        return None

    print(f"  Stitching {category_name} ({len(sorted_files)} images)...")

    images = []
    for f in sorted_files:
        img_path = os.path.join(src_path, f)
        img = Image.open(img_path).convert("RGBA")
        images.append(img)

    max_width = max(img.width for img in images)
    total_height = sum(img.height for img in images) + GAP * (len(images) - 1)

    canvas = Image.new("RGBA", (max_width, total_height), (0, 0, 0, 0))

    # Stack from bottom to top (sub0 at bottom, subK at top)
    current_y = total_height
    for img in images:
        y_pos = current_y - img.height
        x_pos = (max_width - img.width) // 2
        canvas.paste(img, (x_pos, y_pos), img)
        current_y = y_pos - GAP

    return canvas


# ============================================================================
# Main Pipeline
# ============================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Render and stitch mode shapes in one go"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preset", help="Colormap preset name")
    group.add_argument(
        "--custom-colormap",
        help="Custom colormap as JSON: [[val,r,g,b], ...] where val in [0,1], rgb in [0,1]",
    )

    parser.add_argument(
        "--preset-file",
        help="Path to external ParaView JSON preset file (use with --preset)",
    )

    args = parser.parse_args()

    if args.preset and not args.preset_file:
        if args.preset not in PRESET_SLUGS:
            print(
                f"Error: Preset '{args.preset}' not known. Available: {list(PRESET_SLUGS.keys())}"
            )
            print("To use a custom preset name, you must also provide --preset-file")
            return 1

    if args.preset:
        if args.preset_file:
            filename = os.path.splitext(os.path.basename(args.preset_file))[0]
            output_slug = filename.lower().replace(" ", "_")
        else:
            output_slug = PRESET_SLUGS[args.preset]
        colormap_name = args.preset
    else:
        output_slug = "custom"
        colormap_name = "Custom"

    print("=" * 70)
    print(f"Mode Shape Renderer & Stitcher")
    print(f"Colormap: {colormap_name}")
    print(f"Output: {OUTPUT_DIR}/{output_slug}_*.png")
    print("=" * 70)

    # Step 1: Extract whitelist
    whitelist = extract_whitelist()
    print(f"\nFound {len(whitelist)} selected modes")

    if not whitelist:
        print("ERROR: No modes found")
        return 1

    # Step 2: Render to intermediate directory (kept for inspection)
    intermediate_dir_name = f"intermediate_renders_{output_slug}"
    temp_dir = os.path.abspath(intermediate_dir_name)
    os.makedirs(temp_dir, exist_ok=True)

    print(f"\nRendering to intermediate directory: {temp_dir}")

    try:
        tasks = []
        for item in whitelist:
            cat_output_dir = os.path.join(temp_dir, item["category"])
            os.makedirs(cat_output_dir, exist_ok=True)

            output_path = os.path.join(cat_output_dir, item["output_filename"])

            task = {
                "vtk_path": item["vtk_path"],
                "mode_name": item["mode_name"],
                "output_path": output_path,
            }

            if args.preset:
                task["colormap"] = args.preset
                if args.preset_file:
                    task["preset_file"] = args.preset_file
            else:
                task["custom_colormap"] = args.custom_colormap

            tasks.append(task)

        print(f"\nRendering {len(tasks)} images with {MAX_WORKERS} workers...")
        print("-" * 70)

        success_count = 0
        error_count = 0

        with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_task = {}
            for task in tasks:
                if os.path.exists(task["output_path"]):
                    print(
                        f"  Skipping existing: {os.path.basename(task['output_path'])}"
                    )
                    success_count += 1
                    continue

                future = executor.submit(render_task, task)
                future_to_task[future] = task

            if future_to_task:
                for i, future in enumerate(as_completed(future_to_task)):
                    task = future_to_task[future]
                    try:
                        output_path, success, msg = future.result()
                        filename = os.path.basename(output_path)

                        if success:
                            success_count += 1
                            print(f"  [Rendered] ✓ {filename}")
                        else:
                            error_count += 1
                            print(f"  [Failed] ✗ {filename}: {msg}")
                    except Exception as e:
                        error_count += 1
                        print(f"  [Exception] ✗ {e}")

        if error_count > 0:
            print(f"\nERROR: {error_count} renders failed. Aborting.")
            return 1

        print(f"\n{'=' * 70}")
        print(f"Rendering complete! {success_count}/{len(tasks)} images")
        print("=" * 70)

        # Step 3: Stitch images
        print("\nStitching images...")
        print("-" * 70)

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        categories = [
            "primal_interior_modes",
            "dual_interior_modes",
            "primal_interface_modes",
            "dual_interface_modes",
        ]

        for cat in categories:
            canvas = stitch_category(cat, temp_dir)
            if canvas:
                output_filename = f"{output_slug}_{cat}_stitched.png"
                output_path = os.path.join(OUTPUT_DIR, output_filename)
                canvas.save(output_path)
                print(f"  ✓ Saved {output_filename} ({canvas.width}x{canvas.height})")

        print("\n" + "=" * 70)
        print(f"All done! Final images saved to: {OUTPUT_DIR}/")
        print("=" * 70)

    finally:
        # Step 4: Intermediate files are kept
        print(f"\nIntermediate files kept at: {temp_dir}")
        # shutil.rmtree(temp_dir)  # Disabled cleanup

    return 0


if __name__ == "__main__":
    exit(main())
