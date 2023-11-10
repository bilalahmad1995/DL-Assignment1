import os
import json
import numpy as np
from skimage.transform import resize, rotate
from skimage.io import imread
import matplotlib.pyplot as plt
import random

class ImageGenerator:
    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        self.file_path = file_path
        self.label_path = label_path
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        self.current_index = 0  # Initialize the current index
        self.current_epoch_num = 0
        self.class_names = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer',
                            5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship', 9: 'truck'}

        # Load the image filenames
        self.image_names = sorted(os.listdir(file_path))

        # Load the labels from the provided json file
        self.labels = self.load_labels(label_path)

        # Create an array of indices to keep track of image order
        self.indices = np.arange(len(self.image_names))

        # Shuffle if the shuffle flag is True
        if shuffle:
            np.random.shuffle(self.indices)

    def load_labels(self, label_path):
        with open(label_path) as f:
            return json.load(f)

    def next(self):
        batch_images = []
        batch_labels = []

        while len(batch_images) < self.batch_size:
            if self.current_index >= len(self.image_names):
                self.current_index = 0
                self.current_epoch_num += 1
                if self.shuffle:
                    np.random.shuffle(self.indices)

            idx = self.indices[self.current_index]
            img_name = self.image_names[idx]
            img_path = os.path.join(self.file_path, img_name)

            # Check the file extension and decide the method to read the file
            if img_path.endswith('.npy'):
                # It's a NumPy binary file (.npy), use np.load
                img = np.load(img_path)
            else:
                # It's an image file, use imread
                img = imread(img_path)

            img = resize(img, self.image_size, anti_aliasing=True)

            if self.mirroring and random.choice([True, False]):
                img = np.fliplr(img)
            if self.rotation:
                img = rotate(img, angle=random.choice([0, 90, 180, 270]), resize=False)

            batch_images.append(img)
            batch_labels.append(self.labels[str(idx)])  # Ensure the key is a string
            self.current_index += 1

        return np.array(batch_images), np.array(batch_labels)

    def current_epoch(self):
        return self.current_epoch_num

    def class_name(self, label):
        return self.class_names[label]

    def show(self):
        images, labels = self.next()
        # Calculate the number of rows and columns to display the images in a grid
        grid_size = int(np.ceil(np.sqrt(len(images))))

        plt.figure(figsize=(15, 15))
        for i in range(len(images)):
            plt.subplot(grid_size, grid_size, i + 1)  # Create subplots in a grid
            plt.imshow(images[i])
            plt.title(self.class_name(labels[i]))
            plt.axis('off')  # Hide the axes
        plt.show()
