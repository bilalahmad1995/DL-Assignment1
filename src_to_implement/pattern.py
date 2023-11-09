import numpy as np
import matplotlib.pyplot as plt

class Checker:
    def __init__(self, resolution, tile_size):
        if resolution % (2 * tile_size) != 0:
            raise ValueError("Resolution must be evenly divisible by 2 times tile size.")
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = None  # Initialize the output as None

    def draw(self):
        # Create an empty black and white checkerboard pattern
        rows = self.resolution
        cols = self.resolution
        checkerboard = np.zeros((rows, cols), dtype=int)
        tile_rows = rows // (2 * self.tile_size)
        tile_cols = cols // (2 * self.tile_size)

        for i in range(tile_rows):
            for j in range(tile_cols):
                if (i + j) % 2 == 0:
                    checkerboard[i * self.tile_size:(i + 1) * self.tile_size,
                                j * self.tile_size:(j + 1) * self.tile_size] = 1

        self.output = checkerboard

    def show(self):
        plt.imshow(self.output, cmap='gray')
        plt.show()


class Circle:
    def __init__(self, resolution, radius, position):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = None  # Initialize the output as None

    def draw(self):
        # Create an empty binary image with a circle
        x, y = np.meshgrid(np.arange(self.resolution), np.arange(self.resolution))
        circle = (x - self.position[0]) ** 2 + (y - self.position[1]) ** 2 <= self.radius ** 2
        self.output = circle.astype(int)

    def show(self):
        plt.imshow(self.output, cmap='gray')
        plt.show()

class Spectrum:
    def __init__(self, resolution):
        self.resolution = resolution
        self.output = None  # Initialize the output as None

    def draw(self):
        # Create an RGB color spectrum
        spectrum = np.zeros((self.resolution, self.resolution, 3), dtype=float)

        for x in range(self.resolution):
            r = x / (self.resolution - 1)  # Red component
            spectrum[:, x, 0] = r

            g = (x / (self.resolution - 1)) % 1  # Green component
            spectrum[:, x, 1] = g

            b = 1 - (x / (self.resolution - 1)) % 1  # Blue component
            spectrum[:, x, 2] = b

        self.output = spectrum

    def show(self):
        plt.imshow(self.output)
        plt.show()
