python
Copy code
import requests

# Backend URL
BASE_URL = 'http://127.0.0.1:5000'

# Step 1: Generate Ideas
response = requests.post(f'{BASE_URL}/generate_ideas', json={"query": "What new app should I build?"})
if response.status_code == 200:
    ideas = response.json().get('ideas', [])
    print("Here are 3 ideas:")
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea}")
else:
    print("Error generating ideas:", response.json().get('error'))

# Step 2: User selects ideas
selection = input("Select 2 ideas by numbers (e.g., 1, 3): ").split(',')
selected_ideas = [ideas[int(num.strip()) - 1] for num in selection]

# Step 3: Expand on selected ideas
response = requests.post(f'{BASE_URL}/expand_ideas', json={"selected": selected_ideas})
if response.status_code == 200:
    details = response.json().get('details', [])
    for i, detail in enumerate(details, 1):
        print(f"\nDetails for Idea {i}:\n{detail}")
else:
    print("Error expanding ideas:", response.json().get('error'))
