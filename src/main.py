import cv2
import numpy as np
import os

# Global variables
drawing = False
roi_points = []
labels = []
current_label = None

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
            elif key == ord('q'):
                break

        # Close all the open windows
        cv2.destroyAllWindows()

        return labels

# Save the labels
print("Saving labels...")

def save_annotated_images(annotations):
    for i, (roi, label) in enumerate(labels):
        cv2.imwrite(f"annotated_image_{i}.jpg", roi)
        with open(f"annotation_{i}.txt", "w") as f:
            f.write(label)

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
        for i, image in enumerate(images):
            print(f"{i+1}. {image}")

        #  Here starts 

    image_path ="./data/nature.jpg" 
    annotations = annotate_image(image_path)
    save_annotated_images(annotations)
##
if __name__ == "__main__":
    main()
        
    
