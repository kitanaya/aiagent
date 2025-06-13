import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) < 2:
        print("Need to provide a prompt!")
        sys.exit(1)    
    else:
        prompt = client.models.generate_content(model="gemini-2.0-flash-001", contents=sys.argv[1])
        
    print(f"Prompt tokens: {prompt.usage_metadata.prompt_token_count}\nResponse tokens: {prompt.usage_metadata.candidates_token_count}")
    print(prompt.text)

if __name__ == "__main__":
    main()