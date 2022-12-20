
import os
import PyPDF2
merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
merger.write('Newfolder/combined.pdf')
merger.close()
    

    
