import config as config

class doc_docx:

    def __init__(self, filename, sourcefile):
        # Return an object

        self.filename   =   filename
        self.extension  =   'docx'
        self.mimetype   =   'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        self.fullname   =   self.filename + "." + self.extension
        self.ospath = config.filespath() + self.fullname

        from docx import Document
        from docx.shared import Pt

        with open(sourcefile, 'r')  as f:
            data = f.read()

        document = Document()

        style = document.styles['Normal']
        font = style.font
        font.name = 'Courier New'
        font.size = Pt(10)

        p = document.add_paragraph(data)
        p.style = document.styles['Normal']

        document.save(self.ospath)
