import os.path
import json
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
from numpy import resize


# In this exercise task you will implement an image generator. Generator objects in python are defined as having a next function.
# This next function returns the next generated object. In our case it returns the input of a neural network each time it gets called.
# This input consists of a batch of images and its corresponding labels.
class ImageGenerator:
    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        self.file_path = file_path
        self.label_path = label_path
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle

        # Load the label dictionary from the JSON file
        with open(label_path, 'r') as label_file:
            self.labels = json.load(label_file)

        # Get a list of image file names from the provided directory
        self.image_files = os.listdir(file_path)

        # Initialize variables for tracking the current batch and epoch
        self.current_batch_index = 0
        self.current_epoch_number = 0


        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
        #TODO: implement constructor

    def next(self):

        # This function creates a batch of images and corresponding labels and returns them.
        # In this context a "batch" of images just means a bunch, say 10 images that are forwarded at once.
        # Note that your amount of total data might not be divisible without remainder with the batch_size.
        # Think about how to handle such cases
        #TODO: implement next method
            # Create empty arrays to store images and labels for the current batch
            batch_images = []
            batch_labels = []

            # Determine the start and end indices for the current batch
            start_index = self.current_batch_index * self.batch_size
            end_index = start_index + self.batch_size

            # Loop through the image files to populate the current batch
            for i in range(start_index, end_index):
                if i < len(self.image_files):
                    # Load an image and its label
                    image_filename = self.image_files[i]
                    image_path = os.path.join(self.file_path, image_filename)
                    label = self.labels[image_filename]

                    # Load the image and resize it to the desired size
                    image = scipy.misc.imread(image_path)
                    image = resize(image, self.image_size, mode='reflect', anti_aliasing=True)

                    # Augmentation: Randomly apply mirroring and rotation
                    if self.mirroring and np.random.rand() > 0.5:
                        image = np.fliplr(image)
                    if self.rotation and np.random.rand() > 0.5:
                        degrees = np.random.randint(1, 180)
                        image = scipy.misc.imrotate(image, degrees)

                    # Append the image and label to the batch
                    batch_images.append(image)
                    batch_labels.append(label)

                else:
                    # If we've reached the end of the image files, wrap around and shuffle if necessary
                    self.current_batch_index = 0
                    self.current_epoch_number += 1
                    if self.shuffle:
                        np.random.shuffle(self.image_files)

            # Increment the batch index for the next iteration
            self.current_batch_index += 1

            # return images, labels
            return np.array(batch_images), np.array(batch_labels)



    def augment(self,img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        #TODO: implement augmentation function

        return img

    def current_epoch(self):
        # return the current epoch number
        return self.current_epoch_number


    def class_name(self, x):
        # This function returns the class name for a specific input
        #TODO: implement class name function
        return self.class_dict[x.label]

    def show(self):
        # In order to verify that the generator creates batches as required, this functions calls next to get a
        # batch of images and labels and visualizes it.
        #TODO: implement show method
        # Generate a batch using the next() method
        images, labels = self.next()

        # Create a grid of images with class names as titles
        num_images = len(images)
        num_rows = int(np.ceil(num_images / 5))
        fig, axes = plt.subplots(num_rows, 5, figsize=(15, 3 * num_rows))

        for i in range(num_images):
            row, col = divmod(i, 5)
            ax = axes[row, col]
            ax.imshow(images[i])
            ax.set_title(self.class_name(labels[i]))
            ax.axis('off')

        plt.show()


