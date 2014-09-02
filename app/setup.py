"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Otto.py']
#DATA_FILES = ['Otto.xib']
#DATA_FILES = ['Otto.nib']
DATA_FILES = []
INCLUDES = ['json',  # this doesn't cause the json module to be copied, so i'm using simplejson instead
            'chardet', 'mutagen', 'pymongo', 'bson', 'StringIO',
            'PIL', 'PIL.Image', 'getpass', 'hashlib', 'unicodedata']
#OPTIONS = {'argv_emulation': True}
#OPTIONS = { 'iconfile': '../static/images/ottoicon.icns', 'packages': '../lib/python2.7' }
#OPTIONS = { 'iconfile': '../static/images/ottoicon.icns', 'includes': INCLUDES, 'plist': {'LSUIElement': True} }
OPTIONS = { 'iconfile': '../static/images/ottoicon.icns', 'includes': INCLUDES, 'plist': 'Info.plist' }

# might want to consider using --extra-scripts for loader.py (and maybe a reset):
# https://bitbucket.org/ronaldoussoren/py2app/issue/125/mechanism-to-run-arbitrary-scripts-using

# some hints on code signing:
# https://bitbucket.org/ronaldoussoren/py2app/issue/86/py2app-should-support-sandboxing

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
