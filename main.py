from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    if sentiment > 0.0:
        return Mood('😊', sentiment)
    elif sentiment < 0.0:
        return Mood('😠', sentiment)
    else:
        return Mood('😐', sentiment)


if __name__ == '__main__':
    while True:
        text: str = input('Text: ')
        mood: Mood = get_mood(text)

        print(f'{mood.emoji} ({mood.sentiment})')