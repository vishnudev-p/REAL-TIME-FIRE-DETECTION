# REAL-TIME-FIRE-DETECTION
Real-Time Fire Detection is a project aimed at early detection of fires using machine learning and computer vision techniques. This project provides a real-time fire monitoring system that can alert authorities or homeowners at the earliest onset of a fire, potentially saving lives and property.

Features
Real-time Detection: Capable of detecting fires in real-time using live video feeds.
Machine Learning: Uses state-of-the-art machine learning models optimized for fire detection.
Notifications: Provides instant alerts via SMS, email, or other integrations when a fire is detected.
Historical Data: Saves detected incidents for future review and analysis.
User-friendly Interface: Comes with a GUI for easy setup and monitoring.
Prerequisites
Python 3.x
OpenCV
TensorFlow or PyTorch (depending on the selected model)
Installation
Clone this repository:
git clone https://github.com/yourusername/Real-Time-Fire-Detection.git

Navigate to the project directory:
cd Real-Time-Fire-Detection

Install the required dependencies:
pip install -r requirements.txt

Usage
To start the fire detection on your webcam:
python fire_detection.py --source 0

To start the fire detection on an IP camera:
python fire_detection.py --source <your_ip_camera_url>

To use a pre-trained model:
python fire_detection.py --source 0 --model_path models/pretrained_model.h5
