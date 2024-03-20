import os
import numpy as np
import cv2

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

class Shorse:
    def display(self):
        # load image from assets folder
        img = cv2.imread(os.path.join(os.path.dirname(__file__), 'assets', 'shorse.png'))

        # resize the image to 50% of screen size, maintaining aspect ratio
        scale_percent = 50
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)

        # dsize
        dsize = (width, height)

        # resize image
        img = cv2.resize(img, dsize)
        # write press q to quit in the bottom of the image centered horizontally
        font = cv2.FONT_HERSHEY_SIMPLEX
        # vertical bottom, horizontal center
        bottomLeftCornerOfText = (int(width/4),height-10)
        fontScale = 1
        fontColor = (240,150,100)
        lineType = 2
        cv2.putText(img,'Press q to quit',
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType)
        # display the image
        cv2.imshow('Shorse', img)

        # wait for q to be pressed
        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def dance(self):
        # rotate image 70 degrees right then 70 degrees left in a video
        img = cv2.imread(os.path.join(os.path.dirname(__file__), 'assets', 'shorse.png'))
        scale_percent = 50
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dsize = (width, height)
        img = cv2.resize(img, dsize)

        # write press q to quit in the bottom of the image centered horizontally
        font = cv2.FONT_HERSHEY_SIMPLEX
        # vertical bottom, horizontal center
        bottomLeftCornerOfText = (int(width / 4), height - 10)
        fontScale = 1
        fontColor = (240, 150, 100)
        lineType = 2
        cv2.putText(img, 'Press q to quit',
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    lineType)

        # 14 rotations of 5 degrees to be 70 degrees
        total_rotations = -14
        right = True

        # keep rotating right and left 70 degrees (5 degrees each frame)
        while True:

            if right:
                total_rotations += 1
                rotated = rotate_image(img, 5 * total_rotations)
            else:
                total_rotations -= 1
                rotated = rotate_image(img, 5 * total_rotations)

            cv2.imshow('Shorse', rotated)

            if total_rotations == 14:
                right = False
            elif total_rotations == -14:
                right = True
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

