from ultralytics import YOLO
import cv2
import serial
import time

THRESHOLD = 5.00

# Change to your Arduino port:
# Mac example: '/dev/tty.usbmodem14101'
# Windows example: 'COM3'
arduino = serial.Serial('/dev/tty.usbmodem1401', 9600, timeout=1)
time.sleep(2)  # let Arduino initialize

alert_triggered = False


# Load YOLOv8 model
model = YOLO("yolov8n.pt")
class_names = model.names
# print("List of labels (class names):")
# print(class_names)

# Price list
price_map = {
    "apple": 0.75,
    "banana": 0.54,
    "orange": 1.33,
    "bread": 2.80,
    "donut": 2.00,
    "cake": 15.00,
    "carrot": 2.50,
    "broccoli": 1.90,
    "pizza": 9.00,
    "hot dog": 5.00
}

# Open camera (1 = default webcam for Sams MacBook)
cap = cv2.VideoCapture(0)

# load lables to filter results
with open('labels.txt','r') as f:
    filterLabels = f.read().splitlines()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)

    total_price = 0.0  # RESET every frame

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = r.names[cls]

            if label in filterLabels and label in price_map:
                total_price += price_map[label]

            # Draw bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", 
                        (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
            
            # Trigger buzzer when threshold exceeded
            if total_price >= THRESHOLD and not alert_triggered:
                arduino.write(b'B')
                alert_triggered = True

            # Reset alert when price goes back down
            if total_price < THRESHOLD:
                alert_triggered = False


    # DISPLAY TOTAL PRICE ON SCREEN
    cv2.putText(frame, f"Total Price: ${total_price:.2f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3)

    cv2.imshow("YOLO Live Detection", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
