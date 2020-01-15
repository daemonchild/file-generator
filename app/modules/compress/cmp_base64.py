import config as config

class cmp_base64:

    def __init__(self, filename, sourcefile):
        # Return an object
        self.filename   =   filename
        self.extension  =   'b64'
        self.mimetype   =   'application/base64'
        self.fullname   =   self.filename + "." + self.extension
        self.ospath = config.filespath() + self.fullname

        # Generate the file

        import base64

        with open(sourcefile, 'rb') as f:
            data = f.read()
            f.close()

        b64 = base64.encodebytes(data)

        with open(self.ospath, 'wb') as f:
            f.write(b64)
            f.close()
