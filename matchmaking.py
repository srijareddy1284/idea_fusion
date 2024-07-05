import json
import os

class Implementor:
    def __init__(self, fullName, email, phone, skills, experience, availability, portfolio="N/A", onlineProfiles="N/A", projectPreferences="N/A", communicationChannels="N/A", expectations="N/A", compensation="0"):
        self.full_name = fullName
        self.email = email
        self.phone = phone
        self.skills = skills
        self.experience = experience
        self.availability = availability
        self.portfolio = portfolio
        self.online_profiles = onlineProfiles
        self.project_preferences = projectPreferences
        self.communication_channels = communicationChannels
        self.expectations = expectations
        try:
            self.compensation = int(compensation)  # Convert compensation to integer
        except ValueError:
            self.compensation = 0  # Default value if conversion fails

    def __str__(self):
        return f"Implementor: {self.full_name}"

class Innovator:
    def __init__(self, projectName, projectDescription, skillsNeeded):
        self.project_name = projectName
        self.project_description = projectDescription
        self.skills_needed = skillsNeeded

    def __str__(self):
        return f"Innovator: {self.project_name}"

def load_implementors(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [Implementor(**item) for item in data]

def load_innovators(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [Innovator(**item) for item in data]

def match(implementors, innovators):
    matches = []

    for innovator in innovators:
        best_match = None
        best_score = 0

        for implementor in implementors:
            score = 0

            if innovator.skills_needed in implementor.skills:
                score += 1

            if innovator.skills_needed in implementor.project_preferences:
                score += 1

            if implementor.compensation <= 200000:  # Assuming a threshold compensation value for simplicity
                score += 1

            if score > best_score:
                best_score = score
                best_match = implementor

        if best_match:
            matches.append((innovator, best_match))

    return matches

def create_html(matches, file_path):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Matchmaking Results</title>
    </head>
    <body>
        <h1>Matchmaking Results</h1>
        <ul>
    """
    for innovator, implementor in matches:
        html_content += f"<li>{innovator} is matched with {implementor}</li>"
    
    html_content += """
        </ul>
    </body>
    </html>
    """

    with open(file_path, 'w') as file:
        file.write(html_content)

# Assuming JSON files are in the same directory as the script
current_dir = os.path.dirname(os.path.abspath(__file__))
implementor_file = os.path.join(current_dir, 'implementor.json')
innovator_file = os.path.join(current_dir, 'innovator.json')
output_html_file = os.path.join(current_dir, 'matchmaking_results.html')

# Load implementors and innovators from JSON files
implementors = load_implementors(implementor_file)
innovators = load_innovators(innovator_file)

# Perform matchmaking
matches = match(implementors, innovators)

# Create HTML file with matches
create_html(matches, output_html_file)

print(f"Matchmaking results have been written to {output_html_file}")
