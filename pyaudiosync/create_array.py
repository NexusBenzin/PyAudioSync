import sounddevice as sd
import soundfile as sf
import errors

def play_file():
    try:
        file = ("file.mp3")
    except Exception as e:
        # errors.error(f"Couldn't find file {file} with error: {e}, Does file exist?"
        print(e)

    try:
        data, fs = sf.read(file, dtype='float32')
    except Exception as e:
        errors.error(f"Couldn't read file {file} with error: {e}, Does the file exist and contain audio?")

    try:
        sd.play(data, samplerate=fs)
        sd.wait()
    except Exception as e:
        errors.error(f"Couldn't play file {file} with error: {e}")


play_file()