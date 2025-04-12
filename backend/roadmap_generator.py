import json
import os

# Load roadmap templates from JSON
ROADMAP_FILE = os.path.join(os.path.dirname(__file__), "../data/roadmap_templates.json")

def load_roadmap_templates():
    """Load roadmap templates from a JSON file."""
    with open(ROADMAP_FILE, "r") as file:
        return json.load(file)

def generate_basic_roadmap(role, experience):
    """
    Generate a basic interview preparation roadmap based on role and experience.

    Args:
    - role (str): The job role (e.g., "software engineer", "data scientist").
    - experience (str): The experience level (e.g., "beginner", "intermediate", "advanced").

    Returns:
    - dict: Structured roadmap with stages and tasks.
    """

    # Load roadmap template
    roadmap_template = load_roadmap_templates()

    # Get role-specific roadmap based on role and experience
    role_steps = roadmap_template.get(role.lower(), {}).get(experience.lower(), [])

    if not role_steps:
        return {"error": f"No roadmap available for {role} at {experience} level."}

    # Return the role-specific steps
    return {"roadmap": role_steps}
