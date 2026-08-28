from pydantic import BaseModel


class AtkResponse(BaseModel):
    id: int
    varian: str | None
    item: str | None
    satuan: str | None
    harga: float | None
