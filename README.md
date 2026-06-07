# Smart Flood Risk Monitoring System

## Overview

This project is an Edge AI-inspired flood monitoring system that combines simulated water level sensor data with debris detection results. The system performs heterogeneous data fusion, evaluates flood risk, and generates alerts when dangerous conditions are detected.

The project integrates concepts from Edge AI, Multi-threaded Processing, Data Fusion, and Cloud Communication.

---

## Objectives

* Simulate water level monitoring
* Simulate debris detection
* Fuse heterogeneous data streams
* Assess flood risk levels
* Generate alerts
* Store monitoring records in JSON format

---

## System Architecture

```text
Water Sensor Simulation
        |
        v
Debris Detection Simulation
        |
        v
Data Fusion Engine
        |
        v
Risk Assessment Module
        |
        v
Alert Generation
        |
        v
JSON Logging (local.jsonl)
```

---

## Risk Assessment Logic

### LOW Risk

* Water level ≤ 3.0 m

### MEDIUM Risk

* Water level > 3.0 m

### HIGH Risk

* Water level > 4.0 m and debris count > 5

---

## Sample Output

```json
{
  "water_level": 4.88,
  "debris_count": 9,
  "risk_level": "HIGH",
  "alert": true
}
```

---

## Results

The system successfully:

* Generated simulated water level measurements
* Generated debris detection events
* Performed heterogeneous data fusion
* Classified flood risk levels
* Generated alert notifications
* Logged monitoring data into local.jsonl

---

## Technologies Used

* Python
* NumPy
* JSON
* Queue
* Threading
* MQTT Communication Strategy

---

## Future Improvements

* Real YOLOv10 object detection
* Real ultrasonic water sensor integration
* MQTT cloud dashboard
* Live monitoring interface

---

## Author

Poorna Chandra Kumar Penubarthi (強度)

Student ID: 614785169

Master's Program, Tamkang University
