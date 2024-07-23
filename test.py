from textblob import TextBlob


import requests


params = {}
params['text'] = 'I feel great!'
params['f'] = 'value2'
response = requests.get('http://localhost:5001/sentiment', params=params)
# Print the JSON response
print(response.text)  

