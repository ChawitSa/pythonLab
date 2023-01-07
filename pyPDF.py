import PyPDF4

def PDFRotation(originalFileName, newFileName, rotateAngle):
        pdfReader = PyPDF4.PdfFileReader(originalFileName)
        pdfWriter = PyPDF4.PdfFileWriter()

        for page in range(pdfReader.getNumPages()):
                pageObject = pdfReader.getPage(page)
                pageObject.rotateClockwise(rotateAngle)

                pdfwriter.addPage(pageObject)
        newFile = open(newFileName, "wb")
        pdfWriter.write(newFile)
        newFile.close()
        print("Rotation Done!!")

def PDFMerger(pdfs, outputFileName):
        pdfMerger = PyPDF4.PdfFileMerger()
        for pdf in pdfs:
                pdfMerger.append(pdf)
        newFile = open(outputFileName, "wb")
        pdfMerger.write(newFile)
        newFile.clone()
        print("Merger Done!!")

originalFileName = "Test.pdf"
newFileName = "Rotated_example.pdf"
rotateAngle = 270
PDFRotation(originalFileName, newFileName, rotateAngle)

pdfs = ["Test1.pdf", "Test2.pdf"]
outputFileName = "Combined_example.pdf"
PDFMerger(pdfs, outputFileName)