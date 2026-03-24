import re
import sounddevice as sd


class NoDevicesFoundError(Exception):
    pass
class AudioDeviceManager:
    def __init__(self):
        self.devices = sd.query_devices()











    def get_output_devices(self):
        seen_names = set()
        result = []
        for i, device in enumerate(self.devices):
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
            raise NoDevicesFoundError("No output devices were detected on this system.")

        return result