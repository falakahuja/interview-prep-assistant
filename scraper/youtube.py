import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

class YouTubeScraper:  # This class name must match your import
    def __init__(self):
        self.api_key = os.getenv('YOUTUBE_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
    
    def search_videos(self, query, max_results=5):
        """Search YouTube for videos matching the query"""
        request = self.youtube.search().list(
            q=query,
            part='id,snippet',
            maxResults=max_results,
            type='video',
            relevanceLanguage='en'
        )
        response = request.execute()
        return self._parse_response(response)
    
    def _parse_response(self, response):
        """Format API response into a cleaner structure"""
        videos = []
        for item in response.get('items', []):
            videos.append({
                'title': item['snippet']['title'],
                'video_id': item['id']['videoId'],
                'thumbnail': item['snippet']['thumbnails']['high']['url'],
                'channel': item['snippet']['channelTitle'],
                'published_at': item['snippet']['publishedAt']
            })
        return videos

# Test function (optional)
if __name__ == "__main__":
    scraper = YouTubeScraper()
    print(scraper.search_videos("Python Interview"))