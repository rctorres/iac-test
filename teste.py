import requests
import os


API_TOKEN = os.environ['RENDER_API_KEY']
BLUEPRINT_FILE_PATH = "./render.yaml"
API_BASE_URL = "https://api.render.com/v1"

# Function to upload the blueprint file
def upload_blueprint(file_path):
    url = f"{API_BASE_URL}/blueprints"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    with open(file_path, "r") as file:
        blueprint_data = file.read()
    
    response = requests.post(url, headers=headers, json={"blueprint": blueprint_data})
    if response.status_code == 201:
        blueprint_id = response.json()["id"]
        print(f"Blueprint uploaded successfully. ID: {blueprint_id}")
        return blueprint_id
    else:
        print(f"Failed to upload blueprint: {response.text}")
        return None

# Function to apply the uploaded blueprint
def apply_blueprint(blueprint_id):
    url = f"{API_BASE_URL}/blueprints/{blueprint_id}/apply"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print("Blueprint applied successfully.")
        print(response.json())
    else:
        print(f"Failed to apply blueprint: {response.text}")

# Main function
if __name__ == "__main__":
    # Check if the blueprint file exists
    if not os.path.exists(BLUEPRINT_FILE_PATH):
        print(f"Blueprint file not found: {BLUEPRINT_FILE_PATH}")
    else:
        # Upload the blueprint and apply it
        blueprint_id = upload_blueprint(BLUEPRINT_FILE_PATH)
        # if blueprint_id:
        #     apply_blueprint(blueprint_id)