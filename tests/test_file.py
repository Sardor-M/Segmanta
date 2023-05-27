import unittest
import os
from utils.file_utils import load_images_from_folder

# Unit tests for the load_images_from_folder function
class FileUtilsTestCase(unittest.TestCase):

    def test_load_images_from_folder(self):

        folder = 'test_images'
        expected_images = ['test_images/image1.jpg', 'test_images/image2.png']

        # Create dummy image files in the test folder
        os.makedirs(folder, exist_ok=True)
        open('test_images/image1.jpg', 'a').close()
        open('test_images/image2.png', 'a').close()
        open('test_images/not_an_image.txt', 'a').close()

        # Call the load_images_from_folder function
        images = load_images_from_folder(folder)

        # Check if the loaded images match the expected images
        self.assertCountEqual(images, expected_images)

        # Remove the dummy image files
        os.remove('test_images/image1.jpg')
        os.remove('test_images/image2.png')
        os.remove('test_images/not_an_image.txt')
        os.rmdir('test_images')


if __name__ == '__main__':
    unittest.main()
