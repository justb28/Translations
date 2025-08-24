import numpy as np
import cv2

#you should change your directories for these files
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
cap = cv2.VideoCapture(0)

z = 0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #this loop is to draw the squares around the faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        smile = smile_cascade.detectMultiScale(roi_gray)
	#this loop is to draw the squares around the eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            z = ey
        
	#this loop is to draw the squares around the smiles
        for (sx,sy,sw,sh) in smile:
            if(z + 40 < sy):
                cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    #click escape on your keyboard if you want to stop the program 
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()