"""
ai-threat-triage
-----------------
Uses OpenAI to analyze security log entries and classify threats.
Replace OPENAI_API_KEY with your key or load from environment.
"""

import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a senior cybersecurity analyst. Given a raw security log entry,
classify it into one of these threat levels:
  - CRITICAL: Immediate action required (e.g., active exploit, data exfil)
  - HIGH: Likely malicious, investigate within 1 hour
  - MEDIUM: Suspicious, investigate within 24 hours
  - LOW: Informational, log for review
  - BENIGN: Normal activity

Respond in JSON with keys: threat_level, summary, recommended_action.
"""


def analyze_log(log_entry: str) -> dict:
    """Send a log entry to GPT and return a structured threat assessment."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Log entry:\n{log_entry}"},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


def triage_logs(log_file: str) -> None:
    """Read logs from a file and print triage results."""
    with open(log_file, "r") as f:
        logs = [line.strip() for line in f if line.strip()]

    print(f"\nAnalyzing {len(logs)} log entries...\n{'='*60}")
    for i, entry in enumerate(logs, 1):
        result = analyze_log(entry)
        print(f"\n[{i}] LOG: {entry[:80]}...")
        print(f"    Threat Level : {result.get('threat_level')}")
        print(f"    Summary      : {result.get('summary')}")
        print(f"    Action       : {result.get('recommended_action')}")


if __name__ == "__main__":
    sample_logs = [
        "2024-03-01 02:14:33 FAILED SSH login root@192.168.1.105 attempt 47",
        "2024-03-01 02:15:01 User admin downloaded 4.2GB from /sensitive/payroll",
        "2024-03-01 08:00:10 User jdoe logged in successfully from 10.0.0.22",
        "2024-03-01 03:44:55 Outbound connection to known C2 IP 45.33.32.156:4444",
    ]

    print("AI Threat Triage Tool")
    print("=" * 60)
    for i, log in enumerate(sample_logs, 1):
        result = analyze_log(log)
        print(f"\n[{i}] LOG: {log}")
        print(f"    Threat Level : {result.get('threat_level')}")
        print(f"    Summary      : {result.get('summary')}")
        print(f"    Action       : {result.get('recommended_action')}")
