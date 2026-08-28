from pydantic import BaseModel


class DeviceResponse(BaseModel):
    device_id: str
    device_name: str
    ip_address: str
    location: str
    etc: str
    ping: str | None
