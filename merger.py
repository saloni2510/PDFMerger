import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdflist):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdflist:
		print(pdf)
		merger.append(pdf)

	merger.write('Merged.pdf')

pdf_combiner(inputs)