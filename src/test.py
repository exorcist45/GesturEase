import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


response = model.generate_content("What is the meaning of life?", stream = True)

for chunk in response:
    print(chunk.text)
    #print("_"*80)