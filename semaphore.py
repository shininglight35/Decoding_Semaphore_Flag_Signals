import cv2
import mediapipe as mp
import math
import time

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    a = [a.x, a.y]
    b = [b.x, b.y]
    c = [c.x, c.y]
    
    ba = [a[0] - b[0], a[1] - b[1]]
    bc = [c[0] - b[0], c[1] - b[1]]
    
    dot_product = ba[0] * bc[0] + ba[1] * bc[1]
    magnitude_ba = math.sqrt(ba[0]**2 + ba[1]**2)
    magnitude_bc = math.sqrt(bc[0]**2 + bc[1]**2)
    
    angle = math.acos(dot_product / (magnitude_ba * magnitude_bc))
    cross_product = ba[0] * bc[1] - ba[1] * bc[0]
    if cross_product < 0:
        angle = -angle
    return math.degrees(angle)

cap = cv2.VideoCapture(0)
detected_sema4 = []
last_detection_time = 0
reset_detection_time = 0
gesture_delay = 2.5
z = "Letter"
count = 0
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Unable to read from the video feed.")
            break
        
        frame = cv2.flip(frame, 1)
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = pose.process(rgb_frame)
        current_time = time.time()
        
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            
            left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
            left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
            right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW]
            right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
            right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]
            
            left_shoulder_angle = calculate_angle(left_wrist, left_shoulder, left_hip)
            right_shoulder_angle = calculate_angle(right_wrist, right_shoulder, right_hip)
            left_arm_angle = calculate_angle(left_wrist, left_elbow, left_shoulder)
            right_arm_angle = calculate_angle(right_wrist, right_elbow, right_shoulder)
            
            h, w, _ = frame.shape
            
            if 170 < left_arm_angle < 180 or -170 > left_arm_angle > -180 and 170 < right_arm_angle < 180 or -170 > right_arm_angle > -180:
                if 35 < left_shoulder_angle < 55 and 0 > right_shoulder_angle > -20:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("A")
                        if z == "Number":
                            detected_sema4.append("1")
                        last_detection_time = current_time

                if 80 < left_shoulder_angle < 100 and 0 > right_shoulder_angle > -20:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("B")
                        if z == "Number":
                            detected_sema4.append("2")
                        last_detection_time = current_time

                if 125 < left_shoulder_angle < 145 and 0 > right_shoulder_angle > -20:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("C")
                        if z == "Number":
                            detected_sema4.append("3")
                        last_detection_time = current_time

                if 170 < abs(left_shoulder_angle) < 180 and 0 > right_shoulder_angle > -20:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("D")
                        if z == "Number":
                            detected_sema4.append("4")
                        last_detection_time = current_time

                if 0 < left_shoulder_angle < 20 and -125 > right_shoulder_angle > -145:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("E")
                        if z == "Number":
                            detected_sema4.append("5")
                        last_detection_time = current_time

                if 0 < left_shoulder_angle < 20 and -80 > right_shoulder_angle > -100:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("F")
                        if z == "Number":
                            detected_sema4.append("6")
                        last_detection_time = current_time

                if 0 < left_shoulder_angle < 20 and -35 > right_shoulder_angle > -55:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("G")
                        if z == "Number":
                            detected_sema4.append("7")
                        last_detection_time = current_time

                if 80 < left_shoulder_angle < 100 and 35 < right_shoulder_angle < 55:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("H")
                        if z == "Number":
                            detected_sema4.append("8")
                        last_detection_time = current_time

                if 125 < left_shoulder_angle < 145 and 35 < right_shoulder_angle < 55:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("I")
                        if z == "Number":
                            detected_sema4.append("9")
                        last_detection_time = current_time

                if 170 < abs(left_shoulder_angle) < 180 and -80 > right_shoulder_angle > -100:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("J")
                        if z == "Number":
                            detected_sema4.append("0")
                        last_detection_time = current_time

                if 35 < left_shoulder_angle < 55 and 170 < abs(right_shoulder_angle) < 180:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("K")
                        last_detection_time = current_time

                if 35 < left_shoulder_angle < 55 and -125 > right_shoulder_angle > -145:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("L")
                        last_detection_time = current_time

                if 35 < left_shoulder_angle < 55 and -80 > right_shoulder_angle > -100:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("M")
                        last_detection_time = current_time

                if 35 < left_shoulder_angle < 55 and -35 > right_shoulder_angle > -55:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("N")
                        last_detection_time = current_time

                if 125 < left_shoulder_angle < 145 and 80 < right_shoulder_angle < 100:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("O")
                        last_detection_time = current_time

                if 80 < left_shoulder_angle < 100 and 170 < abs(right_shoulder_angle) < 180:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("P")
                        last_detection_time = current_time

                if 80 < left_shoulder_angle < 100 and -125 > right_shoulder_angle > -145:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("Q")
                        last_detection_time = current_time

                if 80 < left_shoulder_angle < 100 and -80 > right_shoulder_angle > -100:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("R")
                        last_detection_time = current_time

                if 80 < left_shoulder_angle < 100 and -35 > right_shoulder_angle > -55:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("S")
                        last_detection_time = current_time

                if 125 < left_shoulder_angle < 145 and 170 < abs(right_shoulder_angle) < 180:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("T")
                        last_detection_time = current_time

                if 125 < left_shoulder_angle < 145 and -125 > right_shoulder_angle > -145:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("U")
                        last_detection_time = current_time

                if 170 < abs(left_shoulder_angle) < 180 and -35 > right_shoulder_angle > -55:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("V")
                        last_detection_time = current_time

                if -80 > left_shoulder_angle > -100 and -125 > right_shoulder_angle > -145:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("W")
                        last_detection_time = current_time

                if -35 > left_shoulder_angle > -55 and -125 > right_shoulder_angle > -145:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("X")
                        last_detection_time = current_time

                if 125 < left_shoulder_angle < 145 and -80 > right_shoulder_angle > -100:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("Y")
                        last_detection_time = current_time

                if -35 > left_shoulder_angle > -55 and -80 > right_shoulder_angle > -100:
                    if current_time - last_detection_time > gesture_delay:
                        if z == "Letter":
                            detected_sema4.append("Z")
                        last_detection_time = current_time

                if -10 < left_shoulder_angle < 0 and 0 < right_shoulder_angle < 10:
                    if current_time - last_detection_time > gesture_delay:
                        z = "Letter"
                        last_detection_time = current_time

                if 170 < abs(left_shoulder_angle) < 180 and -125 > right_shoulder_angle > -145:
                    if current_time - last_detection_time > gesture_delay:
                        z = "Number"
                        last_detection_time = current_time

                if 125 < left_shoulder_angle < 145 and -35 > right_shoulder_angle > -55:
                    if current_time - last_detection_time > gesture_delay:
                        detected_sema4.pop()
                        last_detection_time = current_time
                        
                if current_time - reset_detection_time > 0.5:
                    prev_left_ang = left_shoulder_angle
                    prev_right_ang = right_shoulder_angle
                    reset_detection_time = current_time

                if current_time - last_detection_time > gesture_delay:
                    if abs(prev_left_ang-left_shoulder_angle) >100 and abs(prev_right_ang-right_shoulder_angle) >100:
                        count = count + 1
                        if count == 4:
                            detected_sema4.clear()
                            count = 0
                            last_detection_time = current_time
               

        word = "".join(detected_sema4)
        cv2.putText(frame, f"OUTPUT: {word}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, f"Category: {z}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        resized_frame = cv2.resize(frame, (800, 600))
        cv2.imshow('Arm Values', resized_frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
