# YOLOv8-Sleep-Detector-with-Text-to-Speech-Alert
This repository contains code for a real-time sleep detection system using YOLOv8 object detection and a webcam feed. The detector can identify whether a person's eyes are open or closed and determine if they are awake or asleep. When the system consistently detects closed eyes (indicating sleep) for about 4 seconds, it triggers a text-to-speech alert saying "Be Alert!".

## Getting Started

#### Install the required packages:
```
pip install -r requirements.txt
```

Download the YOLOv8 model weights and place them in the specified directory:
```
./runs/detect/train/weights/last.pt
```

Run the Webcam YOLOv8 detector script:
```
python AwakeOrSleepWebcamYOLOv8.py
```

## Usage
The webcam feed will open, and the system will start detecting eyes.

Detected eyes will be highlighted in green rectangles.

If closed eyes are consistently detected for about 4 seconds, a "Be Alert!" alert will be triggered through text-to-speech.

## Configuration
You can adjust the detection threshold by modifying the threshold variable in the AwakeOrSleepWebcamYOLOv8.py file.

Modify the alert trigger duration by changing the condition in the if count % 32 == 0: block.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Dataset Privacy Notice

Please note that the dataset used for training this model is not provided in this repository due to privacy concerns. 

The dataset is essential for training the model. However, you will need to source your own dataset for training purposes.

### Directory Structure
- Images: `./data/Awake&Sleep/images/train`
- Labels: `./data/Awake&Sleep/labels/train`

For privacy and ethical reasons, we are unable to provide the dataset. If you want to train your own model, please make sure to source your own dataset with images of open and closed eyes and corresponding labels indicating awake or sleep states. Ensure that your dataset follows a similar directory structure for successful training.

