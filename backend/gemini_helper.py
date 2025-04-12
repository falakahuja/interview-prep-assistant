import json
from dotenv import load_dotenv
import google.generativeai as genai
import os
from functools import lru_cache  # ✅ Import lru_cache

# Load environment variables
load_dotenv()

# Set up Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load roadmap templates
with open("data/roadmap_templates.json", "r") as file:
    ROADMAP_TEMPLATES = json.load(file)

@lru_cache(maxsize=100)
def cache_response(prompt, format_type="markdown"):
    """Cache AI responses for the same prompt and format type."""
    return generate_response(prompt, format_type)

def generate_response(prompt, format_type="markdown"):
    """Generate AI response using Gemini API and format it."""
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)

    # Format response based on user preference
    formatted_response = format_response(response.text, format_type)
    return formatted_response

def format_response(text, format_type="markdown"):
    """Format AI response to Markdown or HTML."""
    if format_type == "html":
        return f"<p>{text.replace('\n', '<br>')}</p>"
    elif format_type == "markdown":
        return f"**Response:**\n\n{text}"
    return text

def get_roadmap(role, experience):
    """Return roadmap based on role and experience level."""
    role = role.lower()
    experience = experience.lower()

    if role in ROADMAP_TEMPLATES and experience in ROADMAP_TEMPLATES[role]:
        return ROADMAP_TEMPLATES[role][experience]
    else:
        return [{"stage": "Error", "task": "Invalid role or experience level provided."}]
