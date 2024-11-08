#*****************************************************
# Name: RenameSGToMatName
# Author: Chris Peterson
# Description: Renames shading group nodes to the 
# material name + 'SG' at the end
#*****************************************************

import pymel.core as pm

for mat in pm.ls(materials=True):
    matName = str(mat)
    sgNode = pm.listConnections('%s.outColor' % matName,d=True,s=False)
    print(sgNode)
    try:
        pm.undoInfo(openChunk=True)
        pm.rename(sgNode,matName + 'SG')
    except Exception as e:
        pm.undoInfo(closeChunk=True)
        print(str(e))
    print(pm.listConnections('%s.outColor' % matName,d=True,s=False))
pm.warning('Shading groups renamed.')