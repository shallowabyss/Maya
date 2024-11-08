#*****************************************************
# Name: ReloadAllTextures
# Author: Chris Peterson
# This script will reload all file node files
# (e.g. textures)
#*****************************************************
import maya.cmds as cmds

files = cmds.ls(type='file')
for f in files:
    fileName = cmds.getAttr('{0}.fileTextureName'.format(f))
    cmds.setAttr('{0}.fileTextureName'.format(f), fileName, type='string')