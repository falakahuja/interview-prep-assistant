import requests
import json
from typing import List, Dict

class LeetcodeScraper:
    def __init__(self):
        self.public_api_url = "https://leetcode.com/api/problems/all/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://leetcode.com/'
        }

    def scrape_by_topic(self, topic: str) -> List[Dict]:
        """Get problems filtered by topic tag (uses public API)"""
        try:
            response = requests.get(self.public_api_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            problems = []
            for item in data['stat_status_pairs']:
                if topic.lower() in [tag.lower() for tag in item['stat']['question__title_slug'].split('-')]:
                    problems.append({
                        'title': item['stat']['question__title'],
                        'slug': item['stat']['question__title_slug'],
                        'difficulty': ['Easy', 'Medium', 'Hard'][item['difficulty']['level'] - 1],
                        'url': f"https://leetcode.com/problems/{item['stat']['question__title_slug']}/"
                    })
            return problems
            
        except Exception as e:
            print(f"API Error: {str(e)}")
            return []

if __name__ == "__main__":
    scraper = LeetcodeScraper()
    
    print("Fetching array-related problems...")
    results = scraper.scrape_by_topic("array")
    
    if results:
        print(f"\nFound {len(results)} array problems:")
        for idx, problem in enumerate(results[:10], 1):  # Show first 10
            print(f"{idx}. {problem['title']} ({problem['difficulty']})")
            print(f"   Link: {problem['url']}\n")
    else:
        print("No problems found. Try a different topic like 'string' or 'tree'")