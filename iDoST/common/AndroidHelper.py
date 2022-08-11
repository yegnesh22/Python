import os
import time
import subprocess
from common import utils

class AndroidHelper:

    def __init__(self):
        self.SerialNum = None
        self.fnList = dict()
        self.fnList = {
                'Install': self.Install,
                'Shell': self.Shell,
                'Tap': self.Tap,
                'Module': self.ExecModule,
                'ScreenCap': self.ScreenCap,
                'Pull': self.Pull,
                'Uninstall': self.UnInstall,
        }

    def runCmd(self, cmd):
        code, output = utils.ExecCommand(cmd)
        if (code != 0):
            print(cmd, code)
            return "fail"
        else:
            return output

    def setHost(self, host):
        self.SerialNum = host

    def Install(self, apk):
        apkpath = os.path.join(os.getcwd(),"Downloads",apk)
        output = self.runCmd('adb -s {} install {}'.format(self.SerialNum, apkpath))
        if (output != "Success"):
            return "fail"
        return "pass"

    def UnInstall(self, comp):
        output = self.runCmd('adb -s {} uninstall {}'.format(self.SerialNum, comp))
        if (output != "Success"):
            return "fail"
        return "pass"

    def Pull(self, f):
        output = self.runCmd('adb -s {} pull {}'.format(self.SerialNum, f))
        if (output == "fail"):
            return "fail"
        return "pass"

        
    def Shell(self, cmd):
        output = self.runCmd('adb -s {} shell {}'.format(self.SerialNum, cmd))
        if (output == "fail"):
            return "fail"
        return output

    def Tap(self, cmd):
        x = cmd.split()[0]
        y = cmd.split()[1]
        op = self.Shell("input tap {} {}".format(x, y))
        if (op == "fail"):
            return "fail"
        return "pass"

    def ExecModule(self, mod):
        output=""
        mdelim = "."
        mname = "".join(mod.split(mdelim)[0:-1]) 
        mpath = "import tests.Android." + self.__cur__ + mdelim + mname + " as " + mname
        exec(mpath)
        output = eval(mod + "()")
        return output

    def ScreenCap(self, cmd):
        # wait until the result screen is displayed or test timesout
        if (cmd != None):
            timeout = 300
            screen_found = 0
            while ((screen_found < 1) and (timeout > 0)):
                screen_found = int(self.Shell("\"dumpsys window windows | grep mCurrentFocus | grep {} | wc -l\"".format(cmd)))
                time.sleep(1)
                timeout = timeout - 1
            if ((timeout == 0) and (screen_found == 0)):
                print ("Result screen timedout")
                return "fail"

        lpath = os.path.join(os.getcwd(), "results", (self.__cur__ +  ".png"))
        op = self.Shell("screencap -p /sdcard/Pictures/{}.png".format(self.__cur__))
        if (op == "fail"):
            return "fail"
        op = self.Pull("/sdcard/Pictures/{}.png {}".format(self.__cur__, lpath))
        if (op == "fail"):
            return "fail"
        return "pass"
    
    def ExecuteCommand(self, cmd, testName):
        print("{}. Running {}".format(testName, cmd))
        self.__cur__ = testName
        try:
            cmd1 = cmd.split(':')[0]
            cmd2 = "".join(cmd.split(':')[1:])
        except:
            cmd1 = cmd
            cmd2 = None
        print (cmd1, cmd2)
        try:
            op = self.fnList[cmd1](cmd2)
            return op
        except KeyError:
            print ("Unsupported command: {}".format(cmd1))
            return "fail"
