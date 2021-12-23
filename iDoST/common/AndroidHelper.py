'''
Created on 22-Dec-2021

@author: yegnesh
'''
from common import utils

supportedCommands = {
    'adbShell': runCommand,
    'adbPull': pullFile,
}

class AndroidHelper:
    def __init__(self): 
        print ("Android helper object created")
    
    def setHost(self, HostId):
        self.DeviceSerial = HostId
    
    def runCommand(self, cmd):
        return utils.execCommand("adb -s " + self.DeviceSerial + " " + cmd)

    def pull(self, path):
        return utils.execCommand("adb -s " + self.DeviceSerial + " pull " + path)
    
    def GetBuildInfo(self):
        build_info['product'] = self.runCommand("getprop ro.build.product")
        build_info['desc'] = self.runCommand("adb shell getprop ro.build.description")
        build_info['version incremental'] = self.runCommand("adb shell getprop ro.build.version.incremental")
        build_info['release'] = self.runCommand("adb shell getprop ro.build.version.release")
        build_info['sdk'] = self.runCommand("adb shell getprop ro.build.version.sdk")
        return build_info

    def ExecCommand(self, cmd):
        cmd_exe = cmd.split(':')[0]
        cmd_args = (cmd.split(':')[1:]).join()
        try:
            rt = "op = self.{}(cmd_args)".format(supportedCommands[cmd_exe])
            exec(rt)
        except KeyError:
            print("Exception: Invalid command {}".format(cmd_exe))
            return -1
        return op
    
    