import cv2
import numpy  as np 

resim = cv2.imread("Logo.jpeg",0)

cv2.imshow("Ahmet Ilkay", resim)

cv2.imwrite("LogoGri.jpeg" ,resim)



cv2.waitKey(0) #Pencerenin kalmasi icin herhangi bir tusa basmayi bekler
cv2.destroyAllWindows() #Carpiya bastigimiz zaman resimle alakali tum pencereleri kapatir.