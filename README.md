# Plant Detection with YOLOv8 🌿

This repository contains the source code for a custom object detection model built with **YOLOv8**. The model is trained to detect specific plants (labeled as `y_bitki`).

Due to GitHub's file storage limits, the large image dataset required for training and testing is hosted externally on Kaggle.

## 📂 Dataset

The dataset is hosted on Kaggle. To run this project, you must download the dataset from the link below.

👉 **[Download Plant Detection Dataset from Kaggle](https://www.kaggle.com/datasets/miraybalkolu/plant-detection-dataset)**

### Setup Instructions
1. Download the `archive.zip` file from the Kaggle link above.
2. Extract the contents of the zip file into the root directory of this project.
3. Ensure your folder structure matches the layout below so the script can find the images:

Plant-Detection-YOLOv8/
├── train/
│   └── images/
├── test/
│   └── images/
├── val/
│   └── images/
├── dataset1.yaml
├── main.py
├── yolov8n.pt
├── yolov8m.pt
└── README.md
🛠 Installation
Clone the repository:

Bash

git clone [https://github.com/YOUR_USERNAME/Plant-Detection-YOLOv8.git](https://github.com/YOUR_USERNAME/Plant-Detection-YOLOv8.git)
cd Plant-Detection-YOLOv8
Install dependencies: This project requires the ultralytics library.

Bash

pip install ultralytics
🚀 Usage
To start training the model using the default Nano model, run the main.py script.

Bash

python main.py
Configuration
The dataset1.yaml file is configured to use relative paths. It expects the dataset folders (train, test, val) to be located in the same directory as the script.

YAML

path: . 
train: train/images
val: val/images
test: test/images

nc: 1
names: ["y_bitki"]
⚙️ Model Selection (Optional)
By default, the script uses YOLOv8 Nano (yolov8n.pt) for faster training. If you require higher accuracy, this repository also includes the YOLOv8 Medium (yolov8m.pt) model.

To use the Medium model:

Open main.py.

Change the line model = YOLO('yolov8n.pt') to model = YOLO('yolov8m.pt').

📊 Model Details
Task: Object Detection

Classes: y_bitki (Plant)

Epochs: 70

Image Size: 640

Batch Size: 5

📝 License
This project is open-source and available for educational and research purposes.
