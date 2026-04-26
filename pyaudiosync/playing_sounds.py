import numpy as np
import sounddevice as sd


def play_beep(device_id, frequency=440, duration=1):
    fs = 44100
    t = np.linspace(0, duration, int(fs * duration), False)
    beep = 0.5 * np.sin(2 * np.pi * frequency * t)
    if device_id != 0:
        print(f"playing to device {device_id}")

    if device_id != 0:
        try:
            sd.play(beep, samplerate=fs, device=(device_id))
            sd.wait()
        except:
            print("could not play to device (Maybe device is not connected?)")
    else:
        print("No device selected")