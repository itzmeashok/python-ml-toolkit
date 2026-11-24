import httpx

DEFAULT_ENDPOINT = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "llama3.2:3b"

class OllamaClient:
    def __init__(self, model: str = DEFAULT_MODEL, endpoint: str = DEFAULT_ENDPOINT):
        self.model = model
        self.endpoint = endpoint

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
        }
        response = httpx.post(self.endpoint, json=body, timeout=httpx.Timeout(120.0))
        response.raise_for_status()
        return response.json()["message"]["content"]


