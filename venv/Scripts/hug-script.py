#!C:\Users\colin.zt\PycharmProjects\ptest\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hug==2.4.1','console_scripts','hug'
__requires__ = 'hug==2.4.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hug==2.4.1', 'console_scripts', 'hug')()
    )
