import cv2
import numpy as np
image = cv2.imread(r"C:\Users\karan\OneDrive\Documents\download.jpg")


# sharpen_kernel = cv2.imread(r"C:\Users\karan\OneDrive\Documents\download.jpg")
sharpen_kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])


sharpened = cv2.filter2D(image,-1,sharpen_kernel)
cv2.imshow("original",image)
cv2.imshow("sharpened",sharpened)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()