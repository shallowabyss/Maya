#*****************************************************
# Name: SaveUVToDesktop
# Author: Chris Peterson
# This script will send the selected objects to the
# origin based on their bounding box.
#*****************************************************
import maya.mel
import maya.cmds as cmds

obj_sel = cmds.ls(sl=True)

if len(obj_sel):
    result = cmds.promptDialog(
        title='Save UV to Desktop',
        text='4096',
        message='Image Resolution:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    resol = 0
    if result == 'OK':
        resol = cmds.promptDialog(query=True, text=True)
        resol = int(resol)

    if resol > 0:
        for selected_items in obj_sel:
            cmds.select(selected_items, r=True)
            print(selected_items)
            shapes = cmds.listRelatives(selected_items, shapes=True)
            if shapes:
                try:
                    print('yaya')
                    currentUser = getpass.getuser()
                    objName = selected_items.strip('|')
                    fName = os.path.join('c:\\', 'users', currentUser, 'desktop', objName + '_UV.png')
                    fName = fName.replace('\\', '/')
                    print('exporting ' + str(selected_items))
                    cmds.uvSnapshot(n=fName, o=True, xr=resol, yr=resol, redColor=0, greenColor=0, blueColor=0,
                                    antiAliased=True, fileFormat='png')
                    maya.mel.eval('print "Saved {0} to the desktop."'.format(selected_items))
                except Exception as err:
                    cmds.warning(err)
            else:
                cmds.warning('{0} is not a valid mesh. Skipping it.'.format(selected_items))
    cmds.select(obj_sel, r=True)
else:
    cmds.warning('Please select at least one object before exporting the UVs.')