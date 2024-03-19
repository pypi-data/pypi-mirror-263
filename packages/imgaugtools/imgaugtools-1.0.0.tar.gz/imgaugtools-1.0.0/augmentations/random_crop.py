import numpy as np

def random_crop(image, crop_size):
    height, width = image.shape[:2]
    crop_height, crop_width = crop_size
    if height < crop_height or width < crop_width:
        raise ValueError("Crop size must be smaller than image size")
    y = np.random.randint(0, height - crop_height + 1)
    x = np.random.randint(0, width - crop_width + 1)
    return image[y:y+crop_height, x:x+crop_width]
