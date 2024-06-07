# Sentiment Analysis Chatbot

## Overview
The Sentiment Analysis Chatbot is an AI-powered tool designed to analyze and interpret the emotional tone of text input. Utilizing the TextBlob library, this chatbot can determine the sentiment polarity of a given text and provide an appropriate emoji representation of the sentiment. The chatbot categorizes sentiments as positive, negative, or neutral, enhancing user interactions by providing immediate feedback on the emotional tone of their messages.

## Features
\- **Sentiment Detection:** Uses **TextBlob** to analyze the sentiment polarity of the input text.
\- **Emoji Representation:** Represents the detected sentiment with corresponding emojis: 😊 for positive, 😠 for negative, and 😐 for neutral.
\- **Real-time Analysis:** Provides instant sentiment analysis results for user input.
\- **User-friendly Interface:** Simple text-based interface for easy interaction.

## Installation
To get started with the Sentiment Analysis Chatbot, follow these steps:

1. ### Clone the repository:

```python
git clone https://github.com/your-username/sentiment-analysis-chatbot.git
cd sentiment-analysis-chatbot
```

2. ### Install dependencies:

```python
pip install -r requirements.txt
```

## Usage
After installing the dependencies, you can start the chatbot by running the following command:

```python
python app.py
```

Interact with the chatbot by entering text, and it will respond with the corresponding sentiment emoji and polarity score.

Example:

```python
Text: I love the new update!
😊 (0.5)
```

## Code Explanation
### Mood Dataclass
The Mood dataclass is used to store the emoji and sentiment polarity score of the analyzed text.

```python
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float
```

### get_mood Function
The **get_mood** function takes an input text, analyzes its sentiment using **TextBlob**, and returns a **Mood** object with the appropriate emoji and sentiment polarity score.

```python
from textblob import TextBlob

def get_mood(input_text: str) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    if sentiment > 0.0:
        return Mood('😊', sentiment)
    elif sentiment < 0.0:
        return Mood('😠', sentiment)
    else:
        return Mood('😐', sentiment)
```

### Main Loop
The main loop continuously prompts the user for text input, analyzes the sentiment, and prints the result.

```python
if __name__ == '__main__':
    while True:
        text: str = input('Text: ')
        mood: Mood = get_mood(text)

        print(f'{mood.emoji} ({mood.sentiment})')
```

## Contributing
I welcome contributions from the community! If you have suggestions for improvements or new features, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact shivashishprusty@gmail.com.
