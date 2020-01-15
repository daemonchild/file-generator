import config as config

class ft_blank:

    def __init__(self, filename, sourcefile):
        # Return an object
        self.filename   =   filename
        self.extension  =   config.mimetypes.zip['extension']
        self.mimetype   =   config.mimetypes.zip['mimetype']
        self.fullname   =   self.filename + "." + self.extension
        self.ospath     = config.filespath() + self.fullname

        # Generate the file
