from problem1 import problem1
import numpy as np

# import Image from PIL
from PIL import Image

# Open the image
img = Image.open("lena.jpg")

# Convert the image to a NumPy array
img_array = np.array(img)

# Normalize pixel values to the range [0, 1]. Don't forget this !!!
normalized_img_array = img_array / 255.0

# Obtain blur and ridge from problem1 and call them on your image

blur,ridge = problem1()
new_img = ridge(normalized_img_array)

# Convert the normalized array back to image. Don't forget this !!!
normalized_img = Image.fromarray((new_img * 255).astype(np.uint8))

# Show or save your images  

normalized_img.save("new_image.jpg")
