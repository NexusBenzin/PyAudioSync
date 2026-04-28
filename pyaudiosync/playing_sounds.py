import threading
import numpy as np
import sounddevice as sd


def play_single(device_id, beep, fs):
    try:
        sd.play(beep, samplerate=fs, device=device_id)
        sd.wait()
    except Exception as e:
        print(f"Error with device {device_id}: {e}")

def play_multiple(device_ids, frequency=440, duration=1):
    fs = 44100
    t = np.linspace(0, duration, int(duration * fs), False)
    beep = 0.5 * np.sin(2 * np.pi * frequency * t)

    threads = []
    for d_id in device_ids:
        t = threading.Thread(target=play_single, args=(d_id, beep, fs))
        threads.append(t)
        t.start()
