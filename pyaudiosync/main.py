from pyaudiosync.devices import AudioDeviceManager
from pyaudiosync.gui import gui

devices = AudioDeviceManager.get_devices()


gui(devices)