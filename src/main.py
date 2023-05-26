import cv2
import os
from annotation_utils import annotate_image, visualize_masks, save_annotated_images, load_gallery_images, browse_gallery
from model_utils import load_pretrained_model
from file_utils import load_images_from_folder

def main():
    print("1. Load images from local directory:")
    choice = int(input("Enter 1 to load image(s) from the directory: "))

    if choice == 1:
        sample_images_folder = "data/standard_test_images" 
        sample_images = load_images_from_folder(sample_images_folder)
        if len(sample_images) == 0:
            print("No sample images found.")
            return
        for i, sample_image in enumerate(sample_images):
            print(f"{i+1}. {sample_image}")
        image_choice = int(input("Enter your sample image number to annotate: "))
        if image_choice < 1 or image_choice > len(sample_images):
            print("Invalid sample image choice.")
            return 
        image_pth = sample_images[image_choice -1]
    else:
        print("Invalid choice.")
        return 

    annotations = annotate_image(image_pth)
    save_annotated_images(annotations)
    visualize_masks(cv2.imread(image_pth), annotations)

    load_gallery_images()
    browse_gallery()

if __name__ == "__main__":
    main()
