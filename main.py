import time
import threading
import queue
import json
import random

sensor_queue = queue.Queue(maxsize=50)
vision_queue = queue.Queue(maxsize=1)
stop_event = threading.Event()

def sensor_producer():
    while not stop_event.is_set():
        data = {
            "ts": time.time(),
            "water_level": round(random.uniform(2.0, 5.0), 2)
        }

        try:
            sensor_queue.put_nowait(data)
        except queue.Full:
            sensor_queue.get_nowait()
            sensor_queue.put_nowait(data)

        time.sleep(0.05)

def vision_producer():
    while not stop_event.is_set():
        data = {
            "ts": time.time(),
            "debris_count": random.randint(0, 10)
        }

        try:
            vision_queue.put_nowait(data)
        except queue.Full:
            vision_queue.get_nowait()
            vision_queue.put_nowait(data)

        time.sleep(0.25)

def assess_risk(water_level, debris_count):
    if water_level > 4.0 and debris_count > 5:
        return "HIGH", True
    elif water_level > 3.0:
        return "MEDIUM", False
    else:
        return "LOW", False

def save_payload(payload):
    with open("local.jsonl", "a") as f:
        f.write(json.dumps(payload) + "\n")

if __name__ == "__main__":

    threading.Thread(target=sensor_producer, daemon=True).start()
    threading.Thread(target=vision_producer, daemon=True).start()

    print("Smart Flood Risk Monitoring System Started")

    try:
        while True:

            vis = vision_queue.get()

            best_match = None
            min_diff = 1.0

            while not sensor_queue.empty():
                sensor = sensor_queue.get()

                diff = abs(vis["ts"] - sensor["ts"])

                if diff < min_diff:
                    min_diff = diff
                    best_match = sensor

            if best_match and min_diff < 0.1:

                risk_level, alert = assess_risk(
                    best_match["water_level"],
                    vis["debris_count"]
                )

                payload = {
                    "timestamp": round(vis["ts"], 2),
                    "water_level": best_match["water_level"],
                    "debris_count": vis["debris_count"],
                    "risk_level": risk_level,
                    "alert": alert,
                    "sync_error_ms": round(min_diff * 1000, 2)
                }

                print(payload)

                save_payload(payload)

            time.sleep(0.1)

    except KeyboardInterrupt:
        stop_event.set()
        print("System Stopped")