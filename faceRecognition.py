from fer import FER
import cv2
from PIL import Image

class Facial:

    def whatFacialExpression(self, filePlace, img, lastEmotion):

        img = cv2.imread(filePlace)
        detector = FER()
        detector.detect_emotions(img)
        if detector.top_emotion(img)[0] == "happy":
                return "happy"
        elif detector.top_emotion(img)[0] == "sad":
                return "sad"
        else:
            return lastEmotion