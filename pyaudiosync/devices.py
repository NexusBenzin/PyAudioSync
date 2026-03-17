import sounddevice as sd
import numpy as np
import tkinter as tk



def list_devices():
    wasapi_index = None
    for i, api in enumerate(sd.query_hostapis()):
        if "WASAPI" in api['name']:
            wasapi_index = i
            break

    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        if dev['hostapi'] == wasapi_index and dev['max_output_channels'] > 0:
            print(f"[{i}] {dev['name']}")


def play_to_device(device_id, duration=3, frequency=440):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio = np.sin(2 * np.pi * frequency * t).astype(np.float32)

    sd.play(audio, samplerate=sample_rate, device=device_id)
    sd.wait()

# list_devices()
# play_to_device(device_id=6, duration=1, frequency=440)