import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

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
            'LEETCODE_SESSION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiOTY4MDkyNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzRjMTEyMTFjM2FiYzRlMGI3NGJiMTkwMjFhMTAzZTIxNDkyYmNiZThkMTIzOThlYmZjZDE1ZDY4YjQ1YjJiMSIsInNlc3Npb25fdXVpZCI6ImI0Mjg2NzViIiwiaWQiOjk2ODA5MjQsImVtYWlsIjoiZmFsYWthaHVqYTAxMDFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJmYWxha2FodWphIiwidXNlcl9zbHVnIjoiZmFsYWthaHVqYSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9kZWZhdWx0X2F2YXRhci5qcGciLCJyZWZyZXNoZWRfYXQiOjE3NDMyNzE4MTIsImlwIjoiMTM2LjIzMy45LjEwNiIsImlkZW50aXR5IjoiM2ZhMzFiNTJkZDZlYmM1MTdlNTQ5MmQ0M2Q3N2U2MWMiLCJkZXZpY2Vfd2l0aF9pcCI6WyJlMjBlNzIxMWY0MWRiZTZiMWI2Zjg2ZTVjZGFlMzViMyIsIjEzNi4yMzMuOS4xMDYiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.WCKHgff6CU_34hIUvS3fbmm_g2nEtWPf_fwiF4g3o9o',  # Get from browser dev tools
            'csrftoken': 'vfrnotRgJeevpw5U6NWEQB951EeDZv2lp1WH3aMe1Qu4kwxgnuFOMI8zQcrQP8DT'             # Optional but recommended
        }
        try:
            response = requests.get(url, headers=self.headers, cookies=cookies, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None