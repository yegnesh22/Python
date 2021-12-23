'''
Created on 23-Dec-2021

@author: yegnesh
'''

from common import AndroidHelper
from common import LinuxHelper


class OsHelper {
        def __init__(self):
            OsHelpers["Android"] = AndroidHelper()
            OsHelpers["Linux"] = LinuxHelper()
            
        def getHelper(self, os):
            return OsHelpers[os]
}
