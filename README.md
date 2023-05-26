# Segmanta

## 📝 Project Description

This is Interactive Image Segmentation Tool that allows users to segment and annotate objects in images based on their semantic measurments. The tool provides an intuitive interface for users to draw regions of interest (ROI) around objects in an image and assign corresponding semantic labels to those regions.

## 🏗️ Project Structure

The project is structured as follows:

```
|───tests
|   ├───test_annotation_utils.py
|   ├───test_file_utils.py
|   └───test_model_utils.py
├───result_images
├───.gitignore
├───src
│   ├───__pycache__
│   └───data 
│       ├───annotated_images
│       └───standard_test_images
|   └───prev_source_code_folder
│       └───main_prev.py
│   ├───annotation_utils.py
│   ├───file_utils.py
│   ├───main.py
│   └───model_utils.py
├───LICENSE.md
└───README.md
```


##

## 🔐 Features:

- **[x] Interactive Image Segmentation**
  - [x] Freehand Drawing
  - [x] Polygon Selection
  - [x] Rectangle Selection
  - [x] Define ROIs around objects
  - [x] Assign semantic labels to ROIs


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

- [ ] Real Time Image Segmentation: The current version of the program only allows users to segment images that are already stored on their local machine. In the future, I would like to implement a feature that allows users to segment images in real time using their webcam.
- [ ] Active Learning for Semantic Segmentation: This includes implementing an active learning approach where the toll learns from the user's annotations and provides suggestions for the next best annotation to be made. 


## 📝 License

> This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<!-- 
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
│   ├───annotation_utils.py
│   ├───file_utils.py
│   ├───main.py
│   └───model_utils.py
├───LICENSE.md
└───README.md
``` -->
