#*****************************************************
# Name: FixShapeNodes
# Author: Chris Peterson
# This script will rename the shape nodes of each transform to make them
# match the transform's name.
#*****************************************************
    
import maya.cmds as cmds
import re

# create an undo state
cmds.undoInfo(openChunk=True)
# get list of all transforms
nodes = cmds.ls(type='transform')
# get list of all of those transforms' shapes
shapeNodes = cmds.listRelatives(nodes,shapes=True,path=True)
# since some of the transforms might not have shape nodes
# we need to loop through the shape nodes and get their parents'
# names in order to rename them.
for shape in shapeNodes:
    parent=cmds.listRelatives(shape,parent=True,path=True)[0]
    s=r"""%s""" % parent
    try:
        match = re.match('.*?([0-9]+)$', s)
        shapeName = ''
        if len(match.group(1)) > 0:
            shapeName = parent[:-len(match.group(1))] + 'Shape' + match.group(1)
        else:
            shapeName = parent + 'Shape'
        try:
            cmds.rename(shape,shapeName)
        except:
            pass
    except Exception as e:
        pass
    finally:
        cmds.undoInfo(closeChunk=True)