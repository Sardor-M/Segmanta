import os

## Load images from a folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            img = os.path.join(folder, filename)
            images.append(img)
    return images
