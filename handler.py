import subprocess
import sys
import os

devnull = open(os.devnull, 'w')

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf

def morse(input_string):
    with open("/root/dos/INPUT.STR", "w") as fp:
        fp.write("\"%s\"\n" % input_string)

    subprocess.call([
        "dosbox", "./PRINT.EXE", "-c", "C:\\QBASIC.EXE /run C:\\MORSE.BAS > C:\\LOG.TXT", "-exit", "> /dev/null"
    ], cwd="/root/dos", stdout=devnull, stderr=devnull)

    output = "???"

    try:
        with open("/root/dos/LOG.TXT", "r") as fp:
            output = fp.read().strip()
    except e:
        pass

    return output

if(__name__ == "__main__"):
    st = get_stdin()
    print(morse(st))
