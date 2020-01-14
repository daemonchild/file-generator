import os
from importlib import import_module

filetypes= []
prefix = "cmp_"

thispath = os.path.dirname(os.path.realpath(__file__))

for file in os.listdir(thispath):
    if file.startswith(prefix):
        ft = file[4:-3]
        filetypes.append(ft)

from modules.compress.cmp_base64 import cmp_base64
from modules.compress.cmp_gzip import cmp_gzip
from modules.compress.cmp_zip import cmp_zip
from modules.compress.cmp_tar import cmp_tar
from modules.compress.cmp_tgz import cmp_tgz

