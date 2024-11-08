#*****************************************************
# Name: AutoLoadTexturesOn
# Author: Chris Peterson
# This script will enable the autoload of textures in maya
#*****************************************************
import maya.mel

maya.mel.eval('nexOpt -e autoloadTextures true;')
maya.mel.eval('print "AutoLoad textures ENABLED."')