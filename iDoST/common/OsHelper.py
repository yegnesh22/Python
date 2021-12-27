from common import AndroidHelper
#import LinuxHelper

class OsHelper:
    def __init__(self, os):
        self.os = os

    def getHelper(self):
        if (self.os == 'Android'):
            return AndroidHelper.AndroidHelper()
        '''if (os == 'Linux'):
            return LinuxHelper()'''


        

