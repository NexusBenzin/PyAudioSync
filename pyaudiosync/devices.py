import re
import sounddevice as sd
import requests



res = requests.get("https://dummyjson.com/quotes/random")
data = res.json()
print(f"{data["quote"]} - {data['author']}")


class AudioDeviceManager:
    def __init__(self):
        self.devices = sd.query_devices()


    def get_output_devices():
        devices = sd.query_devices()
        seen_names = set()
        result = []
        for i, device in enumerate(devices):
            if device['max_output_channels'] > 0:
                name = device['name']
                normalized = re.sub(r'\s*\(.*?\)', '', name)
                normalized = re.sub(r'\s+\d+$', '', normalized).strip()
                normalized = normalized.lower()
                if normalized not in seen_names:
                    seen_names.add(normalized)
                    result.append({
                        "id": i,
                        "name": name,
                        "channels": device['max_output_channels']
                    })

        if not result:
            raise RuntimeError("No audio output devices found.")

        return result