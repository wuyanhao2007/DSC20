"""
DSC 20 Project Winter 2026
Name(s): Yanhao Wu
PID(s):  A19061338
Sources: None
"""

import numpy as np
import os
from PIL import Image
import copy

NUM_CHANNELS = 3


# --------------------------------------------------------------------------- #

# YOU SHOULD NOT MODIFY THESE TWO METHODS

def img_read_helper(path):
    """
    Creates an RGBImage object from the given image file
    """
    # Open the image in RGB
    img = Image.open(path).convert("RGB")
    # Convert to numpy array and then to a list
    matrix = np.array(img).tolist()
    # Use student's code to create an RGBImage object
    return RGBImage(matrix)


def img_save_helper(path, image):
    """
    Saves the given RGBImage instance to the given path
    """
    # Convert list to numpy array
    img_array = np.array(image.get_pixels())
    # Convert numpy array to PIL Image object
    img = Image.fromarray(img_array.astype(np.uint8))
    # Save the image object to path
    img.save(path)


# --------------------------------------------------------------------------- #

# Part 1: RGB Image #
class RGBImage:
    """
    Represents an image in RGB format
    """

    def __init__(self, pixels):
        """
        Initializes a new RGBImage object

        # Test with non-rectangular list
        >>> pixels = [
        ...              [[255, 255, 255], [255, 255, 255]],
        ...              [[255, 255, 255]]
        ...          ]
        >>> RGBImage(pixels)
        Traceback (most recent call last):
        ...
        TypeError

        # Test instance variables
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.pixels
        [[[255, 255, 255], [0, 0, 0]]]
        >>> img.num_rows
        1
        >>> img.num_cols
        2
        """
        # YOUR CODE GOES HERE #
        # Raise exceptions here
        if not isinstance(pixels, list):
            raise TypeError
        if len(pixels) < 1:
            raise TypeError
        if not (isinstance(pixels[0], list) and len(pixels[0]) >= 1):
            raise TypeError
        if len(set([len(row) for row in pixels])) != 1:
            raise TypeError
        if not all([isinstance(col, list)
                    for row in pixels for col in row]):
            raise TypeError
        if not all([len(col) == 3 for row in pixels for col in row]):
            raise TypeError
        if not all([(isinstance(rgb, int) and (0 <= rgb <= 255))
                    for row in pixels for col in row for rgb in col]):
            raise ValueError
        self.pixels = pixels
        self.num_rows = len(pixels)
        self.num_cols = len(pixels[0])


    def size(self):
        """
        Returns the size of the image in (rows, cols) format

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.size()
        (1, 2)
        """
        return self.num_rows, self.num_cols

    def get_pixels(self):
        """
        Returns a copy of the image pixel array

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_pixels = img.get_pixels()

        # Check if this is a deep copy
        >>> img_pixels                               # Check the values
        [[[255, 255, 255], [0, 0, 0]]]
        >>> id(pixels) != id(img_pixels)             # Check outer list
        True
        >>> id(pixels[0]) != id(img_pixels[0])       # Check row
        True
        >>> id(pixels[0][0]) != id(img_pixels[0][0]) # Check pixel
        True
        """
        return copy.deepcopy(self.pixels)

    def copy(self):
        """
        Returns a copy of this RGBImage object

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_copy = img.copy()

        # Check that this is a new instance
        >>> id(img_copy) != id(img)
        True
        """
        pixels = self.get_pixels()
        return RGBImage(pixels)


    def get_pixel(self, row, col):
        """
        Returns the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid index
        >>> img.get_pixel(1, 0)
        Traceback (most recent call last):
        ...
        ValueError

        # Run and check the returned value
        >>> img.get_pixel(0, 0)
        (255, 255, 255)
        """
        if not (isinstance(row, int) and isinstance(col, int)):
            raise TypeError
        if self.num_rows - 1 < row or self.num_cols - 1 < col:
            raise ValueError
        if row < 0 or col < 0:
            raise ValueError
        return tuple(self.pixels[row][col])

    def set_pixel(self, row, col, new_color):
        """
        Sets the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid new_color tuple
        >>> img.set_pixel(0, 0, (256, 0, 0))
        Traceback (most recent call last):
        ...
        ValueError

        # Check that the R/G/B value with negative is unchanged
        >>> img.set_pixel(0, 0, (-1, 0, 0))
        >>> img.pixels
        [[[255, 0, 0], [0, 0, 0]]]
        """
        if not (isinstance(row, int) and isinstance(col, int)):
            raise TypeError
        if self.num_rows - 1 < row or self.num_cols - 1 < col:
            raise ValueError
        if row < 0 or col < 0:
            raise ValueError
        if not (isinstance(new_color, tuple) and len(new_color)
                == 3 and all([isinstance(i, int)
                              for i in new_color])):
            raise TypeError
        if not all(isinstance(i, int) for i in new_color):
            raise TypeError
        if not all(i <= 255 for i in new_color):
            raise ValueError
        for i in range(3):
            if new_color[i] >= 0:
                self.pixels[row][col][i] = new_color[i]


# Part 2: Image Processing Template Methods #
class ImageProcessingTemplate:
    """
    Contains assorted image processing methods
    Intended to be used as a parent class
    """

    def __init__(self):
        """
        Creates a new ImageProcessingTemplate object

        # Check that the cost was assigned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost
        0
        """
        self.cost = 0

    def get_cost(self):
        """
        Returns the current total incurred cost

        # Check that the cost value is returned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost = 50 # Manually modify cost
        >>> img_proc.get_cost()
        50
        """
        return self.cost

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check if this is returning a new RGBImage instance
        >>> img_proc = ImageProcessingTemplate()
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_negate = img_proc.negate(img)
        >>> id(img) != id(img_negate) # Check for new RGBImage instance
        True

        # The following is a description of how this test works
        # 1 Create a processor
        # 2/3 Read in the input and expected output
        # 4 Modify the input
        # 5 Compare the modified and expected
        # 6 Write the output to file
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()                            # 1
        >>> img = img_read_helper('img/test_image_32x32.png')                 # 2
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')  # 3
        >>> img_negate = img_proc.negate(img)                               # 4
        >>> img_negate.pixels == img_exp.pixels # Check negate output       # 5
        True
        >>> img_save_helper('img/out/test_image_32x32_negate.png', img_negate)# 6
        """
        pixels = [[[255 - rgb for rgb in col] for col in row] for
                  row in image.pixels]
        return RGBImage(pixels)

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_gray.png')
        >>> img_gray = img_proc.grayscale(img)
        >>> img_gray.pixels == img_exp.pixels # Check grayscale output
        True
        >>> img_save_helper('img/out/test_image_32x32_gray.png', img_gray)
        """
        pixels = [[[(col[0] + col[1] + col[2]) //
                    3, (col[0] + col[1] + col[2]) //
                    3, (col[0] + col[1] + col[2]) // 3]
                   for col in row] for row in image.pixels]
        return RGBImage(pixels)

    def rotate_180(self, image):
        """
        Returns a rotated version of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_rotate.png')
        >>> img_rotate = img_proc.rotate_180(img)
        >>> img_rotate.pixels == img_exp.pixels # Check rotate_180 output
        True
        >>> img_save_helper('img/out/test_image_32x32_rotate.png', img_rotate)
        """
        row_rotate = image.pixels[::-1]
        col_rotate = [row[::-1] for row in row_rotate]
        return RGBImage(col_rotate)

    def get_average_brightness(self, image):
        """
        Returns the average brightness for the given image

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.get_average_brightness(img)
        86
        """
        pixels = [(col[0] + col[1] + col[2]) // 3 for row in image.pixels for col in row]
        all_avg = sum(pixels) // len(pixels)
        return all_avg


    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_adjusted.png')
        >>> img_adjust = img_proc.adjust_brightness(img, 1.2)
        >>> img_adjust.pixels == img_exp.pixels # Check adjust_brightness
        True
        >>> img_save_helper('img/out/test_image_32x32_adjusted.png', img_adjust)
        """
        pixels = []
        for row in image.pixels:
            new_row = []
            for col in row:
                new_pixel = []
                for rgb in col:
                    val = int(rgb * intensity)
                    if val < 0:
                        val = 0
                    elif val > 255:
                        val = 255
                    new_pixel.append(val)
                new_row.append(new_pixel)
            pixels.append(new_row)
        return RGBImage(pixels)


# Part 3: Standard Image Processing Methods #
class StandardImageProcessing(ImageProcessingTemplate):
    """
    Represents a standard tier of an image processor
    """

    def __init__(self):
        """
        Creates a new StandardImageProcessing object

        # Check that the cost was assigned
        >>> img_proc = StandardImageProcessing()
        >>> img_proc.cost
        0
        """
        super().__init__()
        self.cost = 0
        self.coupon = 0

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check the expected cost
        >>> img_proc = StandardImageProcessing()
        >>> img_in = img_read_helper('img/square_32x32.png')
        >>> negated = img_proc.negate(img_in)
        >>> img_proc.get_cost()
        5

        # Check that negate works the same as in the parent class
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')
        >>> img_negate = img_proc.negate(img)
        >>> img_negate.pixels == img_exp.pixels # Check negate output
        True
        """
        if self.coupon > 0:
            self.coupon -= 1
            return super().negate(image)

        else:
            self.cost += 5
            return super().negate(image)


    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        """
        if self.coupon > 0:
            self.coupon -= 1
            return super().grayscale(image)

        else:
            self.cost += 6
            return super().grayscale(image)


    def rotate_180(self, image):
        """
        Returns a rotated version of the given image
        """
        if self.coupon > 0:
            self.coupon -= 1
            return super().rotate_180(image)

        else:
            self.cost += 10
            return super().rotate_180(image)


    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level
        """
        if self.coupon > 0:
            self.coupon -= 1
            return super().adjust_brightness(image, intensity)
        else:
            self.cost += 1
            return super().adjust_brightness(image, intensity)


    def redeem_coupon(self, amount):
        """
        Makes the given number of methods calls free

        # Check that the cost does not change for a call to negate
        # when a coupon is redeemed
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.redeem_coupon(1)
        >>> img = img_proc.rotate_180(img)
        >>> img_proc.get_cost()
        0
        """
        if not isinstance(amount, int):
            raise TypeError
        if amount <= 0:
            raise ValueError
        self.coupon += amount


# Part 4: Premium Image Processing Methods #
class PremiumImageProcessing(ImageProcessingTemplate):
    """
    Represents a paid tier of an image processor
    """

    def __init__(self):
        """
        Creates a new PremiumImageProcessing object

        # Check the expected cost
        >>> img_proc = PremiumImageProcessing()
        >>> img_proc.get_cost()
        50
        """
        super().__init__()
        self.cost = 50

    def pixelate(self, image, block_dim):
        """
        Returns a pixelated version of the image, where block_dim is the size of 
        the square blocks.

        >>> img_proc = PremiumImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_pixelate = img_proc.pixelate(img, 4)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_pixelate.png')
        >>> img_exp.pixels == img_pixelate.pixels # Check pixelate output
        True
        >>> img_save_helper('img/out/test_image_32x32_pixelate.png', img_pixelate)
        """
        result_pixels = image.get_pixels()
        height = len(result_pixels)
        width = len(result_pixels[0])
        for i in range(0, height, block_dim):
            for j in range(0, width, block_dim):
                r_sum, g_sum, b_sum = 0, 0, 0
                count = 0
                for q in range(block_dim):
                    for p in range(block_dim):
                        if i + q < height and j + p < width:
                            r, g, b = result_pixels[i + q][j + p]
                            r_sum += r
                            g_sum += g
                            b_sum += b
                            count += 1
                r_avg = r_sum // count
                g_avg = g_sum // count
                b_avg = b_sum // count
                for q in range(block_dim):
                    for p in range(block_dim):
                        if i + q < height and j + p < width:
                            result_pixels[i + q][j + p] = [r_avg, g_avg, b_avg]
        return RGBImage(result_pixels)

    def edge_highlight(self, image):
        """
        Returns a new image with the edges highlighted

        >>> img_proc = PremiumImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_edge = img_proc.edge_highlight(img)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_edge.png')
        >>> img_exp.pixels == img_edge.pixels # Check edge_highlight output
        True
        >>> img_save_helper('img/out/test_image_32x32_edge.png', img_edge)
        """
        result = image.get_pixels()
        result = [[sum(pixel) // 3 for pixel in row] for row in result]
        height = len(result)
        width = len(result[0])
        new_result = [[0] * width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                total = 0
                for q in range(-1, 2):
                    for p in range(-1, 2):
                        ni, nj = i + q, j + p
                        if 0 <= ni < height and 0 <= nj < width:
                            if q == 0 and p == 0:
                                total += result[ni][nj] * 8
                            else:
                                total += result[ni][nj] * -1
                new_result[i][j] = max(0, min(255, total))
        new_result = [[[v, v, v] for v in row] for row in new_result]
        return RGBImage(new_result)


# Part 5: Image KNN Classifier #
class ImageKNNClassifier:
    """
    Represents a simple KNNClassifier
    """

    def __init__(self, k_neighbors):
        """
        Creates a new KNN classifier object
        """
        self.k_neighbors = k_neighbors

    def fit(self, data):
        """
        Stores the given of data and labels for later
        """
        if len(data) == 0:
            raise ValueError()
        images = [i[0].pixels for i in data]
        image1 = images[0]
        if not all([len(i) == len(image1)
                    and len(i[0]) == len(image1[0])
                    for i in images]):
            raise ValueError()
        self.data = data

    def distance(self, image1, image2):
        """
        Returns the distance between the given images

        >>> img1 = img_read_helper('img/steve.png')
        >>> img2 = img_read_helper('img/knn_test_img.png')
        >>> knn = ImageKNNClassifier(3)
        >>> knn.distance(img1, img2)
        15946.312896716909
        """
        if not all([isinstance(image1, RGBImage),
                    isinstance(image2, RGBImage)]):
            raise TypeError()
        pixel1 = image1.pixels
        pixel2 = image2.pixels
        if len(pixel1) != len(pixel2):
            raise ValueError()
        if len(pixel1[0]) != len(pixel2[0]):
            raise ValueError()
        pixels1 = [q for i in pixel1 for j in i for q in j]
        pixels2 = [q for i in pixel2 for j in i for q in j]
        diff = sum([(pixels1[i] - pixels2[i])
                    ** 2 for i in range(len(pixels1))]) ** 0.5
        return diff

    def vote(self, candidates):
        """
        Returns the most frequent label in the given list

        >>> knn = ImageKNNClassifier(3)
        >>> knn.vote(['label1', 'label2', 'label2', 'label2', 'label1'])
        'label2'
        """
        return max(set(candidates), key=candidates.count)


    def predict(self, image):
        """
        Predicts the label of the given image using the labels of
        the K closest neighbors to this image

        The test for this method is located in the knn_tests method below
        """
        if not hasattr(self, "data"):
            raise ValueError()
        dist = [(self.distance(image, i[0]), i[1]) for i in self.data]
        dist.sort(key=lambda x: x[0])
        return self.vote([i[1] for i in dist[:self.k_neighbors]])






def knn_tests(test_img_path):
    """
    Function to run knn tests

    >>> knn_tests('img/knn_test_img.png')
    'nighttime'
    """
    # Read all of the sub-folder names in the knn_data folder
    # These will be treated as labels
    path = 'knn_data'
    data = []
    for label in os.listdir(path):
        label_path = os.path.join(path, label)
        # Ignore non-folder items
        if not os.path.isdir(label_path):
            continue
        # Read in each image in the sub-folder
        for img_file in os.listdir(label_path):
            train_img_path = os.path.join(label_path, img_file)
            img = img_read_helper(train_img_path)
            # Add the image object and the label to the dataset
            data.append((img, label))

    # Create a KNN-classifier using the dataset
    knn = ImageKNNClassifier(5)

    # Train the classifier by providing the dataset
    knn.fit(data)

    # Create an RGBImage object of the tested image
    test_img = img_read_helper(test_img_path)

    # Return the KNN's prediction
    predicted_label = knn.predict(test_img)
    return predicted_label
