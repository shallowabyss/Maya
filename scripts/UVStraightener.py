# *****************************************************
# Name: UVStraightener
# Author: Chris Peterson
# This script will take edges (separating all of the polys you want to UV)
# and create a straight UV strip from them.
# *****************************************************

# import our library
import pymel.core as pm


# create an undo state
pm.undoInfo(openChunk=True)
try:
    # store our edge list
    edgesList = pm.ls(sl=True, fl=True)
    # convert to polys (not contained polys)
    pm.polyListComponentConversion(edgesList, fe=True, tf=True, internal=False)
    # store our poly list
    polyList = pm.ls(sl=True)
    # auto project all polygons
    pm.polyAutoProjection(polyList, lm=0, pb=0, ibd=1, cm=0, l=2, sc=1, o=1, p=6, ps=0.2, ws=0)
    # unitize all polygons (make them squares normalized to 0 to 1 uv space)
    pm.polyForceUV(unitize=True)

    # clear poly selection
    pm.select(cl=True)
    # select all edges -1 so that it doesnt weld all of them together (leaves it in a strip)
    for i in range(0, len(edgesList) - 1):
        pm.select(edgesList[i], tgl=True)
    # current selected edges will be moved and sewn
    mergeEdgeList = pm.ls(sl=True)
    # move and sew them
    pm.polyMapSewMove(mergeEdgeList, nf=10, lps=0, ch=1)

    # select polygons again
    pm.select(polyList, r=True)
    # unfold them based on vertical edges
    pm.unfold(i=5000, ss=0.001, gb=0, gmb=0.5, pub=0, ps=0, oa=1, us=False)
    # normalize to fit in 0 to 1 UV space
    pm.polyNormalizeUV(normalizeType=1, preserveAspectRatio=1, centerOnTile=0)

except Exception as err:
    print(str(err))
# close undo state
pm.undoInfo(closeChunk=True)
