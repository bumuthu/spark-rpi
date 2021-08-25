
import cv2
import imutils
import numpy as np
import base64

in_img_path = "./input_img.jpg"
out_img_path = "./output_img.jpg" 


class Detector:

    def __init__(self):
        print("Detector initialized")

    def detect(self):

        image = cv2.imread(in_img_path)
        self.image = image
        image_blur = cv2.medianBlur(image,25)
        image_blur_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)

        image_res ,image_thresh = cv2.threshold(image_blur_gray,240,255,cv2.THRESH_BINARY_INV)
        kernel = np.ones((3,3),np.uint8)
        opening = cv2.morphologyEx(image_thresh,cv2.MORPH_OPEN,kernel) 
        dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
        ret, last_image =  cv2.threshold(dist_transform, 0.3*dist_transform.max(),255,0)
        last_image = np.uint8(last_image)

        cnts = cv2.findContours(last_image.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        self.cnts = cnts

        return len(cnts)

    def get_image(self):

        for (i, c) in enumerate(self.cnts):
            ((x, y), _) = cv2.minEnclosingCircle(c)
            cv2.putText(self.image, "#{}".format(i + 1), (int(x) - 45, int(y)+20),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
            cv2.drawContours(self.image, [c], -1, (0, 255, 0), 2)

        cv2.imwrite(out_img_path, self.image)

        with open(out_img_path, "rb") as imageFile:
            base_encoded = base64.b64encode(imageFile.read()).decode('ascii')

        return base_encoded