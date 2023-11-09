import numpy as np
import matplotlib.pyplot as plt
#from generator import ImageGenerator
from pattern import Checker, Circle, Spectrum
import pytest

if __name__ == "__main__":
    # Create a Checker object
    checker_resolution = 400
    checker_tile_size = 40
    checker = Checker(checker_resolution, checker_tile_size)

    # Create a Circle object
    circle_resolution = 400
    circle_radius = 50
    circle_position = (200, 200)
    circle = Circle(circle_resolution, circle_radius, circle_position)

    # Call the methods on the specific object you want
    # For example, to draw and show the Checker pattern:
    checker.draw()
    checker.show()

    # Or to draw and show the Circle pattern:
    circle.draw()
    circle.show()

    spectrum_resolution = 400
    spectrum = Spectrum(spectrum_resolution)
    spectrum.draw()
    spectrum.show()

    #file_path = '/exercise_data'
    #label_path = '/Labels.json'
    #batch_size = 10
    #image_size = (32, 32, 3)  # Adjust image size as needed
    #rotation = True
    #mirroring = True
    #shuffle = True

   #image_generator = ImageGenerator(file_path, label_path, batch_size, image_size, rotation, mirroring, shuffle)

    # Call the show() method to visualize a batch of images
    #'image_generator.show()'