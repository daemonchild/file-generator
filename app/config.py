import os

# Global Variables and functions

def appport():

    return 9000


def apppath():

    import os
    return (os.path.dirname(os.path.realpath(__file__ )))

def respath():

    return (apppath() + "/resources/")

def filespath():

    fp = apppath() + "/files/"


    if not os.path.exists(fp):
        os.makedirs(fp)

    return (fp)


class mimetypes:

    #mimetypelisturl="https://www.iana.org/assignments/media-types/application.csv"
    #source = "application.csv"

    docx = {'mimetype': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'extension': 'docx'}
    zip = {'mimetype': 'application/zip', 'extension': 'zip'}
    gzip = {'mimetype': 'application/gzip', 'extension': 'gzip'}
    base64 = {'mimetype': 'application/base64', 'extension': 'b64'}

    def __init__(self):
        # Return an object
        self.module   =   'mimetypes'





