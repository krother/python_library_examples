
from PyPDF2 import PdfMerger
from PIL import Image


files = [
    "image1.jpg,
    "image2.jpg,
    "image3.jpg,
]
output_pdf = "merged_output.pdf"

merger = PdfMerger()

images = [Image.open(img).convert('RGB') for img in files]

images[0].save(output_pdf, save_all=True, append_images=images)
