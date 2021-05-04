import os,sys
from time import time, sleep
import picamera
while True:
    sleep(30 - time() % 30)
	# thing to run
    
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        print("init camera")
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        path = '~/Desktop/pycoral'
        camera.capture('./pycoral/test_data/cars.jpg')
        print("picture clicked")
    os.system("sudo python3 "+path+"/examples/detect_image.py   --model "+path+"/test_data/ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite   --labels "+path+"/test_data/coco_labels.txt   --input "+path+"/test_data/cars.jpg   --output "+path+"/test_data/processed/cars_processed.jpg")

    print("ran detect_image.py")
    
    os.system("sudo python3 ./firestore/firestoreTest.py")
    print("data sent to cloud")
        
