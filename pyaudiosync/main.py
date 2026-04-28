from devices import AudioDeviceManager
from gui import gui
from quote import get_quote


devices = AudioDeviceManager.get_devices()


quote_data = get_quote()
gui(device_list=devices, quote=(f"{quote_data['quote']} - {quote_data['author']}"))



