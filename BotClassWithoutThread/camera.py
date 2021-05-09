from picamera import PiCamera

Image = "image.jpeg"
camera = PiCamera()

class Camera(PiCamera):
    def __init__(self):
        super(Camera, self).__init__(camera=PiCamera())
        self.camera = PiCamera()

    def prendrePhoto(self, PiCamera):
        print("test")
        camera.resolution = (1920, 1080)
        camera.rotation = 180
        camera.start_preview(fullscreen=False, window=(50, 50, 640, 480))
        sleep(5)
        camera.capture(Image)
        camera.stop_preview()
        camera.close()