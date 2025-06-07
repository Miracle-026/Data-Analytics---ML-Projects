import google.generativeai as genai

genai.configure(api_key="AIzaSyC35Zw4a5guVsnH-RzdFbbJ61eqvzXgjSQ")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

prompt = input(str("Enter your prompt: "))	
response = model.generate_content(prompt)

print(response.text) 