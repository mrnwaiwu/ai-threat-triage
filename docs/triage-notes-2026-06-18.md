# Triage Tuning Notes — 2026-06-18

Short notes on how the triage scoring behaves and how to read its output.

## Severity bands

The triage engine maps a raw model score (0.0–1.0) onto four bands:

| Band     | Score range | Suggested action                          |
|----------|-------------|-------------------------------------------|
| Critical | 0.90–1.00   | Page on-call immediately                  |
| High     | 0.70–0.89   | Open an incident ticket within the hour   |
| Medium   | 0.40–0.69   | Queue for same-day analyst review         |
| Low      | 0.00–0.39   | Auto-close with a logged rationale        |

## Reducing false positives

- Prefer raising the Medium/High boundary over disabling a rule outright.
- Re-check any rule that fires on more than 30% of events; that usually
  signals a noisy signal source rather than a real threat pattern.
- Keep an allowlist for known-good internal scanners so they do not inflate
  the High band during scheduled scans.

## Next review

Revisit these bands once a week against the previous week's closed alerts.
