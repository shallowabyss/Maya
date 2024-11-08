#*****************************************************
# Name: CopyScenePathClipboard
# Author: Chris Peterson
# This script will copy the scene path to the clipboard on Windows
#*****************************************************

import maya.cmds as cmds
import maya.mel
import subprocess
import os

path = cmds.file(q=True, sn=True)
if path != '':
    if os.path.exists(path):
        path = path.replace('/','\\')
        cmd = 'echo ' + path.strip() + '|clip'
        subprocess.check_call(cmd, shell=True)           
        maya.mel.eval('print "File path copied to clipboard."')
    else:
        cmds.warning('The file does not exist locally.')
else:
    cmds.warning('You must be in a saved file to explore to it.')
    
