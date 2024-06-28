import cv2
import numpy as np
import pyttsx3

def detect_color(hsv, color_ranges):
    detected_color_name = "Unknown"
    
    # Iterate through the color ranges
    for color_name, (lower, upper) in color_ranges.items():
        # Check if HSV values are within the current color range
        if lower[0] <= hsv[0] <= upper[0] and lower[1] <= hsv[1] <= upper[1] and lower[2] <= hsv[2] <= upper[2]:
            detected_color_name = color_name
            break
    
    return detected_color_name

engine = pyttsx3.init()

color_ranges = {
    "red": ([0, 120, 70], [10, 255, 255]),
    "green": ([35, 100, 100], [90, 255, 255]),
    "blue": ([100, 100, 100], [140, 255, 255]),
    "yellow": ([20, 100, 100], [30, 255, 255]),
    "orange": ([10, 100, 100], [20, 255, 255]),
    "purple": ([140, 50, 50], [170, 255, 255]),
    "pink": ([150, 50, 50], [170, 255, 255]),
    "cyan": ([85, 100, 100], [110, 255, 255]),
    "gray": ([0, 0, 0], [179, 60, 150]),  
    
}

cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Resize frame for faster processing (optional)
    frame = cv2.resize(frame, (640, 480))
    
    # Convert BGR frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Detect color in the current frame
    detected_color_name = detect_color(hsv[240, 320], color_ranges)  # Sample point at center of frame (240, 320)
    
    # Display the detected color name on the frame
    cv2.putText(frame, f"Detected Color: {detected_color_name.capitalize()}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow("Color Detection", frame)
    
    # Announce the detected color using text-to-speech
    engine.say(f"Detected Color: {detected_color_name.capitalize()}")
    engine.runAndWait()
    
    # Exit condition: press 'Esc' key to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
