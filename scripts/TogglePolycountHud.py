#*****************************************************
# Name: TogglePolycountHud
# Author: Chris Peterson
# This script will toggle the polycount HUD and make it yellow
#*****************************************************

import maya.mel

maya.mel.eval('setPolyCountVisibility(!`optionVar -q polyCountVisibility`);')
cmds.displayColor('headsUpDisplayLabels', 17, dormant=True)
maya.mel.eval('print "HUD toggled."')