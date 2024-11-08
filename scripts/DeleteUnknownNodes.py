#*****************************************************
# Name: DeleteUnknownNodes
# Author: Chris Peterson
# This script will delete unknown nodes in the scene.
#*****************************************************

import maya.cmds as cmds

sel = cmds.ls(type='unknown')
for i in sel:
    confirm = cmds.confirmDialog(title='Confirm',
                                    message='Delete {0}'.format(str(i)), button=['Yes', 'No'], defaultButton='Yes',
                                    cancelButton='No', dismissString='No')
    if confirm == 'Yes':
        try:
            cmds.delete(i)
            print('Deleted: {0}'.format(str(i)))
        except Exception as e:
            cmds.warning('Error deleting {0}. {1}.'.format(str(i), str(e)))