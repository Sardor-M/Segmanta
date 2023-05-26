import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
import cv2
import numpy as np

# Mouse callback function


def label_roi_with_model(roi, model):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[
                             0.229, 0.224, 0.225])
    ])

    roi_pil = Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
    roi_tensor = transform(roi_pil)
    roi_tensor = roi_tensor.unsqueeze(0)

    with torch.no_grad():
        model.eval()
        output = model(roi_tensor)
        predicted_mask = output.argmax(1).squeeze().detach().numpy()
        mask = (predicted_mask > 0).astype(np.uint8) * 255

    roi_masked = cv2.bitwise_and(roi, roi, mask=mask)
    return roi_masked

# Load the pretrained model


def load_pretrained_model():
    global model
    model = models.segmentation.deeplabv3_resnet50(pretrained=True)
    model = model.eval()
    return model
