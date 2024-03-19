from setuptools import setup, find_packages
 
setup(
    name='imgaugtools',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # List of dependencies
        "numpy>=1.0",
        "opencv-python>=4.5.1",
    ],
    author='Abhinav Chaturvedi',
    description='easy to use image augmentation tool',
    Long_description='''
    imgaugtool  is a Python package for image augmentation. It provides a collection of tools and utilities for augmenting images and corresponding annotations, helping users enhance their image datasets for machine learning and computer vision tasks.

    Key Features:

    Apply a variety of geometric transformations such as rotation.
    Perform color space transformations including changing RGB color channels and converting to grayscale.
    Apply kernel filters such as sharpening, blurring, and noise addition.
    Support for handling annotations files and transforming coordinates accordingly.
    Simple and easy-to-use tool for applying augmentations to images and annotations.
'''
)