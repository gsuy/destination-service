from pydantic import BaseModel

class GridTripInfo(BaseModel):
    dayofweek: str
    hour: int
    latitude: float
    longitude: float