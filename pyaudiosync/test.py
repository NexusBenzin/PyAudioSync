import errors
import threading
import numpy as np
import sounddevice as sd


def test_single(device_id, beep, fs):
    try:
        sd.play(beep, samplerate=fs, device=device_id)
        sd.wait()
    except Exception as e:
        errors.error(f"Error with device {device_id}: {e}")

def test_multiple(device_ids, frequency=440, duration=1):
    fs = 44100
    t = np.linspace(0, duration, int(duration * fs), False)
    beep = 0.5 * np.sin(2 * np.pi * frequency * t)

    threads = []
    for i in device_ids:
        t = threading.Thread(target=test_single, args=(i, beep, fs))
        threads.append(t)
        t.start()
