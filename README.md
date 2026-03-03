**RAKSHAK**   Advanced Lane Assist System (ALAS)
Real-Time Lane Detection & Road Curvature Estimation

📌 Overview

The Advanced Lane Assist System (ALAS) is a computer vision-based driver assistance system that detects lane boundaries in real time using classical image processing techniques.

The system performs camera calibration, perspective transformation, lane pixel detection, curvature estimation, and overlays lane guidance information on video frames — simulating features found in modern ADAS (Advanced Driver Assistance Systems).

This project demonstrates end-to-end pipeline development for intelligent automotive vision systems.

🎯 Key Features

🎥 Real-time lane detection on images and videos

📷 Camera calibration & distortion correction

🔄 Bird’s-eye view perspective transformation

🛣️ Lane curvature estimation

📏 Vehicle offset from center calculation

📊 Real-time processing progress display

🎬 Output video generation

🧠 Tech Stack

Python

OpenCV

NumPy

Matplotlib

MoviePy (optional for video processing)

Docopt (CLI argument parsing)

🛠️ System Pipeline

The lane detection pipeline consists of the following stages:

Camera Calibration

Removes distortion using chessboard images.

Ensures geometric consistency.

Perspective Transformation

Converts road view into bird’s-eye view.

Makes lane detection more accurate.

Thresholding

Gradient and color thresholding.

Binary lane pixel extraction.

Lane Pixel Detection

Sliding window search.

Polynomial curve fitting.

Curvature & Offset Calculation

Radius of curvature estimation.

Vehicle deviation from lane center.

Overlay & Visualization

Lane region filled.

Curvature and offset values displayed.

🚀 How to Run
📷 Image Processing
python main.py input_image.jpg output_image.jpg
🎥 Video Processing
python main.py --video input_video.mp4 output_video.mp4

Press Q during processing to stop real-time display.

📊 Performance Highlights

Robust lane detection under varying lighting conditions

Real-time frame-by-frame video processing

Smooth polynomial curve fitting

Reliable curvature estimation

💼 Why This Project Matters

This project simulates a core component of:

🚗 ADAS systems

🛣️ Autonomous driving pipelines

🧠 Intelligent mobility solutions

It demonstrates:

Computer vision fundamentals

Real-time video processing

Automotive domain problem-solving

Modular pipeline architecture

🔮 Future Enhancements

Deep learning-based lane segmentation (CNN / UNet)

Real-time webcam integration

Steering angle prediction

Integration with vehicle control simulation

👨‍💻 Author

Milan Dhal
Machine Learning & Computer Vision Enthusiast

Final result blended with original frame.
