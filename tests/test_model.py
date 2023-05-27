import unittest
import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
import cv2
import numpy as np
from unittest.mock import patch
from utils.model_utils import label_roi_with_model, load_pretrained_model

# Test case for the model_utils.py file
class ModelUtilsTestCase(unittest.TestCase):

    def test_label_roi_with_model(self):
        # Create a dummy model for testing
        class DummyModel:
            def __init__(self):
                self.eval_called = False

            def eval(self):
                self.eval_called = True

        # Create a dummy ROI
        roi = np.zeros((100, 100, 3), dtype=np.uint8)

        # Create a dummy output tensor
        output_tensor = torch.zeros(1, 2, 100, 100)

        # Create a dummy expected mask
        expected_mask = np.ones((100, 100), dtype=np.uint8) * 255

        # Create a dummy model and patch the model function
        model = DummyModel()
        with patch.object(model, '__call__', return_value=output_tensor):
            # Call the label_roi_with_model function
            roi_masked = label_roi_with_model(roi, model)

        # Check if the model's eval function was called
        self.assertTrue(model.eval_called)

        # Check the shape of the returned masked ROI
        self.assertEqual(roi_masked.shape, roi.shape)

        # Check if the mask is correct
        mask = cv2.cvtColor(roi_masked, cv2.COLOR_BGR2GRAY)
        self.assertTrue(np.array_equal(mask, expected_mask))

    def test_load_pretrained_model(self):

        # Call the load_pretrained_model function
        model = load_pretrained_model()

        # Check if the model is not None
        self.assertIsNotNone(model)

        # Check if the model is in evaluation mode
        self.assertFalse(model.training)

        # Check if the model is an instance of DeepLabV3ResNet50
        self.assertIsInstance(
            model, models.segmentation.deeplabv3_resnet50.DeepLabV3ResNet50)

if __name__ == '__main__':
    unittest.main()
