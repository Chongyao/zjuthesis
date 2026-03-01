import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOURCE_DATA_DIR = os.path.join(PROJECT_ROOT, "source_data", "pd-partition-demo")

VTK_FILES = {
    "quad": os.path.join(SOURCE_DATA_DIR, "quad.vtk"),
    "S1_all_modes": os.path.join(SOURCE_DATA_DIR, "S1_all_modes.vtk"),
    "S1_shift_all_modes": os.path.join(SOURCE_DATA_DIR, "S1_shift_all_modes.vtk"),
}
