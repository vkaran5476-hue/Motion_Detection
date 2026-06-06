import cv2

image = cv2.imread(r"C:\Users\karan\OneDrive\Documents\download.jpg")

blurred = cv2.medianBlur(image,5)

cv2.imshow("blurred",blurred)
cv2.imshow("second image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()