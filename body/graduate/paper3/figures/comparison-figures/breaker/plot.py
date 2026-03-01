#!/home/zcy/Applications/ParaView-6.0.1-MPI-Linux-Python3.12-x86_64/bin/pvbatch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import pv_utils
except ImportError:
    sys.path.append("..")
    import pv_utils

MODEL_NAME = "breaker"
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
SOURCE_DIR = os.path.join(PROJECT_ROOT, "source_data", "breaker")
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

MODES_TO_PLOT = [1, 25, 47]


def main():
    camera_file = os.path.join(CURRENT_DIR, "camera.json")
    preset_file = os.path.join(os.path.dirname(pv_utils.__file__), "color_presets.json")

    camera_params = pv_utils.load_json(camera_file)
    presets = pv_utils.load_json(preset_file)

    scheme = presets.get("scheme", "blue_orange")

    vtk_file = f"{MODEL_NAME}.vtk"
    modes_file = f"{MODEL_NAME}-modes.vtk"

    view = pv_utils.setup_view(camera_params)
    img_res = [2146, 1358]

    vtk_path = os.path.join(SOURCE_DIR, vtk_file)
    model_source = pv_utils.load_vtk(vtk_path, vtk_file)

    if model_source:
        print("Plotting partitions...")
        part_preset = presets.get("partition", "Fast")

        pv_utils.plot_field(
            view,
            model_source,
            "partition_0",
            part_preset,
            os.path.join(CURRENT_DIR, "primal-partition.png"),
            resolution=img_res,
            compute_normals=False,
            scheme=scheme,
        )

        pv_utils.plot_field(
            view,
            model_source,
            "partition_1",
            part_preset,
            os.path.join(CURRENT_DIR, "dual-partition.png"),
            resolution=img_res,
            compute_normals=False,
            scheme=scheme,
        )

    modes_path = os.path.join(SOURCE_DIR, modes_file)
    modes_source = pv_utils.load_vtk(modes_path, modes_file)

    if modes_source:
        print("Plotting modes...")
        eig_preset = presets.get("eigenvec", "Fast")

        for mode_idx in MODES_TO_PLOT:
            field_name = f"eigenvec_{mode_idx}"
            print(f"  - {field_name}")
            out_path = os.path.join(CURRENT_DIR, f"eig-{mode_idx}.png")
            pv_utils.plot_field(
                view,
                modes_source,
                field_name,
                eig_preset,
                out_path,
                resolution=img_res,
                compute_normals=True,
                scheme=scheme,
            )


if __name__ == "__main__":
    main()
