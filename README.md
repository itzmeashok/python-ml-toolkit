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

## Fun with different temperature 
> Higher temperature is more creative uses more different words, while the lower temperature repeats the same words. 
### 0.9
```
(test_llama) ashokkumarchandran@Mac python-ml-toolkit % python3 -m llm_client.cli "Tell me a holiday joke, office appropriate" --system_prompt "You are standup comedian" --model "llama3.2:3b" --temperature .9
"You know what's wild about the holidays? We spend the whole year telling our kids to be careful and respectful, and then on Christmas Day, we're like, 'Okay, now go ahead and trip on the tree and spill the eggnog.' It's like, we're setting them up for failure. 'Merry Christmas, kiddo! May your festive sweater be a little too tight and your sugar high be a little too high!' (laughs)"
(test_llama) ashokkumarchandran@Mac python-ml-toolkit % python3 -m llm_client.cli "Tell me a holiday joke, office appropriate" --system_prompt "You are standup comedian" --model "llama3.2:3b" --temperature .9
Here's one:

"You know what's wild about the holiday season? We spend all year telling our kids to 'be careful what they wish for.' And then on Christmas morning, we're like, 'Okay, what did you wish for again? Oh, you wanted a pair of socks? Well, here you go!'"
```
### 0.02
(test_llama) ashokkumarchandran@Mac python-ml-toolkit % python3 -m llm_client.cli "Tell me a holiday joke, office appropriate" --system_prompt "You are standup comedian" --model "llama3.2:3b" --temperature .02
Here's one:

"You know what's weird about the holiday season? We spend all year telling our kids to be good, and then on Christmas morning, we're like, 'Oh, you're good? Well, you're getting a 50-inch TV!' It's like, what's the deal with that? 'Be good, and you'll get a new TV... but also, be prepared to explain to your in-laws why you're watching Netflix at 3 PM on Christmas Day.'"
(test_llama) ashokkumarchandran@Mac python-ml-toolkit % python3 -m llm_client.cli "Tell me a holiday joke, office appropriate" --system_prompt "You are standup comedian" --model "llama3.2:3b" --temperature .02
Here's one:

"You know what's weird about the holiday season? We spend all year telling our kids to be good, and then on Christmas morning, we're like, 'Oh, you're good? Well, you're getting a 50-inch TV!' It's like, what's the deal with that? 'Be good, and you'll get a new TV... but also, be prepared to explain to your in-laws why you're watching Netflix at 3 PM on Christmas Day.'"
(test_llama) ashokkumarchandran@Mac python-ml-toolkit % python3 -m llm_client.cli "Tell me a holiday joke, office appropriate" --system_prompt "You are standup comedian" --model "llama3.2:3b" --temperature .02
Here's one:

"You know what's weird about the holiday season? We spend all year telling our kids to be good, and then on Christmas morning, we're like, 'Oh, you're good? Well, you're getting a 50-inch TV and a new bike!' It's like, 'Good' is just a code word for 'I'm not getting you a new bike'."
```

