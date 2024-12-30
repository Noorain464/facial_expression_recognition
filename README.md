# Facial Expression Recognition

## Overview

This project implements facial expression recognition using the FER (Facial Expression Recognition) library. It can detect emotions in images or videos and provide personalized compliments based on the detected emotions.

### Key Features:
- **Emotion Detection**: Detects emotions such as happy, sad, angry, surprised, and more.
- **Personalized Compliments**: Based on the detected emotion, a predefined compliment is displayed.
- **Works with both Images and Videos**: The solution supports emotion recognition from both image and video files.
- **Output**: For images, it generates an annotated image with the detected emotion. For videos, it generates an output video with the emotion information.

---

## Libraries and Tools Used:
- **OpenCV**: For image processing and video manipulation.
- **FER**: A facial expression recognition library that detects emotions from faces.
- **Matplotlib**: For displaying the output image.
- **os**: For file path handling.

---

## Challenges Faced & Solutions:
- **Challenge 1**: Detecting multiple emotions in a single frame.
    - **Solution**: I used the FER library to handle multiple emotions, selecting the one with the highest score.
    
- **Challenge 2**: Handling different input formats (images and videos).
    - **Solution**: The solution checks the file type and calls the respective function for images or videos, making the code flexible for both types of media.

- **Challenge 3**: Generating output images and videos for multiple frames.
    - **Solution**: For video processing, I used OpenCV to read each frame, process it, and write it back into an output video.

---

## Instructions to Run the Code:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/facial-expression-recognition.git
    ```

2. **Install dependencies**:

    Create a virtual environment (optional but recommended), then install the required libraries:

    ```bash
    pip install opencv-python fer matplotlib
    ```

3. **Run the code**:
   - For image input:
   
     ```bash
     python detect_faces.py
     ```

     The script will prompt you to enter the file path of an image. After processing, it will print the detected emotion and the associated compliment.

   - For video input, the script will process the video frames and output the annotated video.

---

