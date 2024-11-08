#*****************************************************
# Name: ChangeOutlinerColor
# Author: Chris Peterson
# Description: This tool will change the selected 
# objects in the outliner a specified color
#*****************************************************


import maya.cmds as cmds
import maya.mel
from PySide2 import QtWidgets



x = cmds.ls(sl=True)

if len(x) > 0:
    color = QtWidgets.QColorDialog.getColor()
    if color.isValid():
        red_val = color.red() / 255
        green_val = color.green() / 255
        blue_val = color.blue() / 255

        for i in x:
            cmds.setAttr(i + ".useOutlinerColor", True)
            cmds.setAttr(i + ".outlinerColor", red_val, green_val, blue_val)
            maya.mel.eval('AEdagNodeCommonRefreshOutliners();')
