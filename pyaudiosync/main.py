import requests
from pyaudiosync.devices import AudioDeviceManager
from pyaudiosync.gui import gui

devices = AudioDeviceManager.get_devices()

res = requests.get("https://dummyjson.com/quotes/random")
data = res.json()



gui(device_list=devices, quote=(f"{data["quote"]} - {data['author']}"))