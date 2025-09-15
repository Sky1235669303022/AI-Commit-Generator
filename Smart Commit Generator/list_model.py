import google.generativeai as genai

# Paste your API key here
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

try:
    print("Listing available models...")
    for model in genai.list_models():
        print(f"- {model.name}")
except Exception as e:
    print(f"Error: {e}")