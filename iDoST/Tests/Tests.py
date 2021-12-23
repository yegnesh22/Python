'''
Created on 22-Dec-2021

@author: yegnesh
'''

import Tests.AndroidTests

class Tests:
    def __init__(self, tgt):
        self.results = {}
        self.tests = self.GenerateTestList(tgt)
        
    def runTests(self):
        for test in self.tests:
            test.prepare()
            test.execute()
            self.results.append(test.getResult())
    
    def runTest(self, test):
        test.prepare()
        test.execute()
        self.results.append(test.getResult())
    
    def getResults(self):
        return self.results
    
    def clearResults(self):
        self.results = {}
    
    def GenerateTestList(self, tgt, bench):
        # Parse the test objects and look for the applicability
    
