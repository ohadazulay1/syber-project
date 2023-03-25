from threading import Thread
from time import sleep

from computerCam import Camera
from graphics import Graphics

cp = Camera()
gr = Graphics()

thread1 = Thread(target=cp.mainProcess)
thread2 = Thread(target=gr.objectsManeger)
#thread3 = threading.Thread(target=gr.playerManeger())
thread1.start()
thread2.start()
#thread3.start()

