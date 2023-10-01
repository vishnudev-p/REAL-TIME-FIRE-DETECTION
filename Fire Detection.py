import cv2        
import threading   
import pygame

# Initialize pygame mixer for playing sound
pygame.init()
pygame.mixer.init()

fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml') 
vid = cv2.VideoCapture(0) 

def play_alarm_sound():
    pygame.mixer.music.load("mixkit-emergency-alert-alarm-1007.wav")
    pygame.mixer.music.play()

while True:
    ret, frame = vid.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x-20, y-20), (x+w+20, y+h+20), (255, 0, 0), 2)
        cv2.putText(frame, "Fire Detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        print("Fire alarm initiated")
        play_alarm_sound()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
