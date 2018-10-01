import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

pdf_name= ''

def convert_pdf_to_text_pdfminer(path):
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	codec = 'utf-8'
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
	with open (path, 'rb') as fp:	
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		password = ""
		maxpages = 0
		caching = True
		pagenos=set()
		for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,password=password,caching=caching, check_extractable=True):

			interpreter.process_page(page)

		text = retstr.getvalue()

	device.close()
	retstr.close()
	return text

def save_to_file(software_name, pdf_name=pdf_name):
	pdf_dir = os.path.join(os.getcwd(), 'pdfs')
	path_to_pdf = os.path.join(pdf_dir, pdf_name)
	output_file_name = '{}_{}.txt'.format(software_name, pdf_name)
	output_file = os.path.join('output/', output_file_name)
	with open(output_file, 'w') as f:
		output = convert_pdf_to_text_pdfminer(path_to_pdf)
		f.write(output)
	print('output saved to {}'.format(output_file))

save_to_file('pdfminer')

