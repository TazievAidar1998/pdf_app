import PyPDF2

# pl = open('pdf1.pdf', 'rb')
# plread = PyPDF2.PdfFileReader(pl)
# getpage37 = plread.getPage(0)
# print(getpage37)
# text37 = getpage37.extractText()
# # print(text37)



# pdf_filename = 'zadachnick.pdf'
# file = open(pdf_filename, 'rb')
# pdf = PyPDF2.PdfFileReader(file)
#
# for i in range(pdf.numPages):
#     page = pdf.getPage(i)
#     output = PyPDF2.PdfFileWriter()
#
#     output.addPage(page)
#
#     filename = 'auction_pdf_#{i}.pdf'.format(i=i)
#     outputStream = open(filename, 'wb')
#     output.write(outputStream)
#     outputStream.close()


pdf_file_names = ['auction_pdf_#0.pdf',
                  'auction_pdf_#1.pdf',
                  'auction_pdf_#2.pdf',
                  'auction_pdf_#3.pdf',
                  'auction_pdf_#4.pdf',
                  'auction_pdf_#5.pdf',]

output = PyPDF2.PdfFileWriter()
for name in pdf_file_names:
    file = open(name, 'rb')
    pdf = PyPDF2.PdfFileReader(file)

    for i in range(pdf.numPages):
        page = pdf.getPage(i)
        output.addPage(page)


filename = 'auction_pdf_union.pdf'
outputStream = open(filename, 'wb')
output.write(outputStream)
outputStream.close()






