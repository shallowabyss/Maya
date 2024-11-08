#*****************************************************
# Name: AutoLoadTexturesOff
# Author: Chris Peterson
# This script will disable the autoload of textures in maya
#*****************************************************
import maya.mel

maya.mel.eval('nexOpt -e autoloadTextures false;')
maya.mel.eval('print "AutoLoad textures DISABLED."')