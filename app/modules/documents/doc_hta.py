import config as config

extension = 'hta'
mimetype = 'application/hta'
description = 'Compiled HTML Application'


class doc_hta:

    def __init__(self, filename, sourcefile):
        # Return an object

        self.filename   =   filename
        self.extension  =   extension
        self.mimetype   =   mimetype
        self.fullname   =   self.filename + "." + self.extension
        self.ospath     =   config.filespath() + self.fullname

        with open(sourcefile, 'r')  as src:
            data = src.read()

        docoutput = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Latin Lessons</title>
 
    <HTA:APPLICATION
        APPLICATIONNAME = "Latin Lessons"
    />
</head>
 
<body>
    <h1>Latin Lessons</h1>
    <p>""" + data + """</p>
</body>
 
</html>
"""
        f = open(self.ospath, "w")
        f.write(docoutput + "\r\n")
        f.close()

