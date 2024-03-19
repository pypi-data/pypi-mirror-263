import numpy as np

def change_color_channels(image, red_factor=1, green_factor=1, blue_factor=1):
    image[:, :, 0] *= red_factor
    image[:, :, 1] *= green_factor
    image[:, :, 2] *= blue_factor
    return np.clip(image, 0, 255)

def intensify_color(image, color, factor):
    color_idx = {'red': 0, 'green': 1, 'blue': 2}
    channel = color_idx[color.lower()]
    image[:, :, channel] *= factor
    return np.clip(image, 0, 255)

def grayscale(image):
    return np.dot(image[..., :3], [0.2989, 0.587, 0.114])
