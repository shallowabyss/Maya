#*****************************************************
# Name: RemoveAllNamespaces
# Author: Chris Peterson
# This script will remove all namespaces in the scene.
#*****************************************************

import maya.cmds as cmds

try:
    ns_list = cmds.namespaceInfo( listOnlyNamespaces=True )
    for i in ns_list:
        if i != 'UI' and i != 'shared':
            cmds.namespace( set=':' )
            cmds.namespace(removeNamespace=i, mergeNamespaceWithRoot=True)
    maya.mel.eval('print "Namespaces have been merged with the root"')
except Exception as err:
    cmds.error('print "Couldn\'t remove all namespaces. {0}"'.format(str(err)))
        