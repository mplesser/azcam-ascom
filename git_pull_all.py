# pull all azcam repos to github

import os
import subprocess

top = os.path.abspath(os.curdir)
commands = {"packages": "git_pull_packages", "environments": "git_pull_environments"}

for root in commands:
    os.chdir(root)
    folder = os.path.abspath(os.curdir)
    print(folder)

    p = subprocess.Popen(commands[root], shell=True, cwd=folder)
    p.wait()
    os.chdir(top)

print()
input("Press Enter to continue...")
