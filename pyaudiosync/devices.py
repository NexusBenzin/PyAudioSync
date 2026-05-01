import errors
import re
import sounddevice as sd


class AudioDeviceManager:
    def __init__(self):
        self.devices = sd.query_devices()

    @staticmethod
    def get_devices():
        devices = sd.query_devices()
        seen_names = set()
        result = []
        for i, device in enumerate(devices):
            if device['max_output_channels'] > 0:
                name = device['name']
                clean_name = name.split(" (@")[0]
                normalized = re.sub(r'\s*\(.*?\)', '', clean_name)
                normalized = re.sub(r'\s+\d+$', '', normalized).strip()

                if normalized.lower() not in seen_names:
                    seen_names.add(normalized.lower())
                    result.append({
                        "id": i,
                        "name": clean_name,  # Return the cleaner version
                        "channels": device['max_output_channels']
                    })

        if not result:
            errors.error("No audio output devices found.")

        return result








