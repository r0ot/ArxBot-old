from py2exe.build_exe import py2exe
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
sys.path.append("C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\redist\\x86\\Microsoft.VC90.CRT")

setup(
    options = {'py2exe': {'bundle_files': 1}},
    windows = [{'script': "Arx.py"}],
    zipfile = None,
    console=[{"script": "Arx.py"}]
)