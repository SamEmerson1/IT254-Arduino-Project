# IT254-Project  
## AI Shopping Cart – YOLO Price Detection & Arduino Alert System

---

## Overview

The AI Shopping Cart is a promotional supermarket prototype that allows customers to add items to their basket as long as the total remains under a fixed spending limit. A camera combined with AI-based object detection identifies items such as fruits, vegetables, and prepared foods as they appear in the cart. The system calculates a running total based on predefined prices and provides an audible alert when the limit is exceeded.

This project demonstrates the practical integration of computer vision, real-time data processing, and physical hardware feedback in a retail environment.

---

## Project Description

The system monitors a live camera feed and detects grocery items using a YOLOv8 model. As products enter or leave the frame, their associated prices are added or removed from the total. When the total passes the defined limit, an Arduino triggers a buzzer to notify the customer that the promotional threshold has been exceeded.

The goal is not perfect accuracy, but a responsive and interactive proof-of-concept for smart retail experiences.

---

## Core Features

- Real-time item recognition using AI and live video feed  
  - Detects items such as fruits, vegetables, and common grocery products  
- Dynamic price calculation based on detected objects  
- Live total displayed on the video stream  
- Enforced spending limit for promotional scenarios  
- Hardware alert system using Arduino and buzzer  
- Threshold-based warning to prevent overspending  

---

## System Requirements

### Hardware
- USB webcam (or compatible camera module)
- Arduino board (Uno, Nano, or similar)
- Buzzer or speaker
- USB cable connection between Arduino and computer

### Software & Libraries
Installed manually (no requirements file included):
- ultralytics  
- opencv-python  
- pyserial  

Install with:
```bash
pip install ultralytics opencv-python pyserial
````

---

## How It Works

1. The camera captures a continuous video feed.
2. YOLOv8 detects objects in each frame.
3. Only objects listed in `labels.txt` are processed.
4. Each detected item is matched to a price in the price map.
5. The combined total is calculated in real time.
6. If the total exceeds the defined threshold:
   * A signal is sent to the Arduino.
   * The buzzer plays an alert tone.

---

## Configuration

### Spending Threshold

Set inside the Python script:

```python
THRESHOLD = 5.00
```

### Pricing Data

Prices are defined directly in the `price_map` dictionary and represent estimated averages for demonstration purposes.

### Label Filtering

The `labels.txt` file determines which detected objects are eligible for pricing and tracking.

---

## File Structure

* main.py
  Core Python script handling detection, pricing, and Arduino communication
* labels.txt
  List of object labels that should be recognized and priced
* yolov8n.pt
  Pre-trained YOLO model weights
* Arduino Sketch
  Controls buzzer activation in response to serial commands

---

## Operational Flow

1. Launch the Python script.
2. Place items in the camera's field of view.
3. The system identifies items and updates the total.
4. When the price limit is exceeded, the buzzer activates.
5. Removing items lowers the total and resets the alert trigger.

---

## Notes

* Total price is recalculated each frame based on current detections.
* Items are counted only while visible in the frame.
* Persistent object tracking is not implemented.
* Designed as a demonstration system, not for commercial accuracy.

---

## Potential Enhancements

* Persistent object tracking to prevent duplicate counting
* Barcode or RFID integration for higher accuracy
* Dynamic pricing via database or API
* Multi-tier alerts for different price levels
* GUI control panel for threshold and pricing management
* Cloud-based analytics for user behavior tracking

---

## Use Case

This system simulates a promotional shopping environment where customers are encouraged to stay within a budget. It provides immediate feedback, creating an engaging and interactive retail experience while demonstrating how AI can support real-world automation scenarios.