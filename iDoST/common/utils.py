'''
Created on 22-Dec-2021

@author: yegnesh
'''

import subprocess

def execCommand(cmd):
    output = subprocess.check_output(cmd, shell=True)
    return output