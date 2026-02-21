import cv2
from ultralytics import YOLO
import cvzone

# Load Pre-trained YOLOv8 model
model = YOLO("yolov8n.pt") 

# Open Video (Replace with 0 for webcam or 'traffic.mp4')
cap = cv2.VideoCapture(r"C:\Users\Pramod\Downloads\traffic_video.mp4")

# Defined Classes for vehicles in COCO dataset
vehicle_classes = [2, 3, 5, 7] # car, motorcycle, bus, truck

while True:
    success, img = cap.read()
    if not success: break

    results = model(img, stream=True)
    count = 0

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            if cls in vehicle_classes:
                # Draw bounding box
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                count += 1

    # Logic for Dynamic Timing
    base_time = 30 # standard 30 sec
    if count > 15:
        signal_time = base_time + 20
        status = "HEAVY TRAFFIC"
    elif count > 5:
        signal_time = base_time + 10
        status = "MODERATE TRAFFIC"
    else:
        signal_time = base_time
        status = "LOW TRAFFIC"

    # Overlay Info
    cvzone.putTextRect(img, f'Count: {count} - {status}', (50, 50))
    cvzone.putTextRect(img, f'Signal Duration: {signal_time}s', (50, 100))

    cv2.imshow("Smart Traffic System", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()