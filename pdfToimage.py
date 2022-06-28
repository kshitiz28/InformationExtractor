from numpy import dtype
from pdf2image import convert_from_path
import imageToboxes
from PIL import Image

# pdfs = r"test.pdf"
pages = convert_from_path('test.pdf', 350)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    i = i+1  

imageToboxes.mark_region(image_name)
# print(marked_image)
