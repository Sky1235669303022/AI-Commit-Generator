import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS  # This is the new import

# Set up your Flask app
app = Flask(__name__)
CORS(app)

# Configure the Gemini API with your key
# IMPORTANT: Never hardcode your key in the code.
# Use an environment variable for security.
# We will get this key from your terminal later.
GEMINI_API_KEY = "YOUR_NEW_API_KEY_HERE"
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=GEMINI_API_KEY)

@app.route('/generate_commit', methods=['POST'])
def generate_commit():
    try:
        data = request.get_json()
        code_diff = data.get('diff')

        if not code_diff:
            return jsonify({"error": "No code changes provided."}), 400

        # Create the prompt for Gemini
        prompt = f"""
        You are a Git commit message generator. Analyze the following code changes (diff) and generate a concise and descriptive commit message that follows the Conventional Commits format (type: message). The type should be one of "feat", "fix", "docs", "style", "refactor", "test", or "chore".

        Code changes:
        ---
        {code_diff}
        ---

        Commit message:
        """

        # Call the Gemini API
        model = genai.GenerativeModel('models/gemini-1.5-pro')
        response = model.generate_content(prompt)
        commit_message = response.text.strip()

        return jsonify({"commit_message": commit_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # The app will run on this port
    app.run(port=5000, debug=True)