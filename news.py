import requests
from datetime import datetime, timedelta
import random


# Set up your API key
api_key = 'b71b2162991543ec8aeee0d002a5845b'

start_date = datetime.now() - timedelta(days=random.randint(1, 30))
from_date = start_date.strftime('%Y-%m-%d')

# Make a GET request to the News API endpoint
url = 'https://newsapi.org/v2/everything'
params = {
    'apiKey': api_key,
    'q': 'tips for mental health',  # Add keywords related to mental health
    'pageSize': 5,
    'from': from_date
}

response = requests.get(url, params=params)

# Check the response status code
if response.status_code == 200:
    data = response.json()
    articles = data.get('articles', [])

    # Process the articles as needed
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print(f"Published At: {article['publishedAt']}")
        print("\n")
else:
    print(f"Error: {response.status_code}, {response.text}")
