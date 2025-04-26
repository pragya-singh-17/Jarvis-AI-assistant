import google.generativeai as genai
from config import apiKey

# Configure your API key
genai.configure(api_key=apiKey)

# Choose a Gemini model (e.g., 'gemini-2.0-flash')
model = genai.GenerativeModel('gemini-2.0-flash')

# Send a request
response = model.generate_content("Explain how AI works in a few words")

# Print the response
print(response.text)