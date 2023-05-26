# Segmanta

[![GitHub  ](https://img.shields.io/github/license/Sardor-M/Segmanta)](github)
[![GitHub contributors](https://img.shields.io/github/contributors/Sardor-M/Segmanta)](github)
[![GitHub last commit](https://img.shields.io/github/last-commit/Sardor-M/Segmanta)](github)

<desc> 💼 Segmanta is an Image Segmentation Tool - IIST </desc>

## 📌 Table of Contents

- [📌 Table of Contents](#-table-of-contents)
- [📝 Project Description](#-project-description)
- [🏗️ Project Structure](#️-project-structure)
- [🔐 Features](#-features)
- [📦 Dependencies](#-dependencies)
- [📜 Usage](#-usage)
  - [Installation :](#installation-)
  - [Running the Program :](#running-the-program-)
- [📚 References](#-references)
- [📌 TODO](#-todo)
- [📝 License](#-license)
- [📌 Contact](#-contact)

## 📝 Project Description

This is an Interactive Image Segmentation Tool that allows users to segment and annotate objects in images based on their semantic measurments. This tool is built using OpenCV and Python. Using this tool, users can segment images using freehand drawing, polygon selection, and rectangle selection. And then, users can assign semantic labels to the regions of interest (ROI) that they have defined. Also users can view annotated images in gallery view and save them to their local machine.

## 🏗️ Project Structure

The project is structured as follows:

```
|───tests
|   ├───test_annotation_utils.py
|   ├───test_file_utils.py
|   └───test_model_utils.py
├───.gitignore
├───src
│   ├───__pycache__
│   └───data
│       ├───annotated_images
│       └───standard_test_images
|   └───prev_source_code_folder
│       └───main_prev.py
|   └───result_images
│   ├───annotation_utils.py
│   ├───file_utils.py
│   ├───main.py
│   └───model_utils.py
├───LICENSE.md
└───README.md
```

##

## 🔐 Features:

- [x] **Interactive Image Segmentation**
- [x] **Freehand Drawing**
- [x] **Polygon Selection Drawing**
- [x] <del> Rectangle Selection </del>
  - **This has to be fixed, not working as expected**
- [x] <del> Define ROIs around objects </del>
- [x] **Assign semantic labels to ROIs**
  - **This has to be fixed, not working as expected**
- [x] **View Annotated Imaages in Gallery View**
  - **This feature is implemented, but needs more work and improvement**
- [x] **Save Annotated Images to Local Machine**

## 📦 Dependencies

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
- [OpenCV 4.5.1](https://opencv.org/)
- [Numpy 1.19.2](https://numpy.org/)
- [Pytorch 1.7.1](https://pytorch.org/)
- [Pillow 8.1.0](https://pillow.readthedocs.io/en/stable/)
- [Torchvision 0.8.2](https://pypi.org/project/torchvision/)
- [Transformers 4.3.3](https://pypi.org/project/transformers/)

## 📷 Result Examples

### Freehand Drawing

![Freehand Drawing]()

### Polygon Selection

![Polygon Selection]()

### Rectangle Selection

![Rectangle Selection]()

### ROI Definition

![ROI Definition]()

### Semantic Label Assignment

![Semantic Label Assignment]()

## 📜 Usage

### Installation :

```bash
git clone https://github.com/Sardor-M/Segmanta.git
```

### Running the Program :

```bash
cd src
python main.py
```

## 📚 References

- [OpenCV](https://opencv.org/)
- [Computer Vision Tutorials](https://github.com/mint-lab/cv_tutorial)
- [Introduction to Semantic Image Segmentation](https://medium.com/analytics-vidhya/introduction-to-semantic-image-segmentation-856cda5e5de8)
- [Image Segmentation using OpenCv](https://nayakpplaban.medium.com/image-segmentation-using-opencv-39013013920a)
- [Semantic Segmentation](https://www.jeremyjordan.me/semantic-segmentation/)

## 📌 TODO

> Note that below To Do list is not intended to be exhaustive. It is just a list of features that I would like to implement in the future.

- [ ] **Annotate Images using Pre-Trained Models:**
  - As of now, pretrained model method is defined, but needs more imporvement. It will be implemented in the future.
- [ ] **Fix Rectangle Selection:**
  - The current version of the program does not allow users to select ROIs using a rectangle. This feature has to be fixed.
- [ ] **Fix Semantic Label Assignment:**
  - The current version of the program does not allow users to assign semantic labels to ROIs. This feature has to be fixed.
- [ ] **Real Time Image Segmentation:**
  - The current version of the program only allows users to segment images that are already stored on their local machine.
  - In the future, I would like to implement a feature that allows users to segment images in real time using their webcam.
- [ ] **Active Learning for Semantic Segmentation:**
  - This includes implementing an active learning approach where the toll learns from the user's annotations and provides suggestions for the next best annotation to be made.
- [ ] **Implementing a Web App and Integrating the GUI that allows users to interact with Semantic Image Segmentation Tool:**
  - I would like to implement a web app that allows users to segment images online.
  - This will allow users to segment images without having to install the program on their local machine.
  - This will also allow users to share their annotations with other users.

## 📝 License

> This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## 📌 Contact

> Feel free to contribute, fork or star or if you have any questions or suggestions please contact me.
>
> - **sardor0968@gmail.com**
