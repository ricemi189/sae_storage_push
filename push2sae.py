import sys
from push import push
import os

assert len(sys.argv)==2
dirpath=sys.argv[1]
if os.path.isabs(dirpath):
    pdir,dirpath=os.path.split(dirpath)
    os.chdir(pdir)
push(dirpath)
