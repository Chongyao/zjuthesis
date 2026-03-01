# trace generated using paraview version 6.0.1
#import paraview
#paraview.compatibility.major = 6
#paraview.compatibility.minor = 0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
partition_Summaryvtk = LegacyVTKReader(registrationName='Partition_Summary.vtk', FileNames=['/home/zcy/workspace/projects/arborecence/pipline/cms_local_update/micro/origin_partition/Partition_Summary.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
partition_SummaryvtkDisplay = Show(partition_Summaryvtk, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
partition_SummaryvtkDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
partition_SummaryvtkDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'fixed'
fixedLUT = GetColorTransferFunction('fixed')

# get opacity transfer function/opacity map for 'fixed'
fixedPWF = GetOpacityTransferFunction('fixed')

# get 2D transfer function for 'fixed'
fixedTF2D = GetTransferFunction2D('fixed')

# hide color bar/color legend
partition_SummaryvtkDisplay.SetScalarBarVisibility(renderView1, False)

# Properties modified on renderView1
renderView1.Exposure = 4.0

# Properties modified on renderView1
renderView1.Exposure = 3.0

# set scalar coloring
ColorBy(partition_SummaryvtkDisplay, ('POINTS', 'partition_0'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(fixedLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
partition_SummaryvtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
partition_SummaryvtkDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'partition_0'
partition_0LUT = GetColorTransferFunction('partition_0')

# get opacity transfer function/opacity map for 'partition_0'
partition_0PWF = GetOpacityTransferFunction('partition_0')

# get 2D transfer function for 'partition_0'
partition_0TF2D = GetTransferFunction2D('partition_0')

renderView1.ResetActiveCameraToNegativeZ()

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# hide color bar/color legend
partition_SummaryvtkDisplay.SetScalarBarVisibility(renderView1, False)

# rescale color and/or opacity maps used to exactly fit the current data range
partition_SummaryvtkDisplay.RescaleTransferFunctionToDataRange(False, True)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(3004, 1022)

# current camera placement for renderView1
renderView1.Set(
    CameraPosition=[5.0, 1.0, 10.3657847046269],
    CameraFocalPoint=[5.0, 1.0, 1.0],
    CameraParallelScale=5.196152422706632,
)

# save screenshot
SaveScreenshot(filename='/home/zcy/workspace/records/primal-dual_modes/figures/local_update/micro_origin_primal.png', viewOrLayout=renderView1, location=16, ImageResolution=[3004, 1022],
    TransparentBackground=1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(3004, 1022)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.Set(
    CameraPosition=[5.0, 1.0, 10.3657847046269],
    CameraFocalPoint=[5.0, 1.0, 1.0],
    CameraParallelScale=5.196152422706632,
)


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