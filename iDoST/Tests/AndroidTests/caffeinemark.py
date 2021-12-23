'''
Created on 23-Dec-2021

@author: yegnesh
'''

from common import utils
import time

class Caffeinemark:
    self.testArgs = {
        'PreConditions': {},
        'Steps': {},
        'WaitForCompletion': {},
    }

    def __init__(self):
        self.resultDir = os.path.join(os.getcwd(), "results")
        
        cmd = "adbShell:logcat -c"
        self.testArgs['PreConditions'].append(cmd)
        
        cmd = "adbShell:mkdir -p /sdcard/iDoST/"
        self.testArgs['PreConditions'].append(cmd)
        
        cmd = "adbShell:rm /sdcard/iDoST/*.png"
        self.testArgs['PreConditions'].append(cmd)
        
        cmd = "adbShell:am start com.primatelabs.geekbench5/com.primatelabs.geekbench.HomeActivity"
        self.testArgs['Steps'].append(cmd)
        cmd = "adbShell:input tap 1070 1640"
        self.testArgs['Steps'].append(cmd)
        
        cmd = "adbShell:dumpsys window window | grep -E 'mCurrentFocus' | grep geekbench.BenchmarkDocument | wc -l"
        self.testArgs['WaitForCompletion'].append(cmd)
        
        cmd = "adbShell:screencap -p /sdcard/iDoST/geekbench.png"
        self.testArgs['ResultActions'].append(cmd)
        
        cmd = "adbPull:/sdcard/iDoST/geekbench.png {}".format(self.resultDir)
        self.testArgs['ResultActions'].append(cmd)
    
    def prepare(self):
        print ("Running pre-conditions")
        
        for step in self.testArgs['PreConditions']:
            tgt.ExecuteCommand(step)
    
    def execute(self):
        for step in self.testArgs['Steps']:
            tgt.ExecuteCommand(step)
        
        for ws in self.testArgs['WaitForCompletion']:
            print("Waiting for completion: {}".format(ws))
            while (tgt.ExecuteCommand(ws) != 1)
                time.sleep(1)
        return
    
    def getResult(self):
        for step in self.testArgs['ResultActions']:
            tgt.ExecuteCommand(step)
        
        
        