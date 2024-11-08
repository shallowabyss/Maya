#*****************************************************
# Name: VertexColorNormal
# Author: Chris Peterson
# Description: This tool will generate smooth vertex face
# normals and apply their values to the vertex color of
# each face. This data is exported (by default) with FBXs
# and can be used with special shaders to apply a point 
# normal move/scaling effect for glows, displacement, etc.
#*****************************************************

import pymel.core as pm
import time



startTime = time.clock()
# turn undo stack on
pm.undoInfo(state=True)
# get list of selected objects
objList = pm.ls(sl=True,type='transform')
# make sure something is selected
if objList is not None:
    # loop through objects
    for obj in objList:
        print(obj)
        try:
            # select the first object in the list
            pm.select(obj,r=True)
            pm.undoInfo(state=True)
            # need to modify construction history to force the generation of faces
            pm.polyTriangulate(obj,ch=1)
            # now undo it and it should work
            pm.undo()
            pm.undoInfo(state=False)
            # dupe the geometry which kills history and can cause errors
            dupe = pm.duplicate(rr=True)[0]
            # switch to component mode
            pm.selectMode( component=True )
            # get the number of faces
            faceCount = pm.polyEvaluate(dupe,face=True)
            # select all of the faces
            pm.select(dupe + '.f[*:*]',r=True)
            # get list of faces
            allFaces = pm.ls(sl=True,fl=True)
            # convert faces to vertex faces for all faces
            pm.polyListComponentConversion(allFaces , ff=True, tvf=True )
            # select all vertex faces of the original object
            pm.select(obj + '.vtxFace[*:*]',r=True)
            # get list of vertex faces of the original
            vtxFaceSel = pm.ls(sl=True,fl=True)
            # change to object selection mode
            pm.selectMode( object=True )
            # select the dupe object
            pm.select(dupe,r=True)
            # smooth normals to 180 degrees
            pm.polySoftEdge( a=180 )
            # change to component selection mode
            pm.selectMode( component=True )

            # loop through all vertices and apply their vertex color information
            for i in range(0,len(vtxFaceSel)):
                # get the name of the vertex so that we dont need to store two identical arrays
                dupeVtxFace = dupe + '.' + vtxFaceSel[i].split('.')[1]
                # select the dupe (smooth) vertex face
                pm.select(dupeVtxFace,r=True)
                # get vertex normal
                vtxNrmSmooth = pm.polyNormalPerVertex(query=True, xyz=True)
                # select the original mesh vertex face
                pm.select(vtxFaceSel[i],r=True)
                # Math to calculate normal colors
                r = (-vtxNrmSmooth[0] * 0.5) + 0.5
                g = (vtxNrmSmooth[1] * 0.5) + 0.5
                b = (vtxNrmSmooth[2] * 0.5) + 0.5
                # Set the vertex colors to the normal colors
                pm.polyColorPerVertex( rgb=(r, g, b) )
            # change to object selection mode
            pm.selectMode( object=True )
            # delete the dupe
            pm.delete(dupe)
            # update progress bar
            #pm.progressBar(gMainProgressBar, edit=True, step=1)
        except Exception as e:
            pm.warning(str(e))

# select our original objects
pm.select(objList,r=True)
# close our undo chunk
#pm.undoInfo(closeChunk=True)
#pm.progressBar(gMainProgressBar, edit=True, endProgress=True)
endTime = time.clock()
print ('Processed completed in %s seconds.' % (endTime-startTime))
print('vertex color information applied.')
# turn undo stack on
pm.undoInfo(state=True)