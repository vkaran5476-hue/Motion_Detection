import cv2

image = cv2.imread(r"C:\Users\karan\Downloads\adorable-puppy-sitting-on-green-grass-photo.jpg")

if image is None:
    print("Image not found")
else:
    print("Image found")
    # cv2.circle(image,(300,300),400,(255,0,0),-1)
    cv2.circle(image, (300, 300), 300, (255, 0, 0), 4)
    cv2.imshow("images",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()