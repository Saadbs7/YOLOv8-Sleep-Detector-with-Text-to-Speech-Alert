import cv2
import os
import time
from ultralytics import YOLO
import pyttsx3
import threading

model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'last.pt')

# Load a model
model = YOLO(model_path)  # load the model

# Select webcam source and read frame
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
threshold = 0.5

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# Used to record the time when we processed last frame 
prev_frame_time = 0
# Used to record the time at which we processed current frame 
new_frame_time = 0

# Innitializing pyttsx3 engine
engine = pyttsx3.init()
# Alert function to run speach command in a seperate thread
def alert():
    # Convert text to speech and play it in a separate thread
    def play_speech():
        engine.say("Be Alert!")
        engine.runAndWait()
    
    # Create a thread to play the speech
    speech_thread = threading.Thread(target=play_speech)
    speech_thread.start()

count = 1   # Counter for Alert

while ret:
    # If images are in grayscale, use the following commented lines.
    # grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # reshapedframe = cv2.cvtColor(grayframe, cv2.COLOR_GRAY2RGB)
    # results = model(reshapedframe)[0]

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            if results.names[int(class_id)].upper() == "AWAKE":
                count = 0
            elif results.names[int(class_id)].upper() == "SLEEP":
                count += 1

    # After about 4 seconds of consistent SLEEP detection on my Machine (I am getting 8 fps) 
    if count % 32 == 0:
        alert()

    # Calculating the fps
    new_frame_time = time.time()
    fps = 1/(new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
  
    # Converting the fps into integer an then into string
    fps = str(int(fps))
  
    # Putting the FPS count on the frame
    cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('Detection',frame)

    ret, frame = cap.read()

    c = cv2.waitKey(1)
    if c == 27:
        break
    
cap.release()
cv2.destroyAllWindows()