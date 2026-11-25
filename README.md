# Python ML Toolkit

Daily learning project — one concept per checkin.

## Setup

### 1. Install Ollama (macOS)

Download from: https://ollama.com/download

### 2. Pull a model

```bash
ollama pull llama3.2:3b   
```

### 3. Verify it runs
```bash
ollama run llama3.2:3b
```

### 4. Install Python dependencies
```bash
pip3 install -r requirements.txt
```

OR

```bash
pip3 install -e .
```

## Usage
```bash
python3 -m llm_client.cli "Your prompt here"
```

The system prompt, temperature and model can be passed to the cli client. These are optional values. 
```bash
python3 -m llm_client.cli "Write a poem" --system_prompt "You are a lyric writer" --model "llama3.2:3b"
```
```bash
python3 -m llm_client.cli "How to replace a three way switch" --system_prompt "You are the best handyman" --model "llama3.2:3b
```
```bash
python3 -m llm_client.cli "why do birds migrate?" --system_prompt "You are zoologist" --model "llama3.2:3b" --temperature .02
```
## Testing
```bash
python3 -m pytest
```
