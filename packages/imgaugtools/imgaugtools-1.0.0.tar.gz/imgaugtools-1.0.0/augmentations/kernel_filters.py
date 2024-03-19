import numpy as np
from scipy.ndimage import convolve

def sharpen(image):
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    return convolve(image, kernel)

def blur(image):
    kernel = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]]) / 9
    return convolve(image, kernel)

def add_noise(image, noise_level):
    noise = np.random.normal(scale=noise_level, size=image.shape)
    return np.clip(image + noise, 0, 255)

def scale_image(image, scale_factor):
    new_height, new_width = int(image.shape[0] * scale_factor), int(image.shape[1] * scale_factor)
    return np.resize(image, (new_height, new_width, image.shape[2]))
