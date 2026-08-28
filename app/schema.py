from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: dict


class DeviceResponse(BaseModel):
    device_id: str
    device_name: str
    ip_address: str
    location: str
    etc: str
    ping: str | None


class AtkResponse(BaseModel):
    id: int
    varian: str | None
    item: str | None
    satuan: str | None
    harga: float | None