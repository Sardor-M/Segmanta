import cv2
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

def annotate_image(image_path):
    global img, labels
     
    img =cv2.imread(image_path)
    clone = img.copy()

    ## Create a window and set mouse callback
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", draw_roi)
    
    ## Loop until the 'q' key is pressed
    while True:
        cv2.imshow("Image", img)
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

    cv2.destroyAllWindows()
    return labels

def visualize_masks(image, annotations):
    for (roi_masked, _), label in zip(annotations, annotations):
        mask = cv2.cv2Color(roi_masked, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    
    cv2.imshow("Mask Visualization", image)
    cv2.waitKey(0)

def save_annotated_images(annotations):
    folder_name = "data/annotated_images"
    os.makedirs(folder_name, exist_ok=True)

    for i, (roi, label) in enumerate(annotations):
        annotated_image_path = os.path.join(folder_name, f"annotated_image_{i}.jpg")
        cv2.imwrite(annotated_image_path, roi)

        annotation_file_path = os.path.join(folder_name, f"annotation_{i}.txt")
        with open(annotation_file_path, "w") as f:
            f.write(label)

def load_gallery_images():
    global gallery_images, gallery_annotations

    annotated_images_folder = "data/annotated_images"
    images = load_images_from_folder(annotated_images_folder)

    for image_path in images:
        image = cv2.imread(image_path)
        annotation_file_path = image_path.replace(".jpg", ".txt")
        with open(annotation_file_path, "r") as f:
            annotation = f.read()
        gallery_images.append(image)
        gallery_annotations.append(annotation)

def browse_gallery():
    global gallery_images, gallery_annotations

    if len(gallery_images) == 0:
        print("No images found in the gallery")
        return
    while True:
        for i, image in enumerate(gallery_images):
            cv2.imshow(f"Image {i+1}", image)
            print(f"{i+1}. {gallery_annotations[i]}")

        key = cv2.waitKey(0) & 0xFF
        cv2.destroyAllWindows()

        if key == ord("q"):
            break
        elif key >= ord('1') and key <= ord(str(len(gallery_images) + ord("O"))):
            index = key - ord('1')
            selected_image = gallery_images[index]
            selected_annotation = gallery_annotations[index]
            cv2.imshow("Selected image", selected_image)
            print(f"Selected Annotation: {selected_annotation}")
            key = cv2.waitKey(0) & 0xFF
            cv2.destroyAllWindows()
