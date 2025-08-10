from deepface import DeepFace
import cv2
from gtts import gTTS
from playsound import playsound
import os
import random

# Emotion-based responses
responses = {
    "happy": [
        "Yay! Happy people throw trash too!",
        "Your smile is contagious, so is cleanliness!",
    ],
    "sad": [
        "Feeling down? Dump your worries here too.",
        "Sadness fades, but clean surroundings stay!",
    ],
    "angry": [
        "Cool down! Throw that anger in the bin!",
        "Don't be mad, just be clean!",
    ],
    "surprise": [
        "Surprised? Me too! Trash me gently!",
        "Unexpected emotions need expected actions. Bin it!",
    ],
    "fear": [
        "Don't be scared, I'm just a talking bin!",
        "Fear not. Cleanliness is your friend.",
    ],
    "neutral": [
        "Let’s make your neutral day a clean one!",
        "Be the change. Start with me.",
    ],
    "disgust": [
        "Throw that disgust away, literally!",
        "Let’s clean that feeling up!"
    ]
}

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "mood_response.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# Start camera
cap = cv2.VideoCapture(0)
print("MoodBin is watching... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Show the frame
    cv2.imshow("MoodBin Camera", frame)

    # Analyze every 60 frames (roughly every 2 seconds)
    if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % 60 == 0:
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
            print(f"Detected Emotion: {emotion}")

            if emotion in responses:
                message = random.choice(responses[emotion])
            else:
                message = "Let's clean our surroundings with a smile!"

            print(f"MoodBin says: {message}")
            speak(message)

        except Exception as e:
            print("Emotion detection failed:", str(e))

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
