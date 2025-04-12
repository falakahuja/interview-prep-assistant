from backend.gemini_helper import get_roadmap, cache_response
# --------------------------
# 🚀 Test Roadmap Caching
# --------------------------
print("\n📚 Testing Roadmap Caching")

# First call (cache miss - loads from JSON)
roadmap1 = get_roadmap("software engineer", "beginner")
print("Roadmap 1 (First Call):")
print(roadmap1)

# Cached call (should be faster)
roadmap2 = get_roadmap("software engineer", "beginner")
print("\nRoadmap 2 (Cached Call, Should be Instant):")
print(roadmap2)

# New role to add to cache
roadmap3 = get_roadmap("data scientist", "intermediate")
print("\nRoadmap 3 (New Role, Adds to Cache):")
print(roadmap3)

# --------------------------
# 🤖 Test AI Response Caching
# --------------------------
print("\n🧠 Testing AI Response Caching")

# First API call (cache miss - makes an API request)
prompt1 = "Explain cloud computing"
response1 = cache_response(prompt1)
print(f"\nFirst API Call Response:\n{response1}")

# Cached API call (should be instant from cache)
response2 = cache_response(prompt1)
print(f"\nCached Response (Should be Instant):\n{response2}")

# Another unique prompt to test cache miss
prompt2 = "Define machine learning"
response3 = cache_response(prompt2)
print(f"\nNew Prompt Response:\n{response3}")
