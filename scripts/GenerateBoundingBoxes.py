#*****************************************************
# Name: GenerateBoundingBoxes
# Author: Chris Peterson
# This script will generate bounding boxes from the 
# selected objects.
#*****************************************************

import maya.cmds as cmds

try:
    sel = cmds.ls(sl=True)
    cmds.undoInfo(openChunk=True)
    if len(sel) > 0:
        for item in sel:
            cmds.select(item,r=True)
            geobbox = cmds.geomToBBox(keepOriginal=True,single=True, name="%s_BBox" % item)
            cmds.parent(geobbox,item)
        cmds.select(sel,r=True)
    else:
        cmds.warning('You need to have something selected in order to create bounding boxes.')
except:
    pass
finally:
    cmds.undoInfo(closeChunk=True)