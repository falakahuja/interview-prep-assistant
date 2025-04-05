import requests
from typing import List, Dict

class LeetcodeScraper:
    def __init__(self):
        self.public_api_url = "https://leetcode.com/api/problems/all/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://leetcode.com/'
        }
        # Expanded keyword mapping including graph-related terms
        self.topic_keywords = {
            'graph': ['graph', 'dfs', 'bfs', 'shortest', 'path', 'topological', 'adjacency'],
            'dp': ['dp', 'dynamic', 'memoiz', 'knapsack', 'subsequence'],
            'tree': ['tree', 'binary', 'bst', 'trie', 'n-ary'],
            'array': ['array', 'subarray', 'contiguous'],
            'string': ['string', 'substring', 'palindrome']
        }

    def scrape_by_topic(self, topic: str) -> List[Dict]:
        """Get problems filtered by topic with enhanced matching"""
        try:
            response = requests.get(self.public_api_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Normalize topic input
            normalized_topic = self._normalize_topic(topic.lower())
            search_terms = self.topic_keywords.get(normalized_topic, [normalized_topic])
            
            problems = []
            for item in data['stat_status_pairs']:
                slug = item['stat']['question__title_slug'].lower()
                title = item['stat']['question__title'].lower()
                
                # Check if any keyword matches in title or slug
                if any(term in slug or term in title for term in search_terms):
                    problems.append({
                        'title': item['stat']['question__title'],
                        'slug': item['stat']['question__title_slug'],
                        'difficulty': ['Easy', 'Medium', 'Hard'][item['difficulty']['level'] - 1],
                        'url': f"https://leetcode.com/problems/{item['stat']['question__title_slug']}/",
                        'topics': self._detect_topics(slug, title)
                    })
            return problems
            
        except Exception as e:
            print(f"API Error: {str(e)}")
            return []

    def _normalize_topic(self, topic: str) -> str:
        """Handle plural/singular forms and synonyms"""
        mappings = {
            'graphs': 'graph',
            'arrays': 'array',
            'strings': 'string',
            'trees': 'tree',
            'dp': 'dynamic programming',
            'dynprog': 'dynamic programming'
        }
        return mappings.get(topic, topic)

    def _detect_topics(self, slug: str, title: str) -> List[str]:
        """Identify all relevant topics for a problem"""
        detected = []
        for topic, keywords in self.topic_keywords.items():
            if any(kw in slug or kw in title for kw in keywords):
                detected.append(topic)
        return detected if detected else ['general']

if __name__ == "__main__":
    scraper = LeetcodeScraper()
    
    # Test cases
    test_terms = ["graph", "graphs", "dp", "dynamic programming", "tree"]
    for term in test_terms:
        results = scraper.scrape_by_topic(term)
        print(f"\nSearch: '{term}' => Found {len(results)} problems")
        if results:
            print(f"Example: {results[0]['title']} (Topics: {', '.join(results[0]['topics'])})")