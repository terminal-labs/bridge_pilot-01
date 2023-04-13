import os
import site
import tempfile
import configparser
import importlib.util

PACKAGEDIR = os.path.abspath(os.path.dirname(_fw.find_config_file()))
FRAMEWORKDIR = os.path.abspath(os.path.dirname(__file__))
SRCDIR = os.path.abspath(os.path.join(FRAMEWORKDIR, _back))
APPDIR = os.path.abspath(os.path.join(FRAMEWORKDIR, _back))
SETUPFILEDIR = os.path.abspath(os.path.join(APPDIR, _back))
TESTDIR = os.path.abspath(os.path.join(APPDIR, "tests"))
if os.path.isdir(_shm):
    MEMTEMPDIR = _shm
    tempfile.tempdir = MEMTEMPDIR
else:
    MEMTEMPDIR = _blank
SITEPACKAGESPATH = site.getsitepackages()[0]
COVERAGERC_PATH = f"{APPDIR}/.coveragerc"

PROJECT_NAME = NAME
