#!/~/projects/master_project/.venv3.6/bin/python3.6

import cv2

# Open a connection to the webcam (0 represents the default webcam)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open webcam.")
    exit()

# Set the video capture properties (optional)
# You can set properties like width, height, and frame rate using cap.set(property, value)
# For example: cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#             cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Loop to continuously capture frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Couldn't read frame.")
        break

    # Display the captured frame
    cv2.imshow('Webcam Capture', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
