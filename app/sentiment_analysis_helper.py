from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self):
        self.pipeline = pipeline("text-classification", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")

    def analyze_sentiment(self, text):
        sentiment = self.pipeline(text)
        return sentiment