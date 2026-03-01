# state file generated using paraview version 6.0.1
import os
import paraview

paraview.compatibility.major = 6
paraview.compatibility.minor = 0

#### import the simple module from the paraview
from paraview.simple import *

# Path setup
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(CURRENT_DIR))
SOURCE_DATA_DIR = os.path.join(PROJECT_ROOT, "source_data", "domain_definition")
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView("RenderView")
renderView1.Set(
    ViewSize=[2146, 1032],
    InteractionMode="2D",
    OrientationAxesVisibility=0,
    CenterOfRotation=[0.5, 0.5, 0.0],
    UseToneMapping=1,
    UseAmbientOcclusion=1,
    CameraPosition=[0.5663255197857149, 0.577932485748215, 3.35],
    CameraFocalPoint=[0.5663255197857149, 0.577932485748215, 0.0],
    CameraFocalDisk=1.0,
    CameraParallelScale=0.7071067811865474,
    OSPRayMaterialLibrary=materialLibrary1,
)

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name="Layout #1")
layout1.AssignView(0, renderView1)
layout1.SetSize(2146, 1032)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
all_modesvtk = LegacyVTKReader(
    registrationName="all_modes.vtk",
    FileNames=[os.path.join(SOURCE_DATA_DIR, "all_modes.vtk")],
)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from all_modesvtk
all_modesvtkDisplay = Show(all_modesvtk, renderView1, "UnstructuredGridRepresentation")

# get color transfer function/color map for 'eigenvec_20'
eigenvec_20LUT = GetColorTransferFunction("eigenvec_20")
eigenvec_20LUT.Set(
    RGBPoints=GenerateRGBPoints(
        preset_name="Cool to Warm",
        range_min=-4.0,
        range_max=4.000000000000007,
    ),
    ColorSpace="Diverging",
    NanColor=[1.0, 1.0, 0.0],
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
all_modesvtkDisplay.Set(
    Representation="Surface",
    ColorArrayName=["POINTS", "eigenvec_20"],
    LookupTable=eigenvec_20LUT,
)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'eigenvec_20'
eigenvec_20PWF = GetOpacityTransferFunction("eigenvec_20")
eigenvec_20PWF.Set(
    Points=[-4.0, 0.0, 0.5, 0.0, 4.000000000000007, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.Set(
    ViewModules=renderView1,
    Cues=timeAnimationCue1,
    AnimationTime=0.0,
)

# ----------------------------------------------------------------
# restore active source
SetActiveSource(all_modesvtk)
# ----------------------------------------------------------------


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/nightly/python/
##--------------------------------------------
