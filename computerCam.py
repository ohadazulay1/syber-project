from cv2 import *
import cv2
from faceRecognition import Facial


class Camera:
    filePlace = "C:/python/photos/test1.jpg"

    def retFilePlace(self, filePlace):
        return filePlace

    def mainProcess(self):
        lastEmotion = "start"
        print("starting...")
        fr = Facial()
        #cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
            #cv2.imshow("preview", frame)
        else:
            rval = False

        while rval:
            rval, frame = vc.read()
            cv2.imwrite(self.filePlace, frame)
            emotion = fr.whatFacialExpression(self.filePlace, frame, lastEmotion)
            if emotion != lastEmotion:
                print(emotion)
                lastEmotion = emotion

            key = cv2.waitKey(500)
            if key == 27:  # exit on ESC
                break


    def finish(self):
        self.vc.release()
        cv2.destroyWindow("preview")

if __name__ == "__main__":
    c = Camera()
    c.mainProcess()
    c.finish()