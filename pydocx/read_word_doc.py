
from docx import Document

document = Document('hamlet.docx')

for para in document.paragraphs:
    print(para.text)
