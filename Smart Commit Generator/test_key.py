import google.generativeai as genai

# Paste your API key here
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

try:
    model = genai.GenerativeModel('models/gemini-1.5-pro')
    response = model.generate_content("hello")
    print("Success! Your API key is working.")
    print("Response:", response.text)
except Exception as e:
    print("Error:", e)