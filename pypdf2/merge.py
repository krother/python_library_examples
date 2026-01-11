
import os
from PyPDF2 import PdfMerger
from pathlib import Path

input_path = Path("input")

merger = PdfMerger()

for fn in os.listdir(input_path):
    if fn.endswith('.pdf'):
      merger.append(open(input_path / fn, "rb"))

output = open("result.pdf", "wb")
merger.write(output)
