#!/home/jin/BUFS_S-BitUnited_Worm/j진서/CTFnWARGAMES/pwncollege/crypto/AES/venv/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from rpyc.cli.rpyc_registry import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
