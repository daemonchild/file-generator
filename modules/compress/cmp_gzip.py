import config as config

class cmp_gzip:

    def __init__(self, filename, sourcefile):
        # Return an object
        self.filename   =   filename
        self.extension  =   'gzip'
        self.mimetype   =   'application/gzip'
        self.fullname   =   self.filename + "." + self.extension
        self.ospath     = config.filespath() + self.fullname

        # Generate the file

        import gzip
        import shutil

        with open(sourcefile, 'rb') as f_in:
            with gzip.open(self.ospath, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)