import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()  # Loads .env file
# Load API key
API_KEY = os.getenv('YOUTUBE_API_KEY')

# Debug: Check if API key exists
print("API_KEY exists?", bool(API_KEY))  # <-- ADD THIS LINE

youtube = build('youtube', 'v3', developerKey=API_KEY)

def test_api():
    request = youtube.search().list(
        q="Python Interview",
        part="snippet",
        type="video",
        maxResults=5
    )
    response = request.execute()
    print(response)

if __name__ == "__main__":  # <-- Best practice to add this
    test_api()