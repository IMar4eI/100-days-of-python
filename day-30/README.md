# Day 30: Robot Config Manager - Exception Hierarchies & JSON Serialization 

This repository contains the final Day 30 foundational module from the "100 Days of Code" challenge. 

## Technical Specifications
The system manages system profiles using atomic validation checks and robust file stream exception boundaries.

* **Exception Hierarchy Trees:** Employs explicit `try-except-else-finally` architecture models to prevent process crashes during telemetry read pipeline faults.
* **Deterministic Object Serialization:** Utilizes native JSON encoders (`json.load()`, `json.dump()`) to map data dictionaries directly into configuration assets.
* **Custom Error Injections:** Integrates conditional `raise KeyError` triggers to enforce strict validation mapping across hardware sensor maps.

## Execution
```bash
python3 config_manager.py