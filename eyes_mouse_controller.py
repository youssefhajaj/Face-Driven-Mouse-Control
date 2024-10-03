import cv2
import mediapipe as mp
import pyautogui



def open_camera():
    
    cap = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)
        landmarks_points = results.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmarks_points:
            landmarks = landmarks_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x*frame_w)
                y = int(landmark.y*frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))

                if id == 1:
                    screen_x = screen_w/frame_w*x   
                    screen_y = screen_h/frame_h*y
                    pyautogui.moveTo(screen_x, screen_y)
                    
            left_eye = [landmarks[145], landmarks[159]]
            for landmark in left_eye:
                x = int(landmark.x*frame_w)
                y = int(landmark.y*frame_h)
                cv2.circle(frame, (x, y), 3, (0, 0, 255))
            
            if (left_eye[0].y - left_eye[1].y) < 0.01:
                pyautogui.click()
                pyautogui.sleep(1)
        

        
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

open_camera()
