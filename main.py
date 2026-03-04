import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    while True:
        success, frame = cap.read()

        # If frame not received, skip this iteration
        if not success or frame is None:
            print("Warning: Failed to grab frame.")
            continue

        # Mirror image
        frame = cv2.flip(frame, 1)

        # Convert BGR → RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False

        # Process frame
        res = hands.process(rgb_frame)

        rgb_frame.flags.writeable = True

        # Get frame dimensions
        h, w, c = frame.shape

        if res.multi_hand_landmarks: # res.multi_hand_landmarks = [hand1, hand2]  list detected hands 
            for idx, hand_landmark in enumerate(res.multi_hand_landmarks):

                # Left or Right hand
                label = res.multi_handedness[idx].classification[0].label

                # Store landmarks
                lm_list = []
                for id, lm in enumerate(hand_landmark.landmark):   #     id → point number (0 to 20) , lm → actual landmark
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append((id, cx, cy))

                fingers = []

                # Thumb (X-axis)
                if label == "Right":
                    fingers.append(1 if lm_list[4][1] > lm_list[3][1] else 0)  # 4,3- landmark id ,   4 → thumb tip , 3 → thumb joint below it
                else:
                    fingers.append(1 if lm_list[4][1] < lm_list[3][1] else 0) # 1- up , 0- down 

                # Other fingers (Y-axis)
                tips = [8, 12, 16, 20]
                for tip in tips:
                    fingers.append(1 if lm_list[tip][2] < lm_list[tip - 2][2] else 0) # did tip-2 to get joint id 

                total_fingers = sum(fingers)

                # Draw landmarks
                mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

                # Display text
                y_offset = idx * 100

                cv2.putText(frame, f'{label} Hand',
                            (10, 50 + y_offset),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                cv2.putText(frame, f'Fingers: {total_fingers}',
                            (10, 90 + y_offset),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Show output
        cv2.imshow("Hand Detection", frame)

        # Exit on ESC key
        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()
