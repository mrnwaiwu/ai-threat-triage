# ai-threat-triage

AI-powered security log analyzer. Paste in raw log entries and get instant threat classifications powered by GPT-4o.

## What it does
- Reads log entries (file or inline)
- Sends each entry to OpenAI for analysis
- Returns: threat level, plain-English summary, and recommended action

## Setup
```bash
pip install openai
export OPENAI_API_KEY=your_key_here
python main.py
```

## Tech Stack
Python · OpenAI API · JSON
