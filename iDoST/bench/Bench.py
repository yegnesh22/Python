import platform

from common import OsHelper
from common import utils

class Bench:
    def __init__(self):
        self.os = platform.system()
        self.helper = OsHelper.OsHelper(self.os).getHelper()

    def ExecCommand(self, cmd):
        return self.helper.ExecuteCommand(cmd)
