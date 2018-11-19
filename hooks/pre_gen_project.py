import os
import shutil
import subprocess


# Globals
TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "
DEBUG_VALUE = "debug"


def clone_git_hooks():
    print(INFO + "Cloning git hooks repo" + TERMINATOR)

    repo = "https://github.com/TangentSolutions/Git-Hooks"
    process = subprocess.Popen(['git', 'clone', repo], stdout=subprocess.PIPE)
    process.wait()

    return process.stdout.read()


def main():
    clone_git_hooks()

    print(SUCCESS + "Pre gen hook complete" + TERMINATOR)


if __name__ == "__main__":
    main()
