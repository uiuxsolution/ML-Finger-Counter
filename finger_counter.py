import cv2
import mediapipe as mp
import time

# Initialize MediaPipe solutions
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection

# Initialize hand and face detection models
hands = mp_hands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.7,
                      min_tracking_confidence=0.5)
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Initialize webcam
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]  # Index of fingertips (except thumb)
    thumb_tip = 4
    finger_count = 0
    
    # Check thumb (comparing with thumb base)
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x:
        finger_count += 1
    
    # Check other fingers
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            finger_count += 1
            
    return finger_count

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame")
        break
        
    # Flip the image horizontally for selfie-view and convert to RGB
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Process hands
    hand_results = hands.process(imgRGB)
    
    # Process face detection
    face_results = face_detection.process(imgRGB)
    
    # Draw face detection box
    if face_results.detections:
        for detection in face_results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (0, 255, 0), 2)
    
    # Process hand landmarks and count fingers
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Count fingers
            fingers = count_fingers(hand_landmarks)
            
            # Display finger count
            cv2.putText(img, f'Fingers: {fingers}', (10, 70),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    # Display the image
    cv2.imshow("Finger Counter", img)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()