from dataclasses import dataclass

import tinytuya


@dataclass
class Device:
    device_id: str
    ip_address: str
    locale_key: str

    def get_device(self):
        device = tinytuya.BulbDevice(self.device_id, self.ip_address, self.locale_key)
        device.set_version(3.3)
        return device

