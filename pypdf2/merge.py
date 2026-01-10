
from PyPDF2 import PdfMerger

merger = PdfMerger()


files = [
"ESt_Rother_2022_20250726_133520.jpg",
"ESt_Rother_2022_20250726_133535.jpg",
"ESt_Rother_2022_20250726_133551.jpg",
"ESt_Rother_2022_20250726_133601.jpg",
"ESt_Rother_2022_20250726_133629.jpg",
"ESt_Rother_2022_20250726_133646.jpg",
"ESt_Rother_2022_20250726_133655.jpg",
"ESt_Rother_2022_20250726_133708.jpg",
"ESt_Rother_2022_20250726_133722.jpg",
]
from PIL import Image
import os

# List of your image file paths

# Open the images and convert them to RGB
images = [Image.open(img).convert('RGB') for img in files]

# Save all images into a single PDF
output_pdf_path = "merged_output.pdf"
images[0].save(output_pdf_path, save_all=True, append_images=images[1:])

print(f"PDF created: {output_pdf_path}")