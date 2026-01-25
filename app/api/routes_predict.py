from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.core.security import verify_token
from app.services.model_service import predict_car_price
from app.core.dependencies import get_current_user, get_api_key

router = APIRouter()

class CarFeatures(BaseModel):
    company: str
    year: int
    owner : str
    fuel : str
    seller_type : str
    transmission : str
    km_driven : str
    mileage_mpg: str
    engine_cc: str
    max_power_bhp : str = Field(..., alias="max_power")
    torque_nm : str 
    seats : float
    model_config = {"populate_by_name": True}
    

@router.post("/predict")
def predict_price(car: CarFeatures,
                  user=Depends(get_current_user),
                  _=Depends(get_api_key)):
    ''' Endpoint to predict car price '''
    prediction = predict_car_price(car.model_dump())
    return {'predicted_price': prediction}

