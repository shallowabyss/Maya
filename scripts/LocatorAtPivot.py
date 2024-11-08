#*****************************************************
# Name: LocatorAtPivot
# Author: Chris Peterson
# This script will add a locator at the pivot of the
# selected objects.
#*****************************************************
import maya.cmds as cmds

sel = cmds.ls(sl=True)
for item in sel:
    wpos = cmds.xform(item,q=1,ws=1,rp=1)
    loc = cmds.spaceLocator()[0]
    cmds.parent(loc,item)
    cmds.setAttr(loc + ".translateX", wpos[0])
    cmds.setAttr(loc + ".translateY", wpos[1])
    cmds.setAttr(loc + ".translateZ", wpos[2])
    cmds.setAttr(loc + ".rotateX", 0)
    cmds.setAttr(loc + ".rotateY", 0)
    cmds.setAttr(loc + ".rotateZ", 0)
    cmds.setAttr(loc + ".scaleX", 1)
    cmds.setAttr(loc + ".scaleY", 1)
    cmds.setAttr(loc + ".scaleZ", 1)
    cmds.parent(loc,world=True)