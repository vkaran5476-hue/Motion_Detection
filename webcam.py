from tkinter.font import Font

import cv2

cap =cv2.VideoCapture(0)

while True:
    returns,frame=cap.read() #return true or false

    if not returns:
        print("No Images")
        break


    cv2.imshow("Images",frame)

    if cv2.waitKey(1) &0xFF == ord('q'):
        print("Quit")
        break
cap.release()
cv2.destroyAllWindows()

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()