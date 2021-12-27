import readline
import sys
import common

from target import Target
from bench import Bench
from tests import Tests

global tgt
global bench

global commandsFn
global commandsList

def completer(text, state):
    options = [i for i in commandsList if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

def quitProgram():
    sys.exit(0)

def runCommand(cmd):
    try:
        print("Executing {}...".format(commandsFn[cmd]))
    except KeyError:
        print("Invalid Command")
        return

    if (cmd == 'exit'):
        commandsFn[cmd]()
    else:
        commandsFn[cmd].helper.setHost(tgt.host)
        commandsFn[cmd].PreConditions()
        commandsFn[cmd].Execute()
        commandsFn[cmd].Result()

def iDoSTMain():
    global commandsList
    global bench
    global tgt 
    global commandsFn 

    print("Starting...")
    commandsList = ['exit']
    commandsFn = {
        'exit': quitProgram,
    }


    # Parse the xml and fill in the target details and instruments connected
    print("Initialize Target functions..")
    tgt = Target.Target('emulator-5554', 'Android')

    # Parse the xml and fill in the host and ostype 
    print("Initialize Bench functions..")
    bench = Bench.Bench()

    # Initialize Tests
    print("Initialize tests..")
    testList = Tests.Tests(tgt.os).getTestsList()
    print(testList)
    for test in testList:
        commandsList.append(test.testParams['Name'][0])
        commandsFn[test.testParams['Name'][0]] = test

    print("Entering while loop..")
    while 1:
        cmd = input(">>> ")
        runCommand(cmd)



if __name__ == "__main__": 
    iDoSTMain()

