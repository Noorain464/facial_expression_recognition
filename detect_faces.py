import cv2
from fer import FER
from fer import Video
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

compliments = {
    "smile": "Your smile lights up the room!",
    "neutral": "Your presence is calm and confident!",
    "sad": "You’ve got this, keep going!",
    "angry": "Your passion and determination are truly inspiring!"
}
def detect_faces_from_video(file_path):
    video = Video(file_path)
    detector = FER(mtcnn=True)
    video_data = video.analyze(detector, display=False)
    output_video_path = f"output/{os.path.basename(file_path).split('.')[0]}_output.mp4" 
    df = video.to_pandas(video_data)

def detect_faces_from_image(file_path):
    input_image = cv2.imread(file_path)
    emotion_detector = FER()
    
    #display all emotions with scores
    emotions = emotion_detector.detect_emotions(input_image)
    print(emotions)

    #display the emotion with max score
    top_emotion = emotion_detector.top_emotion(input_image)
    print(top_emotion)

    #output image with the emotion detected
    max_emotion_text = f"{top_emotion[0]}: {top_emotion[1]}"
    bounding_box = emotions[0]["box"]
    emotion = emotions[0]["emotions"]
    color = (255, 0, 0)

    cv2.putText(input_image,max_emotion_text,
                (bounding_box[0], bounding_box[1] + bounding_box[3] + 30),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,color,1,cv2.LINE_AA,)
    output_image = f"output/images/{os.path.splitext(file_path)[0]}_output.jpg"
    cv2.imwrite(output_image, input_image)
    result_image = mpimg.imread(output_image)
    plt.imshow(result_image)
    compliment = compliments.get(top_emotion[0])
    print(compliment)

def file_path():
    file_path = input("Enter the file path: ")
    _, file_extension = os.path.splitext(file_path)
    
    file_extension = file_extension.lower()
    
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']
    video_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']

    if file_extension in image_extensions:
        return detect_faces_from_image(file_path)
    elif file_extension in video_extensions:
        return detect_faces_from_video(file_path)
    else:
        print("Invalid file type")
        return

file_path()
