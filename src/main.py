import cv2
import numpy as np

# Global variables
drawing = False
roi_points = []
labels = []
current_label = None

def draw_roi(event, x, y, flags, param):
    global drawing, roi_points

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        roi_points = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        roi_points.append((x, y))
        cv2.rectangle(img, roi_points[0], roi_points[1], (0, 255, 0), 2)
        cv2.imshow('Image', img)

def label_roi():
    global current_label
    label = input("Enter the label for the ROI (e.g., person, car, etc.): ")
    current_label = label

def annotate_image(image_path):
    global img, labels

    img = cv2.imread(image_path)
    clone = img.copy()

   

