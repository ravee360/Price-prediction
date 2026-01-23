''' Load the trained model and do the predictions with redis caching'''
import joblib
import pandas as pd
from app.cache.redis_cache import get_cache_prediction, set_cache_prediction
from app.core.config import settings

model = joblib.load(settings.MODEL_PATH)

def predict_car_price(data: dict) -> dict:
    ''' Predict car price with caching '''
    input_df = pd.DataFrame([data])
    cache_key =" ".join([str(value) for value in data.values()])
    
    
    cached_result = get_cache_prediction(cache_key)
    if cached_result:
        return cached_result
    
    prediction = model.predict(input_df)
    result = {"predicted_price": prediction[0]}
    
    set_cache_prediction(cache_key, result)
    
    return result