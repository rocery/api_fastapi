from datetime import datetime

from pydantic import BaseModel


class DeviceResponse(BaseModel):
    device_id: str
    device_name: str
    ip_address: str
    location: str
    etc: str
    ping: str | None

class IspSpeedtestResponse(BaseModel):
    id: int
    isp: str
    download_mbps: float
    upload_mbps: float
    ping_ms: float
    created_at: datetime
    server_city: str
    server: str | None
    
    model_config = {
        "from_attributes": True
    }