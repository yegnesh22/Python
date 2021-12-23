'''
Created on 22-Dec-2021

@author: yegnesh
'''

from common import utils
from common import OsHelper

class Target:
    def __init__(self):
        self.TargetArgs['Os'] = "Android" # This should be read from the config file
        self.TargetArgs['HostID'] = "emulator-5554"
        self.TargetArgs['BuildInfo'] = self.helper.GetBuildInfo()
        self.helper = OsHelper.getHelper(self.TargetArgs['Os'])
        self.helper.setHost(self.TargetArgs['HostID'])
        
    def ExecuteCommand(self, cmd):
        return self.helper.ExecCommand(cmd)
        