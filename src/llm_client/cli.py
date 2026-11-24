import sys

from llm_client.client import OllamaClient

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m llm_client.cli \"your prompt\"")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    client = OllamaClient()
    result = client.chat("You are a professor.", prompt)
    print(result)

if __name__ == "__main__":
    main()

