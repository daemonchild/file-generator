import os

filetypes= []
prefix = "doc_"

thispath = os.path.dirname(os.path.realpath(__file__))

for file in os.listdir(thispath):
    if file.startswith(prefix):
        ft = file[4:-3]
        filetypes.append(ft)

from modules.documents.doc_docx import doc_docx
from modules.documents.doc_xlsx import doc_xlsx
from modules.documents.doc_csv import doc_csv
