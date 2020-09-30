import subprocess
import sys
from os.path import exists

def get_version():
    if exists('./VERSION'):
        with open('./VERSION', 'r') as v:
            return v.read()
    try:
        return subprocess.check_output(["git", "describe", "--always"]).decode(sys.stdout.encoding).strip()
    except subprocess.CalledProcessError:
        return "ERROR GETTING VERSION"

__version__ = get_version()
VERSION = __version__
