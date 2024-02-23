from PIL import Image
import numpy as np


def generate_pixelmap(image_path):
    # Loading image
    image = Image.open(image_path)

    # Convert the image to grayscale
    gray_image = image.convert("L")

    # Set a threshold value (adjust as needed)
    threshold = 128

    # Apply the threshold to create a binary image
    binary_image = gray_image.point(lambda p: p > threshold and 1)

    # Convert the image to a NumPy array
    pixel_array = np.array(binary_image).tolist()
    return pixel_array

