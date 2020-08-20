import cv2

img = cv2.imread('fahmi.PNG')

face = cv2.CascadeClassifier('face-detect.xml')
eye = cv2.CascadeClassifier('eye-detect.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

muka = face.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in muka:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

    cv_warna = img[y:y+h, x:x+w]
    cv_gray = gray[y:y+h, x:x+w]
    mata = eye.detectMultiScale(cv_gray, 1.5, 3)
    for (mx,my,mw,mh) in mata:
        cv2.rectangle(cv_warna, (mx,my), (mx+mw, my+mh), (255, 255, 0), 1)

cv2.imshow('Foto Normal', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
