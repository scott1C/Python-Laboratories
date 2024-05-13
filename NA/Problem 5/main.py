import numpy as np
import math
from PIL import Image
import os

path = os.path.join(os.path.dirname(__file__), "img.jpg")

def scale_image(image, scale_factor):
    height, width, channels = image.shape
    
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)
    
    output = np.zeros((new_height, new_width, channels), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            original_x = min(int(j / scale_factor), width - 1)
            original_y = min(int(i / scale_factor), height - 1)

            output[i, j] = image[original_y, original_x]
    
    return output

image = np.array(Image.open(path))
scaled_image = scale_image(image, 2)

Image.fromarray(scaled_image).save('scaled_image.jpg')
