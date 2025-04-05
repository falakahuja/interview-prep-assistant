import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv
load_dotenv()


class BaseScraper(ABC):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://leetcode.com/',
            'Connection': 'keep-alive'
        }

    
    @abstractmethod
    def scrape(self, query):
        """Main method to implement in child classes."""
        pass
        
    def _get_page(self, url):
        cookies = {
            'LEETCODE_SESSION': os.getenv('LEETCODE_SESSION'),
            'csrftoken': os.getenv('CSRF_TOKEN')
        }
        try:
            response = requests.get(url, headers=self.headers, cookies=cookies, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None