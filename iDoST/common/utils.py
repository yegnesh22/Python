import subprocess

def ExecCommand(cmd):
    code = 0
    try:
        op = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as cmdExcept:
        print("error code:{} exception:{}".format(cmdExcept.returncode, cmdExcept.output))
        return cmdExcept.returncode, cmdExcept.output
    return code, op

