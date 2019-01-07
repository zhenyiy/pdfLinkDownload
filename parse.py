import PyPDF2

PDFFile = open('/Users/zhenyi/Downloads/pdf_files/submit_form_new_4.pdf','rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

links = []

for page in range(pages):

    pageSliced = PDF.getPage(page)
    pageObject = pageSliced.getObject()

    if pageObject.has_key(key):
        ann = pageObject[key]
        for a in ann:
            u = a.getObject()
            if u[ank].has_key(uri):
                links.append(u[ank][uri])

print(links)
