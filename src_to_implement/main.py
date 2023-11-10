import numpy as np
import matplotlib.pyplot as plt
import unittest
from pattern import Checker, Circle, Spectrum
from generator import ImageGenerator
from NumpyTests import TestCheckers, TestCircle, TestGen


if __name__ == "__main__":
    # Create a Checker object
    checker_resolution = 250
    checker_tile_size = 25
    checker = Checker(checker_resolution, checker_tile_size)

    # Call the methods on the specific object you want
    # For example, to draw and show the Checker pattern:
    checker.draw()
    checker.show()


    # Create an instance of Circle
    circle_instance = Circle(resolution=1024, radius=200, position=(512, 256))

    # Draw and show the circle pattern
    circle_instance.draw()
    circle_instance.show()

    # Create an instance of Spectrum
    spectrum_instance = Spectrum(resolution=255)

    # Draw and show the RGB spectrum
    spectrum_instance.draw()
    spectrum_instance.show()

    # The path to the directory containing all images
    image_directory = 'exercise_data'

    # The path to the JSON file containing the labels
    label_file = 'Labels.json'  # Adjust the path if necessary

    # Define the desired batch size and image size
    batch_size = 16  # or any other batch size you want to use
    image_size = [64, 64, 3]  # [height, width, channels]

    # Create an instance of ImageGenerator with desired parameters
    image_generator = ImageGenerator(file_path=image_directory,
                                     label_path=label_file,
                                     batch_size=batch_size,
                                     image_size=image_size,
                                     rotation=True,
                                     mirroring=True,
                                     shuffle=True)

    # Call the show() method to display a batch of images
    image_generator.show()
    unittest.main()








