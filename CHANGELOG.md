# Changelog

All notable changes to this project will be documented in this file.

## 2026-07-15 - Minor improvements

- Added lateral movement indicator scoring to correlate multi-hop alert chains across hosts
- Improved TAXII 2.1 collection polling to handle paginated results from large feeds
- Fixed memory leak in enrichment worker pool when processing oversized STIX objects
- Tuned low-confidence suppression window to avoid flooding queues during threat feed resets

## 2026-07-11 - Minor improvements

- Added enrichment caching layer to cut repeat IOC lookups against identical indicators
- Improved triage queue prioritization to surface critical alerts ahead of bulk feed ingest
- Fixed edge case where malformed STIX bundles aborted the full ingestion batch
- Tuned APT vs. commodity classifier weights to reduce misrouted mid-confidence alerts

## 2026-06-29 - Minor improvements

- Added behavioral clustering to group alerts by attacker TTPs across concurrent campaigns
- Improved sandbox detonation timeout handling to prevent pipeline stalls on evasive samples
- Fixed false-positive spike when scoring indicators from newly onboarded threat feeds
- Tuned MITRE ATT&CK sub-technique mapping to reduce ambiguous tactic assignments

## 2026-06-25 - Minor improvements

- Added geolocation enrichment for IP-based IOC lookups in the triage pipeline
- Improved alert batching to reduce downstream API calls during high-volume events
- Fixed scoring edge case for indicators with empty threat actor attribution fields
- Tuned confidence thresholds for low-fidelity threat feed sources

## 2026-06-18 - Minor improvements

- Added severity decay function to age out stale IOC matches over a configurable window
- Improved correlation between sandbox detonation results and static triage scores
- Fixed race condition when enriching alerts from concurrent threat feed pollers
- Tuned APT classifier thresholds to reduce noise from commodity malware signatures

## 2026-06-15 - Minor improvements

- Added YARA rule integration for binary-level threat classification
- Improved ML model recall for low-volume APT indicator detection
- Fixed false-negative edge case in domain reputation scoring for ccTLDs
- Added configurable alert suppression window for recurring benign patterns

## 2026-06-04 - Minor improvements

- Added support for multi-stage threat confidence aggregation
- Improved IOC enrichment pipeline to reduce lookup latency by ~18%
- Fixed edge case where unresolved hostnames caused triage pipeline to stall
- Refactored alert grouping logic for better cross-source correlation

## 2026-06-01 - Minor improvements

- Added confidence score field to triage output payload
- Improved enrichment pipeline to handle rate-limited external threat feeds
- Fixed bug where duplicate alerts were not correctly merged across sources
- Refactored scoring weights into configurable YAML file

## 2026-05-29 - Minor improvements

- Enhanced threat scoring algorithm with additional IOC indicators
- Added support for MITRE ATT&CK tactic classification in triage output
- Improved false-positive reduction logic for known-safe domains
- Updated threat category labels for consistency

## 2026-05-01 - Initial release

- Core AI-driven threat triage pipeline
- Integration with STIX/TAXII feeds
- Severity scoring (Critical / High / Medium / Low)
- Alert deduplication and grouping
