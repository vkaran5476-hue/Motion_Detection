import cv2

image = cv2.imread(r"C:\Users\karan\Downloads\adorable-puppy-sitting-on-green-grass-photo.jpg")

if image is None:
    print("Image not found")
else:
    print("Image found")
    pt1 = (20,30)
    pt2 = (450,400)

    color = (0,0,255)
    thickness = 3

    cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("images",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()