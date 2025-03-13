python 
Copy code
from flask import Flask, request, jsonify, render_template, request, redirect, url_for, session
import os
import openai

# Initialize Flask app
app = Flask(__name__)

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Route to generate ideas
@app.route('/generate_ideas', methods=['POST'])
def generate_ideas():
    query = request.json.get('query', 'What new app should I build?')
    
    # Generate ideas using OpenAI API
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Generate 3 unique app ideas based on the query: {query}",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        ideas = response.choices[0].text.strip().split('\n')
        ideas = [idea.strip() for idea in ideas if idea.strip()]
        return jsonify({"ideas": ideas[:3]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to expand on selected ideas
@app.route('/expand_ideas', methods=['POST'])
def expand_ideas():
    selected = request.json.get('selected', [])
    details = []
    for idea in selected:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Expand on this idea: {idea}. Provide detailed suggestions and features.",
            max_tokens=200,
            temperature=0.7,
        )
        details.append(response.choices[0].text.strip())
    return jsonify({"details": details}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
