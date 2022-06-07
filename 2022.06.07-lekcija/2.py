import subprocess

cmd='git --version'

rez=subprocess.call(cmd,shell=True)
print(rez)