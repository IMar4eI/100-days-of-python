from typing import Any

def process_sensor_stream(*args: float, **kwargs: Any) -> None:

    print("--- STARTING VECTOR PARSING ---")
    for index, coordinate in enumerate(args):
        print(f"[STREAM] Sensor axis {index} data point: {coordinate}")

    if "device_id" in kwargs:
        print(f"[CONFIG] Target hardware address: {kwargs['device_id']}")
    if "verbose" in kwargs and kwargs['verbose'] is True:
        print("[DEBUG] Extended telemetry logging activated.")
    print("--- STREAM PROCESSING COMPLETE ---")

if __name__ == "__main__":
    process_sensor_stream(12.4, -5.8, 104.2, device_id="LIDAR_01", verbose=True)
    process_sensor_stream(0.0, 1.5, device_id="CAMERA_TOP")