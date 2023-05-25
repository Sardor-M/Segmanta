import cv2
import numpy as np
import os
import torch 
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models


# Global variables
drawing = False
roi_points = []
labels = []
current_label = None
model = None

## Mouse callback function
def draw_roi(event, x, y, flags, param):
    global drawing, roi_points
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        roi_points = [(x, y)]

    ## Check if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        roi_points.append((x, y))
        cv2.rectangle(img, roi_points[0], roi_points[1], (0, 255, 0), 2)
        cv2.imshow('Image', img)


## Label the ROI
def label_roi():
    global current_label
    label = input("Enter the label for the ROI (e.g., person, car or etc): ")
    current_label = label


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            img = os.path.join(folder, filename)
            images.append(img)
    return images


## Annotate the image
def annotate_image(image_path):
    global img, labels
     
    img =cv2.imread(image_path)
    clone = img.copy()

    ## Create a window and set mouse callback
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", draw_roi)
    
    ## Loop until the 'q' key is pressed
    while True:
        cv2.imShow("Image", img)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("n"):
            label_roi()
        
        elif key == ord("h"):
            if len(roi_points) == 2 and current_label:
                roi = clone[roi_points[0][1]:roi_points[1][1], roi_points[0][0]:roi_points[1][0]]
                labels.append((roi, current_label))
                cv2.imshow("ROI", roi)
                cv2.waitKey(0)
                current_label = None

        elif key == ord("e"):
            if len(roi_points) == 2 and current_label:
                roi = clone[roi_points[0][1]:roi_points[1][1], roi_points[0][0]:roi_points[1][0]]
                labeled_roi = label_roi_with_model(roi)
                cv2.imshow("ROI",labeled_roi)
                cv2.waitKey(0)
                user_correction = input("Enter the corrected label for the ROI: ")
                if user_correction:
                    labels.append((labeled_roi, user_correction))
                else:
                    labels.append((labeled_roi, current_label))
                current_label = None
        
        elif key == ord('q'):
            break

        # Close all the open windows
        cv2.destroyAllWindows()

        return labels

# Save the labels
print("Saving labels...")

## Label the ROI with the model
def label_roi_with_model(roi):
    global model

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    roi_pil = Image.fromarray(cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    roi_tensor = transform(roi_pil)
    roi_tensor = roi_tensor.unsqueeze(0)

    with torch.no_grad():
        model.eval()
        output = model(roi_tensor)
        predicted_mask = output.argmax(1).squeeze().detach().numpy()
        mask = (predicted_mask > 0).astype(np.uint8) * 255

    roi_masked = cv2.bitwise_and(roi, roi, mask=mask)
    return roi_masked

## Save the annotated images
def save_annotated_images(annotations):
    folder_name = "src/annotated_images"
    os.makedirs(folder_name, exist_ok=True)

    for i, (roi, label) in enumerate(annotations):
        annotated_image_path = os.path.join(folder_name, f"annotated_image_{i}.jpg")
        cv2.imwrite(annotated_image_path, roi)

        annotation_file_path = os.path.join(folder_name, f"annotation_{i}.txt")
        with open(annotation_file_path, "w") as f:
            f.write(label)


## Load pre-trained model 
def load_pretrained_model():
    global model
    model = models.segmentation.deeplabv3_resnet50(pretrained=True)
    model = model.eval()

## Main function 
def main():
    print("1. Load images from local directory")
    print("2. Load images from Google Drive")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        folder_path = input("Enter the path to the folder: ")
        images = load_images_from_folder(folder_path)
        if len(images) == 0:
            print("No names found in the specified folder")
            return 
        for i, image_pth in enumerate(images):
            print(f"{i+1}. {image_pth}")
        image_choice = int(input("Enter your choice of number to annotate: "))
        if image_choice > 1 or image_choice < len(images):
            print('Invalid image choice')
            return
        image_pth = images[image_choice - 1]
    elif choice == 2:
        sample_images_folder = "./data/sample_images" 
        sample_images = load_images_from_folder(sample_images_folder)
        if len(sample_images) == 0:
            print("No sample images found.")
            return
        for i, sample_image in enumerate(sample_images):
            print(f"{i+1}. {sample_image}")
        image_choice = int(input("Enter your sample mage number to annotate: "))
        if image_choice < 1 or image_choice > len(sample_images):
            print("Invalid sample image choice.")
            return 
        image_pth = sample_images[image_choice -1]
    else:
        print("Invalid choice.")
        return 
        #  Here starts 

    annotations = annotate_image(image_pth)
    save_annotated_images(annotations)
##
if __name__ == "__main__":
    main()
        
    
