
import config as config

class cmp_zip:

    def __init__(self, filename, sourcefile):
        # Return an object
        self.filename   =   filename
        self.extension  =   config.mimetypes.zip['extension']
        self.mimetype   =   config.mimetypes.zip['mimetype']
        self.fullname   =   self.filename + "." + self.extension

        # Generate the file
        from zipfile import ZipFile
        from os.path import basename
        archive = config.filespath() + self.fullname

        with ZipFile(archive, 'w') as newzip:
            newzip.write(sourcefile ,basename(sourcefile) )




