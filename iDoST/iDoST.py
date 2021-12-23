'''
Created on 22-Dec-2021

@author: yegnesh
'''
from Bench import Bench
from Target import Target
from Report import Report

def RunTests():
    # Run all the tests


def BenchConfig():
    OBench = Bench()

def TargetConfig():
    OTarget = Target()

def PublishReport():
    OReport.publish()
    

commands = {
    'run_tests': RunTests,
    'bench_config': BenchConfig,
    'target_config': TargetConfig,
    'publish_report': PublishReport,
    'exit': SystemExit,
}

def idostMain():
    

if __init__ == "main":
    idostMain()
    