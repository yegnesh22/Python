from common import OsHelper

class Target:
    def __init__(self, host, os):
        self.host =  host
        self.os = os
        self.helper = OsHelper.OsHelper(os).getHelper()

    def ExecuteCommand(self, cmd):
        return self.helper.ExecuteCommand(cmd)
    

