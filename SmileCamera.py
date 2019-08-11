import cv2
import os
import time

#function



#Print Messages

def printm(text):

    #font
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,text,(100,100), font, 1, (0,0,0), 3, cv2.LINE_AA)

#Capture Function

def PM():
    print(" 3 ")
    #time.sleep(2)
    print(" 2 ")
    
    print(" 1 ")
    #time.sleep(2)
    printm(" Capturing ")
    printm("  ")
    

    
def capture():
    print("Smile Detected")
    PM()
    
    print("Executed")
    





#classifiers

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
smile=cv2.CascadeClassifier('haarcascade_smile.xml')


cap=cv2.VideoCapture(0)
c=0
while (True and c==0) :
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    for (fx,fy,fw,fh) in face:
        roi_gray = gray[fy:fy+fh, fx:fx+fw] 
        roi_color = img[fy:fy+fh, fx:fx+fw]         
        smiles=smile.detectMultiScale(roi_gray)
        for (sx,sy,sw,sh) in smiles:
            capture()
            cv2.imwrite("SMILE.jpg",img)
            break
        break
            

    cv2.imshow('Camera',img)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cv2.imshow('IMAGE',img)
#cap.release()
#cv2.destroyAllWindows()
