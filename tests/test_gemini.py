# tests/test_gemini.py
# Run pytest with output visible ,              
#python -m pytest tests/ --capture=no   , run this command  to run the tests  

import pytest
from backend.gemini_helper import generate_response
from backend.utils import cache_response
from backend.roadmap_generator import generate_basic_roadmap

def test_generate_response():
    """Test API response with a sample prompt."""
    response = generate_response("What is AI?", "markdown")
    print(response)
    assert "AI" in response

def test_cached_response():
    """Test caching mechanism."""
    prompt = "Explain cloud computing"
    experience = "intermediate"
    level = "beginner"

    response1 = cache_response(prompt, experience, level)
    response2 = cache_response(prompt, experience, level)

    assert response1 == response2  # Should return cached version

def test_invalid_format():
    """Test invalid format handling."""
    response = generate_response("Define IoT", "invalid_format")
    print(response)
    assert "IoT" in response  # Falls back to plain text
def test_generate_roadmap():
    """Test roadmap generation for software engineer intermediate."""
    roadmap = generate_basic_roadmap("software engineer", "intermediate")

    print("\nGenerated Roadmap in Test:")
    for step in roadmap["roadmap"]:
        print(f"{step['stage']}: {step['task']}")

    
    assert "roadmap" in roadmap
    assert len(roadmap["roadmap"]) > 0
    assert any(stage["stage"] == "System Design Basics" for stage in roadmap["roadmap"])
    print(roadmap)
    