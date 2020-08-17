import config as config

extension = 'py'
mimetype = 'application/x-python'
description = 'Python Script'

class doc_py:

    def __init__(self, filename, sourcefile):
        # Return an object

        self.filename   =   filename
        self.extension  =   extension
        self.mimetype   =   mimetype
        self.fullname   =   self.filename + "." + self.extension
        self.ospath = config.filespath() + self.fullname

        with open(sourcefile, 'r')  as src:
            data = src.read()

        f = open(self.ospath, "w")
        f.write("import os\r\n")
        f.write("print ('*** Test Python File - " + self.filename + " ***'\n")
        f.write("print ('" + data + "')")
        f.close()

