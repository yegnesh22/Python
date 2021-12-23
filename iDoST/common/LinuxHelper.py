'''
Created on 23-Dec-2021

@author: yegnesh
'''

import sys
from common import utils

class LinuxHelper:
    def __init__(self):
        self.host = None

    def setHost(self, HostId):
        self.host = HostId;
       
    def ExecCommand(self, cmd):
        if (self.host == None)
            # Assuming that the command is for native os
            return utils.execCommand(cmd)