from functools import lru_cache
from backend.gemini_helper import generate_response

# Cache responses to reduce duplicate API calls.
# Caches responses for role, experience, and level to avoid unnecessary API calls.
@lru_cache(maxsize=50)
def cache_response(role, experience, level, format_type="markdown"):
    """
    Cache API response for specific role, experience, and level.

    Args:
        role (str): Role (e.g., technical, non-technical).
        experience (int): Years of experience.
        level (str): Level of expertise (e.g., beginner, intermediate, advanced).
        format_type (str): Response format (markdown/html).
    
    Returns:
        str: Formatted AI response or cached version.
    """
    prompt = generate_prompt(role, experience, level)
    response = generate_response(prompt, format_type)
    return response


def generate_prompt(role, experience, level):
    """
    Generate a prompt string for API request based on role, experience, and level.

    Args:
        role (str): Role (e.g., technical, non-technical).
        experience (int): Years of experience.
        level (str): Level of expertise.

    Returns:
        str: Generated prompt string.
    """
    return f"Create a {level} interview roadmap for a {role} professional with {experience} years of experience."


def format_response(response_text, format_type="markdown"):
    """
    Format the raw response text from the API.
    This function can add HTML/Markdown formatting or cleanup as needed.

    Args:
        response_text (str): Raw API response text.
        format_type (str): Format type (markdown/html).

    Returns:
        str: Formatted response.
    """
    paragraphs = response_text.split("\n")

    if format_type == "html":
        formatted = "".join(f"<p>{p}</p>" for p in paragraphs if p.strip())
    elif format_type == "markdown":
        formatted = "\n\n".join(f"- {p}" for p in paragraphs if p.strip())
    else:
        formatted = response_text

    return formatted


def handle_api_error(error):
    """
    Handle API errors and return a fallback message.

    Args:
        error (Exception): API error or exception.

    Returns:
        str: Fallback error message.
    """
    return f"An error occurred while generating the response: {str(error)}"
