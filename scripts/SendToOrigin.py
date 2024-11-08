#*****************************************************
# Name: SendToOrigin
# Author: Chris Peterson
# This script will send the selected objects to the
# origin based off of their bounding boxes.
#*****************************************************
import maya.cmds as cmds

selection = cmds.ls(sl=True,tr=True)
for item in selection:
    # centers pivot
    cmds.xform(item, cp=1)
    # moves the object (based on pivot) to the origin
    cmds.move(0,0,0,rpr=True)
    # gets bounding box of the object
    bbnx = cmds.getAttr("%s.bbnx" % item)
    bbny = cmds.getAttr("%s.bbny" % item)
    bbnz = cmds.getAttr("%s.bbnz" % item)
    bbxx = cmds.getAttr("%s.bbxx" % item)
    bbxy = cmds.getAttr("%s.bbxy" % item)
    bbxz = cmds.getAttr("%s.bbxz" % item)
    # Freezes transforms of the object
    cmds.makeIdentity(apply=True,t=1,r=1,s=1,n=0,pn=1)
    # Selects the item
    cmds.select(item,r=True)
    # Sets its y position to half of the bounding box height so it stays above the origin
    cmds.setAttr("%s.ty" % item,((bbxy - bbny)/2))
    # Freezes transforms of the object
    cmds.makeIdentity(apply=True,t=1,r=1,s=1,n=0,pn=1)