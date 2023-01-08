import PyPDF4


def PDFRotation(originalFileName, newFileName, rotateAngle):
        pdfReader = PyPDF4.PdfFileReader(originalFileName)
        pdfWriter = PyPDF4.PdfFileWriter()

        for page in range(pdfReader.getNumPages()):
                pageObject = pdfReader.getPage(page)
                pageObject.rotateClockwise(rotateAngle)

                pdfWriter.addPage(pageObject)
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
        pdfMerger.close()
        print("Merger Done!!")


def PDFSplitting(originalFileName, splitPosition):
        start = 0
        end = splitPosition[0]
        for i in range(len(splitPosition)+1):
                pdfReader = PyPDF4.PdfFileReader(originalFileName)
                pdfWriter = PyPDF4.PdfFileWriter()

                for page in range(start, end):
                        pdfWriter.addPage(pdfReader.getPage(page))
                outputpdf = "SplittedFile"+str(i+1)+".pdf"

                newFile = open(outputpdf, "wb")
                pdfWriter.write(newFile)
                newFile.close()

                start = end

                try:
                        end = splitPosition[i+1]
                except IndexError:
                        end = pdfReader.getNumPages()

        print("Splitting Done!!")


def watermarkMaking(originalFileName, outputFileName, watermarkFileName):
        pdfReader = PyPDF4.PdfFileReader(originalFileName)
        watermarkReader = PyPDF4.PdfFileReader(watermarkFileName)
        mergePDF = PyPDF4.PdfFileWriter()

        watermark = watermarkReader.getPage(0)

        for page in range(pdfReader.getNumPages()):
                currentPage = pdfReader.getPage(page)
                currentPage.mergePage(watermark)

                mergePDF.addPage(currentPage)

        newFile = open(outputFileName, "wb")
        mergePDF.write(newFile)
        newFile.close()
        print("Making Waterpark Done!!")


originalFileName = "test.pdf"
newFileName = "Rotated_example.pdf"
rotateAngle = 270
PDFRotation(originalFileName, newFileName, rotateAngle)

pdfs = ["test.pdf", "test1.pdf"]
outputFileName = "Combined_example.pdf"
PDFMerger(pdfs, outputFileName)

originalFileName = "test.pdf"
splitPosition = [2, 5]
PDFSplitting(originalFileName, splitPosition)

originalFileName = "test.pdf"
outputFileName = "Watermark.pdf"
watermarkFileName = "logo.pdf"
watermarkMaking(originalFileName, outputFileName, watermarkFileName)