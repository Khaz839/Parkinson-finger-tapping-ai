import cv2

# Placeholder example for frame extraction

video_path = "sample_video.mp4"

cap = cv2.VideoCapture(video_path)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Example: display frame (in real case, used for processing)
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    frame_count += 1

cap.release()
cv2.destroyAllWindows()

print(f"Total frames processed: {frame_count}")
