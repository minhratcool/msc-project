import os
import pandas as pd
from app.sentiment_analysis_helper import SentimentAnalyzer
import time



folder_path = "InteractiveSentimentDataset"
chat_text = []
sentiment_value = []

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        # Read the content of the text file
        with open(file_path, 'rb') as file:
            lines = file.readlines()

        # Process each line to extract chat text and sentiment value
        
        for line in lines:
            try: 
                line = line.decode('utf-8')
                parts = line.strip().split(' : ')
                                
                if len(parts) == 2:
                    text = parts[1]
                    if text.endswith('-1'):
                        text = text[:-3]
                        chat_text.append(text)
                        sentiment_value.append(-1)
                    else:
                        chat_text.append(text[:-2])
                        sentiment_value.append(int(text[-1]))
                    
            except:
                pass

# Create a pandas DataFrame
data = {'Chat Text': chat_text, 'Sentiment Value': sentiment_value}
df = pd.DataFrame(data)
analyzer = SentimentAnalyzer()
sample_size = 1000

# Validate the DataFrame with pretrained model
start_point = time.time()
predicted_sentiment_value = []
for i in range(sample_size):
    sentiment = analyzer.analyze_sentiment(chat_text[i])[0].get('label')
    sentiment_encode = 0
    if sentiment == 'positive':
        sentiment_encode = 1
    elif sentiment == 'negative':
        sentiment_encode = -1
    predicted_sentiment_value.append(sentiment_encode)

# Calculate the number of matching elements
validate_set_result = sentiment_value[:sample_size]
matching_count = sum(1 for a, b in zip(predicted_sentiment_value, sentiment_value) if a == b)

# Calculate the matching percentage
total_elements = len(predicted_sentiment_value)
matching_percentage = (matching_count / total_elements) * 100

print(f"Matching Percentage: {matching_percentage:.2f}%")
end = time.time()
print('1st Calculation time spent: ', end - start_point)


# 2nd test
# Validate the DataFrame with pretrained model
start_point = time.time()
predicted_sentiment_value = []
sentiment = analyzer.analyze_sentiment(chat_text[:sample_size])
for s in sentiment:
    sentiment_encode = 0
    s_label = s.get('label')
    if s_label == 'positive':
        sentiment_encode = 1
    elif s_label == 'negative':
        sentiment_encode = -1
    predicted_sentiment_value.append(sentiment_encode)

# Calculate the number of matching elements
validate_set_result = sentiment_value[:sample_size]
matching_count = sum(1 for a, b in zip(predicted_sentiment_value, sentiment_value) if a == b)

# Calculate the matching percentage
total_elements = len(predicted_sentiment_value)
matching_percentage = (matching_count / total_elements) * 100

print(f"Matching Percentage: {matching_percentage:.2f}%")
end = time.time()
print('2nd Calculation time spent: ', end - start_point)