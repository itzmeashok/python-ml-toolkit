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

## Testing
```bash
python3 -m pytest
```
