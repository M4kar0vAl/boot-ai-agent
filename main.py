import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("No api key found. Specify it in the OPENROUTER_API_KEY environment variable")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def generate_content(client: OpenAI, messages: list[dict]):
    return client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    verbose = args.verbose

    if verbose:
        print(f"User prompt: {args.user_prompt}")

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    response = generate_content(client, messages)


    if verbose:
        usage = response.usage

        if usage is None:
            raise RuntimeError("Cannot get the token usage. Probably, the request has failed")

        print(f"Prompt tokens: {usage.prompt_tokens}")
        print(f"Response tokens: {usage.completion_tokens}")

    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
