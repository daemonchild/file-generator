import config as config

extension = 'bat'
mimetype = 'application/x-bat'
description = 'Windows Batch File'


class doc_bat:

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
        f.write("@echo off\r\n")
        f.write("echo *** Test Batch File - " + self.filename + " ***\r\n")
        f.write("echo " + data)
        f.close()

