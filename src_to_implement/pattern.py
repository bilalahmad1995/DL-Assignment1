import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

class Checker:
    def __init__(self, resolution, tile_size):
        self.resolution = resolution
        self.tile_size = tile_size
        if resolution % (2 * tile_size) != 0:
            raise ValueError("Resolution must be divisible by 2 * tile_size")
        self.output = None

    def draw(self):
        # Create an array of zeros (black tiles)
        self.output = np.zeros((self.resolution, self.resolution))

        # Set white tiles
        for y in range(0, self.resolution, self.tile_size * 2):
            for x in range(self.tile_size, self.resolution, self.tile_size * 2):
                self.output[y:y + self.tile_size, x:x + self.tile_size] = 1  # Set white tile
                self.output[y + self.tile_size:y + 2 * self.tile_size,
                x - self.tile_size:x] = 1  # Set white tile in next row

        # Return a copy of the pattern
        return self.output.copy()

    def show(self):
        if self.output is None:
            raise ValueError("Pattern not generated. Call draw() first.")
        plt.imshow(self.output, cmap='gray')
        plt.title('Checkerboard Pattern')
        plt.show()

class Circle:
    def __init__(self, resolution, radius, position):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = None

    def draw(self):
        x_center, y_center = self.position
        x = np.arange(self.resolution)
        y = np.arange(self.resolution)
        xx, yy = np.meshgrid(x, y)

        circle_equation = (xx - x_center) ** 2 + (yy - y_center) ** 2 <= self.radius ** 2
        self.output = circle_equation.astype(np.bool_)

        return self.output.copy()

    def show(self):
        if self.output is None:
            raise ValueError("Pattern not generated. Call draw() first.")
        plt.imshow(self.output, cmap='gray')
        plt.title('Circle Pattern')
        plt.show()

class Spectrum:
    def __init__(self, resolution):
        self.resolution = resolution
        self.output = None

    def draw(self):
        # Create a grid of coordinates
        x = np.linspace(0, 1, self.resolution)
        y = np.linspace(0, 1, self.resolution)
        xx, yy = np.meshgrid(x, y)

        # Create RGB channels
        red = xx  # Red intensity varies horizontally
        green = yy  # Green intensity varies vertically
        blue = (1 - xx) * (1 - yy)  # Blue intensity varies inversely to red and green

        # Combine channels to form an RGB image
        self.output = np.stack((red, green, blue), axis=-1)

        return self.output.copy()

    def show(self):
        if self.output is None:
            raise ValueError("Pattern not generated. Call draw() first.")
        plt.imshow(self.output)
        plt.title('RGB Spectrum')
        plt.show()
