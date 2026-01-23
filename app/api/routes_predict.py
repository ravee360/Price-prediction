from fastAPI import APIRouter, Depends
from pydantic import BaseModel
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
    max_power: str
    torque_nm : str 
    seats : float
    

@router.post("/predict")
def predict_price(car: CarFeatures,
                  user=Depends(get_current_user),
                  _=Depends(get_api_key)):
    ''' Endpoint to predict car price '''
    prediction = predict_car_price(car.model_dump())
    return {'predicted_price': prediction}

