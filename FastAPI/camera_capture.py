import cv2

def capture_image(filename="image.jpg"):
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        raise Exception("Could not start camera.")

    ret, frame = cam.read()

    if ret:
        cv2.imwrite(filename, frame)

    cam.release()
    return filename



