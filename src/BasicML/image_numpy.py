#  Numpy in action
import numpy as np
from matplotlib.image import imread

image = imread(
    "../images/download.jfif")
print(type(image))
print(image)
print(image.size)
print(image.shape)
print(image.ndim)
print(image[:100])
