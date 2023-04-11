import PyPDF2

merger= PyPDF2.PdfMerger()
pdfFiles=["sample.pdf","dummy.pdf"]
for filename in pdfFiles:

    pdfFile=open(filename, 'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()

merger.write('merged.pdf')