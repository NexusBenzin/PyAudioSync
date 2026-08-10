import errors
import threading
import soundfile as sf
import sounddevice as sd


def play_file_single(device_id, path):
    try:
        file = (path)
    except Exception as e:
        # errors.error(f"Couldn't find file {file} with error: {e}, Does file exist?"
        print(e)

    try:
        data, fs = sf.read(file, dtype='float32')
    except Exception as e:
        errors.error(f"Couldn't read file {file} with error: {e}, Does the file exist and contain audio?")

    try:
        sd.play(data, samplerate=fs, device=device_id)
        sd.wait()
    except Exception as e:
        errors.error(f"Couldn't play file {file} with error: {e}")

def play_file_multiple(device_ids, path):
    threads = []
    for i in device_ids:
        t = threading.Thread(target=play_file_single, args=(i, path))
        threads.append(t)
        t.start()
