
import config as config

class doc_csv:

    def __init__(self, filename, sourcefile):
        # Return an object
        self.filename   =   filename
        self.extension  =   'csv'
        self.mimetype   =   'text/x-csv'
        self.fullname   =   self.filename + "." + self.extension
        self.ospath     = config.filespath() + self.fullname

        import csv

        csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

        maxrows = 10
        maxcols = 10

        data = []
        row = []
        for x in range(0,maxcols):
            for y in range (0,maxrows):
                row.append (y*x)
            data.append(row)

        with open(self.ospath, 'w') as f:
            writer = csv.writer(f, dialect='myDialect')
            for row in data:
                writer.writerow(row)
            f.close()