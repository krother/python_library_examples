
# Convert all `.png` images in the current working directory to half their size
from PIL import Image
import os

for filename in os.listdir('.'):
    if filename.endswith('.png'):
        im = Image.open(filename)
        x = im.size[0] // 2
        y = im.size[1] // 2
        small = im.resize((x, y), resample=Image.Resampling.LANCZOS)
        small.save('small_' + filename)
