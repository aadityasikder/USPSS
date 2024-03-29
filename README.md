# Universal Student Profiling and Security System

This repository contains the source code and instructions for a Universal Student Profiling and Security System. The system utilizes a Jetson Nano for face detection and profiling, along with a Kivy-based GUI for user interaction and deployment on Android devices.

## Overview

The Universal Student Profiling and Security System aims to provide a comprehensive solution for educational institutions to manage student attendance, track movement within premises, and enhance security measures. The system utilizes facial recognition technology for accurate identification and profiling of students.

### Components

1. **csv_log_face_gui.py**: This Python script runs on the Jetson Nano and is responsible for face detection and profiling. It generates a CSV file containing information about detected faces.

2. **kivy_app.py**: This script creates a GUI using Kivy framework. It allows users to terminate the system and send the CSV file to the designated system using the IP address and password of the Jetson Nano.

3. **kivy_to_apk.ipynb**: This Jupyter Notebook demonstrates the process of converting the Kivy application into an Android APK file. This enables the deployment of the application on Android devices for convenient usage.

## Setup Instructions

### Requirements

- Jetson Nano with necessary dependencies installed for face detection.
- Python environment with required libraries (e.g., OpenCV, NumPy) for running scripts.
- Android Studio (for converting Kivy app to APK).

Sure, I'll add that instruction to the setup section:

### Steps

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/universal-student-profiling.git
```

2. Set up and configure the Jetson Nano with the necessary dependencies as specified in the documentation.

3. Run `sudo ifconfig` in the terminal of the Jetson Nano to determine its IP address.

4. Run `csv_log_face_gui.py` on the Jetson Nano to start the face detection and profiling process.

5. Run `kivy_app.py` on the system where you want to deploy the GUI. Ensure that you have the IP address and password of the Jetson Nano configured correctly within the script.

6. Interact with the GUI to terminate the system and send the CSV file to the designated system.

7. (Optional) Follow the instructions in `kivy_to_apk.ipynb` to convert the Kivy application into an APK file for deployment on Android devices.

## Contributors

- [Aaditya Sikder](https://github.com/aadityasikder)
- [Tridib jyoti Das](https://github.com/wheezydeeeb)
- []

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per the terms of the license.

