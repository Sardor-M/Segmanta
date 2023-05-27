import unittest
import cv2
import os
import numpy as np
from unittest.mock import patch
from io import StringIO
from utils.annotation_utils  import label_roi, save_image, annotate_image, visualize_masks, save_annotated_images, load_gallery_images, browse_gallery


class TestProjectCode(unittest.TestCase):

    def setUp(self):

        self.image_path = "./data/standard_test_images/sample_12.jpg"

    def tearDown(self):
        if os.path.exists(self.image_path):
            os.remove(self.image_path)

    def test_label_roi(self):

        expected_label = "person"
        with patch('builtins.input', return_value=expected_label):
            label = label_roi()
        self.assertEqual(label, expected_label)

    def test_save_image(self):

        save_image()
        self.assertTrue(os.path.exists("result_images/result_image.jpg"))

    def test_annotate_image(self):

        expected_labels = [(cv2.imread(self.image_path), "person")]
        with patch('builtins.input', return_value="person"):
            with patch('cv2.imshow'):
                with patch('cv2.waitKey', return_value=ord('q')):
                    labels = annotate_image(self.image_path)
        self.assertEqual(labels, expected_labels)

    def test_visualize_masks(self):

        image = np.zeros((512, 512, 3), np.uint8)
        annotations = [(image, "person")]
        with patch('cv2.imshow'):
            with patch('cv2.waitKey', return_value=ord('q')):
                visualize_masks(image, annotations)

    def test_save_annotated_images(self):

        annotations = [(cv2.imread(self.image_path), "person")]
        save_annotated_images(annotations)
        self.assertTrue(os.path.exists(
            "data/annotated_images/annotated_image_0.jpg"))
        self.assertTrue(os.path.exists(
            "data/annotated_images/annotation_0.txt"))

    def test_load_gallery_images(self):
        expected_images = [cv2.imread(self.image_path)]
        expected_annotations = ["person"]

        gallery_images = []
        gallery_annotations = []

        with patch('project_code.load_images_from_folder', return_value=[self.image_path]):
            with patch('builtins.open', return_value=StringIO("person")):
                load_gallery_images()
        self.assertEqual(gallery_images, expected_images)
        self.assertEqual(gallery_annotations, expected_annotations)

    def test_browse_gallery(self):
        gallery_images = [cv2.imread(self.image_path)]
        gallery_annotations = ["person"]
        with patch('builtins.input', return_value="q"):
            with patch('cv2.imshow'):
                with patch('cv2.waitKey', return_value=ord('q')):
                    with patch('project_code.gallery_images', gallery_images):
                        with patch('project_code.gallery_annotations', gallery_annotations):
                            browse_gallery()


if __name__ == "__main__":
    unittest.main()
