import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

# mpHands = mp.solutions.hands
# hands = mpHands.Hands()


while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()


# import cv2
# image = cv2.imread("filename.jpg" , flag)
#
# if image is not None:
#   success = cv2.imwrite("output_python.png", image)
#     if success:
#         print("Image saved as 'output_python.png'")
#     else:
#         print("Error saving images")
#
#     else:
#     print("Images is found")
#
# else:
#     print("Images is not found")

# import cv2
#
# image = cv2.imread{"phase 1 /python_images.png"}
#
# if image is not None:
#     h, w , c = image.shape
#     print(f"Image Loaded:\n Height{h} \n width : {w} \n channel : {c} ")
# else:
# print(f"could not load image")

# resized =cv2.resize(image,(300,300))

# cv2.imshow("original",resized)
# cv2.imshow("resized",resized)
#
# cv2.imwrite("resized.jpg",resized)