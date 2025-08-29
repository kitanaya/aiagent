import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERATIONS

# poe2 0.3 release

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print('Usage: uv run main.py "your prompt here [--verbose]"')
        print('\nExample: uv run main.py "Name the top three cyber security jobs."')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    if verbose:
        print(f"User prompt: {user_prompt}\n")


    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    for i in range(MAX_ITERATIONS):
        try:
            response = client.models.generate_content(
                model = 'gemini-2.0-flash-001',
                contents = messages,
                config = types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt),
            )

            if verbose:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            
            for candidate in response.candidates:
                messages.append(candidate.content)

            if not response.function_calls:
                if verbose:
                    print("Final response:")
                print(response.text)
                return response.text
            
            function_responses = []
            for function_call_part in response.function_calls:
                if verbose:
                    print(f"Calling function: {function_call_part.name}({function_call_part.args})")

                function_call_result = call_function(function_call_part, verbose)
                if(
                    not function_call_result.parts
                    or not function_call_result.parts[0].function_response
                ):
                    raise Exception("empty function call result")
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                function_responses.append(function_call_result.parts[0])

            if function_responses:
                 total_output_content = types.Content(role="user", parts=function_responses)
                 messages.append(total_output_content)
            else:
                raise Exception("no function responses generated, exiting.")
            
        except Exception as e:
            print(f"Error during iteration {i+1}: {e}")
            break

    print(f"Max iterations({MAX_ITERATIONS}) reached without a final response.")
    if messages and messages[-1].parts[0].text:
        return messages[-1].parts[0].text
    return "Agent could not complete the task within the given iterations."

if __name__ == "__main__":
    main()
