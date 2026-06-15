# Changelog

All notable changes to this project will be documented in this file.

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
