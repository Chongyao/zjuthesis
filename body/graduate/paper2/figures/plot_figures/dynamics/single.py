# state file generated using paraview version 5.13.0
import paraview

paraview.compatibility.major = 5
paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

id = int(sys.argv[1])
opacity = float(sys.argv[2])
output = sys.argv[3]

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView("RenderView")
renderView1.ViewSize = [2878, 1338]
renderView1.AxesGrid = "Grid Axes 3D Actor"
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0, 0.0, 10.0]
renderView1.UseToneMapping = 1
renderView1.UseAmbientOcclusion = 1
renderView1.StereoType = "Crystal Eyes"
renderView1.CameraPosition = [-43.384171755831, -169.16347971481085, 58.410492208656976]
renderView1.CameraFocalPoint = [0.0, 0.0, 10.0]
renderView1.CameraViewUp = [0.017814047794645547, 0.2708621854108852, 0.962453290407181]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 46.90415608254247
renderView1.LegendGrid = "Legend Grid Actor"
renderView1.PolarGrid = "Polar Grid Actor"
renderView1.BackEnd = "OSPRay raycaster"
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name="Layout #1")
layout1.AssignView(0, renderView1)
layout1.SetSize(2878, 1338)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
warp0vtk = LegacyVTKReader(
    registrationName=f"warp-{id}.vtk",
    FileNames=[
        f"/home/zcy/workspace/projects/arborecence_test/pipline/localAG-smk/output/different_steps/nut/origin/dynamics/warp/warp-{id}.vtk"
    ],
)

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(registrationName="WarpByVector1", Input=warp0vtk)
warpByVector1.Vectors = ["POINTS", "warp_disp"]

# create a new 'Calculator'
calculator1 = Calculator(registrationName="Calculator1", Input=warpByVector1)
calculator1.Function = "0.7"

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, "UnstructuredGridRepresentation")

# get 2D transfer function for 'Result'
resultTF2D = GetTransferFunction2D("Result")
resultTF2D.ScalarRangeInitialized = 1
resultTF2D.Range = [-1.0, 1.0, 0.0, 1.0]

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction("Result")
resultLUT.TransferFunction2D = resultTF2D
resultLUT.RGBPoints = [
    -1.0,
    0.831,
    0.0,
    0.0,
    -0.5,
    1.0,
    0.502,
    0.502,
    -0.1000000000003638,
    1.0,
    0.94,
    0.855,
    0.0,
    1.0,
    0.965,
    0.835,
    0.1000000000003638,
    0.855,
    0.94,
    1.0,
    0.5,
    0.502,
    0.702,
    1.0,
    1.0,
    0.0,
    0.4,
    1.0,
]
resultLUT.ColorSpace = "RGB"
resultLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction("Result")
resultPWF.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
resultPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = "Surface"
calculator1Display.ColorArrayName = ["POINTS", "Result"]
calculator1Display.LookupTable = resultLUT
calculator1Display.Opacity = opacity
calculator1Display.SelectNormalArray = "None"
calculator1Display.SelectTangentArray = "None"
calculator1Display.ComputePointNormals = 1
calculator1Display.SelectTCoordArray = "None"
calculator1Display.TextureTransform = "Transform2"
calculator1Display.OSPRayScaleArray = "Result"
calculator1Display.OSPRayScaleFunction = "Piecewise Function"
calculator1Display.Assembly = ""
calculator1Display.SelectedBlockSelectors = [""]
calculator1Display.SelectOrientationVectors = "ori_disp"
calculator1Display.ScaleFactor = 7.131706454865416
calculator1Display.SelectScaleArray = "Result"
calculator1Display.GlyphType = "Arrow"
calculator1Display.GlyphTableIndexArray = "Result"
calculator1Display.GaussianRadius = 0.3565853227432708
calculator1Display.SetScaleArray = ["POINTS", "Result"]
calculator1Display.ScaleTransferFunction = "Piecewise Function"
calculator1Display.OpacityArray = ["POINTS", "Result"]
calculator1Display.OpacityTransferFunction = "Piecewise Function"
calculator1Display.DataAxesGrid = "Grid Axes Representation"
calculator1Display.PolarAxes = "Polar Axes Representation"
calculator1Display.ScalarOpacityFunction = resultPWF
calculator1Display.ScalarOpacityUnitDistance = 2.261627533903343
calculator1Display.OpacityArrayName = ["POINTS", "Result"]
calculator1Display.SelectInputVectors = ["POINTS", "ori_disp"]
calculator1Display.WriteLog = ""

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [
    0.7,
    0.0,
    0.5,
    0.0,
    0.700122058391571,
    1.0,
    0.5,
    0.0,
]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [
    0.7,
    0.0,
    0.5,
    0.0,
    0.700122058391571,
    1.0,
    0.5,
    0.0,
]

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

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
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.0
animationScene1.Loop = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(calculator1)
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
SaveScreenshot(output)
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
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
