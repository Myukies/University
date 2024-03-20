import time
import picamera

def capture_picture():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(5) 
        camera.capture('/home/pi/image.jpg')  

def record_video():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(5)  
        camera.start_recording('/home/pi/video.h264')  
        camera.wait_recording(5)  
        camera.stop_recording()

def main():
    capture_picture()
    record_video()

if __name__ == "__main__":
    main()
