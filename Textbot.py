from textblob import TextBlob
import random

# Define messages for different moods
messages = {
    "positive": [
        "That's wonderful! Keep smiling 😊",
        "You're doing amazing! 🌟",
        "Happiness suits you so well! 💖"
    ],
    "negative": [
        "It’s okay to feel low. Tomorrow is a new day 🌈",
        "You are not alone. You're stronger than this 💪",
        "This too shall pass. Keep going 💙"
    ],
    "neutral": [
        "Sometimes a deep breath is all we need 🌬️",
        "Everything will fall into place. Stay steady 🧘",
        "Take your time. You're doing fine 💫"
    ]
}

# Get user input
text = input("How are you feeling today?\n> ")

# Analyze sentiment
blob = TextBlob(text)
polarity = blob.sentiment.polarity

# Choose mood type
if polarity > 0.2:
    mood = "positive"
elif polarity < -0.2:
    mood = "negative"
else:
    mood = "neutral"

# Print a random message based on mood
response = random.choice(messages[mood])
print(f"\nMindMate says: {response}")
