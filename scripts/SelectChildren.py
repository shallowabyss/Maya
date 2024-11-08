#*****************************************************
# Name: SelectChildren
# Author: Chris Peterson
# This script will add all children for the selected nodes
# to the selection.
#*****************************************************
import maya.cmds as cmds

sel = cmds.ls(sl=True)
for x in sel:
    newSel = cmds.listRelatives(x,allDescendents=True,path=True)
    cmds.select(newSel, add=True)