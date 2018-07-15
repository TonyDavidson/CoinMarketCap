import subprocess

from subprocess import check_output
text = '"Hello world"'
say = check_output('espeak '+text, shell=True)

subprocess.call('espeak '+text, shell=True)
