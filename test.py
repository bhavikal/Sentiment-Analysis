from textblob import TextBlob

# def perform_sentiment_analysis(text):
#     blob = TextBlob(text) #blob
#     # Perform sentiment analysis
#     sentiment_score = blob.sentiment.polarity
#     # Determine sentiment
#     if sentiment_score > 0.5:
#         sentiment = "Positive"
#     elif sentiment_score < -0.5:
#         sentiment = "Negative"
#     else:
#         sentiment = "Neutral"
    
#     return sentiment, sentiment_score

# if __name__ == "__main__":
#     # Test sentiment analysis with sample text
#     sample_text = "I dislike this product!"
#     sentiment, score = perform_sentiment_analysis(sample_text)
#     print(f"Sentiment: {sentiment}, Score: {score}")

import requests

# # Test the index route
# response = requests.get('http://localhost:5001/')
# print(response.text)  # Print the response content

# # Test the analyze route
# response = requests.get('http://localhost:5000/analyze', params={'journal_entry': 'I feel great!'})
# print(response.text)  # Print the response content

# Test the sentiment route

params = {}
params['text'] = 'I feel great!'
params['f'] = 'value2'
response = requests.get('http://localhost:5001/sentiment', params=params)
print(response.text)  # Print the JSON response

# # Test the resources route
# response = requests.get('http://localhost:5000/resources', json={'sentiment_score': 0.8})
# print(response.text)  # Print the JSON response