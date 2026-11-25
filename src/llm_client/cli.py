import sys
import argparse

from llm_client.client import OllamaClient
from llm_client.client import DEFAULT_MODEL

AVAILABLE_MODELS = [DEFAULT_MODEL]
DEFAULT_SYSTEM_PROMPT = "You are a professor."
DEFAULT_TEMPERATURE = 0.7

parser = argparse.ArgumentParser(
    prog="llm cli client",
    description="chat with local llm client"
)

parser.add_argument('--model', '-m', help=f'Choose among the available models: {AVAILABLE_MODELS}', default=DEFAULT_MODEL, choices=AVAILABLE_MODELS)
parser.add_argument('--system_prompt', '-s', help=f'System prompt for the model', default=DEFAULT_SYSTEM_PROMPT)
parser.add_argument('--temperature', '-t', help=f'temperature for the model', default=DEFAULT_TEMPERATURE, type=float)
parser.add_argument('prompt', help="user prompt")
args = parser.parse_args()


def main():
    client = OllamaClient(model=args.model)
    result = client.chat(args.system_prompt, args.prompt, temperature=args.temperature)
    print(result)

if __name__ == "__main__":
    main()

