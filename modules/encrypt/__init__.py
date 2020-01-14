import os

filetypes= []
prefix = "enc_"

thispath = os.path.dirname(os.path.realpath(__file__))

for file in os.listdir(thispath):
    if file.startswith(prefix):
        ft = file[4:-3]
        filetypes.append(ft)

#from modules.documents.enc_[blah] import enc_[blah]
