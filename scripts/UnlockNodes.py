# *****************************************************
# Name: UnlockNodes
# Author: Chris Peterson
# This script will unlock nodes so that they can be
# deleted. ex: Removing Turtle from the scene.
# *****************************************************

allNodes = cmds.ls()
for node in allNodes:
    cmds.lockNode(node, l=False)
maya.mel.eval('print "Nodes unlocked."')