'''
Created on 22-Dec-2021

@author: yegnesh
'''
from common import utils
from common import OsHelper

class Bench:
    def __init__(self):
        # TODO - Add bench specific settings
        self.benchArgs['Category'] = "PerfBench"
        self.benchArgs['Os'] = "Linux"
        self.helper = OsHelper.getHelper(self.benchArgs['Os'])
    
    
    