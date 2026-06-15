import json
from pathlib import Path
from typing import Any, Final

BASE_DIR: Final[Path] = Path(__file__).parent
CONFIG_PATH: Final[Path] = BASE_DIR / "robot_config.json"

def load_and_update_telemetry(sensor_name: str, new_frequency: float) -> None:
    try:
        with open(CONFIG_PATH, mode="r", encoding="utf-8") as file:
            config_data: dict[str, Any] = json.load(file)

    except FileNotFoundError:
        print(f"[WARNING] Config registry missing. Initializing default hardware profile at: {CONFIG_PATH.name}")
        config_data = {
            "device_id": "UR_ROBOT_01",
            "sensors": {
                "lidar": {"frequency": 10.0, "port": "/dev/ttyUSB0"},
                "camera": {"frequency": 30.0, "port": "/dev/video0"}
            }
        }

    except json.JSONDecodeError as decode_error:
        print(f"[CRITICAL] Corrupted JSON hardware profile. Parsing failed: {decode_error}")
        return

    else:
        print("[SUCCESS] Hardware configuration matrix successfully loaded into memory.")

    finally:
        print("[PIPELINE] Disk I/O operation sequence finished.")

    try:
        if sensor_name in config_data["sensors"]:
            config_data["sensors"][sensor_name]["frequency"] = new_frequency
            print(f"[REGISTERED] Sensor '{sensor_name}' operational rate updated to {new_frequency} Hz.")
        else:
            raise KeyError(f"Requested node '{sensor_name}' is absent in the hardware map.")

    except KeyError as key_error:
        print(f"[ERROR] Telemetry update aborted: {key_error}")
        return

    try:
        with open(CONFIG_PATH, mode="w", encoding="utf-8") as file:
            json.dump(config_data, file, indent=4)
        print("[SUCCESS] Hardware profile changes synchronized with non-volatile storage.")
    except IOError as io_error:
        print(f"[CRITICAL] Failed to write telemetry updates to storage link: {io_error}")

if __name__ == "__main__":
    print("[START] Telemetry configuration subsystem online.")

    print("\n--- RUN 1: INITIALIZATION ---")
    load_and_update_telemetry(sensor_name="lidar", new_frequency=25.5)

    print("\n--- RUN 2: NORMAL UPDATE ---")
    load_and_update_telemetry(sensor_name="camera", new_frequency=60.0)

    print("\n--- RUN 3: EDGE CASE TESTING ---")
    load_and_update_telemetry(sensor_name="sonar", new_frequency=5.0)