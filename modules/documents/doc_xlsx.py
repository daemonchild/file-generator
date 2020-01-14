import config as config

class doc_xlsx:

    def __init__(self, filename, sourcefile):
        # Return an object

        self.filename   =   filename
        self.extension  =   'xlsx'
        self.mimetype   =   'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        self.fullname   =   self.filename + "." + self.extension
        self.ospath     = config.filespath() + self.fullname

        # Generate the file

        import xlsxwriter

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(self.ospath)
        worksheet = workbook.add_worksheet()

        maxrows = 100
        maxcols = 100

        for x in range(0,maxcols):
            for y in range (0,maxrows):
                worksheet.write(x,y, x*y)

        workbook.close()
