"""Plugin to handle retry in case of exception with DSLR/gPhoto2 camera."""
import pibooth
from pibooth.utils import LOGGER
from pibooth import camera

__version__ = "1.0.0"
def setup_tweaked_camera():
    gp_cam_proxy = camera.get_gp_camera_proxy()
    if gp_cam_proxy:
        LOGGER.info("Configuring gPhoto2 camera with restart ...")
        return GpCameraRetry(gp_cam_proxy)

class GpCameraRetry(camera.GpCamera):

    def capture(self, effect=None):
        """Capture a new picture.
        """
        retry = 0
        max_retry = 2
        while retry < max_retry:
            try:
                return super(GpCameraRetry, self).capture(effect)
            except Exception:
                LOGGER.warning("Gphoto2 capture failed. Restarting the camera and trying again...")
                if self._cam:
                    self._cam.exit()
                    del self._cam
                    self._cam = camera.get_gp_camera_proxy()
            retry += 1
        raise EnvironmentError("Gphoto2 capture failed {} times".format(max_retry))

    def preview(self, window, flip=True):
        """Capture a new picture.
        """
        retry = 0
        max_retry = 2
        while retry < max_retry:
            try:
                return super().preview(window, flip)
            except Exception:
                LOGGER.warning("Gphoto2 preview failed. Restarting the camera and trying again...")
                if self._cam:
                    self._cam.exit()
                    del self._cam #must be there. exit() doesn't release the device.
                self._cam = camera.get_gp_camera_proxy() #initialise again
            retry += 1
        raise EnvironmentError("Gphoto2 preview failed {} times".format(max_retry))

@pibooth.hookimpl
def pibooth_setup_camera(cfg):
    return setup_tweaked_camera()
