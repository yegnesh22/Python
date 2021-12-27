import xml.etree.ElementTree as ET
import os

from common import OsHelper

class Test:
    def __init__(self, osname, test_params):
        self.helper = OsHelper.OsHelper(osname).getHelper()
        self.testParams = test_params

    def runStage(self, stage):
        print (self.testParams[stage])
        for k in self.testParams[stage]:
            for i in range(0, len(self.testParams[stage][k])):
                tname = self.testParams['Name'][0]
                step = self.testParams[stage][k][i]
                self.helper.ExecuteCommand(step, tname)

    def PreConditions(self):
        self.runStage('PreConditions')

    def Execute(self):
        self.runStage('Execute')

    def Result(self):
        self.runStage('Result')

class Tests:
    def __init__(self, osname):
        self.TestList = self.InitTests(osname)

    def getTestsList(self):
        return self.TestList

    def makeDict(self, root):
        myList = dict()
        for t in root:
            if (len(t) != 0):
                myList[t.tag] = self.makeDict(t)
            else:
                try:
                    myList[t.tag].append(t.text)
                except KeyError:
                    myList[t.tag] = list()
                    myList[t.tag].insert(0, t.text)
        return myList
    
    def InitTests(self, osname):
        fileList = list()
        testList = list()

        # Find all test.xml under the os directory
        for root, dirs, files in os.walk(os.getcwd()):
            for f in files:
                if (osname in os.path.dirname(root)) and (os.path.basename(f) == "test.xml"):
                    fileList.append(os.path.join(root, f))

        # Parse each file and create the test objects
        for f in fileList:
            tree = ET.parse(f)
            root = tree.getroot()
            myList = self.makeDict(root)
            testList.append(Test(osname, myList))

        return testList
