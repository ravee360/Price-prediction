import os
import streamlit as st
import requests


def get_env(key: str, default: str = ""):
    return os.environ.get(key, default)


API_URL_DEFAULT = get_env("API_URL", "https://your-api-url")
API_KEY_DEFAULT = get_env("API_KEY", "demo-key")


def login(api_url, username, password):
    try:
        resp = requests.post(f"{api_url.rstrip('/')}/auth/login", json={"username": username, "password": password}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        token = data.get("access_token") or data.get("accessToken")
        return token, None
    except Exception as e:
        return None, str(e)


def predict(api_url, api_key, token, payload):
    headers = {}
    if api_key:
        headers["api-key"] = api_key
    if token:
        headers["token"] = token

    try:
        resp = requests.post(f"{api_url.rstrip('/')}/api/predict", json=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.json(), None
    except Exception as e:
        try:
            # try to show server error body
            return None, f"{e} - {resp.text if 'resp' in locals() else ''}"
        except Exception:
            return None, str(e)


st.set_page_config(page_title="Car Price Predictor", layout="wide")

st.title("Car Price Prediction — Streamlit UI")

with st.sidebar.form(key="config"):
    api_url = st.text_input("API Base URL", value=API_URL_DEFAULT)
    api_key = st.text_input("API Key (header 'api-key')", value=API_KEY_DEFAULT)
    st.write("\n")
    st.markdown("**Login**")
    username = st.text_input("Username", value="admin")
    password = st.text_input("Password", type="password", value="adminpass")
    login_btn = st.form_submit_button("Login")

if "token" not in st.session_state:
    st.session_state.token = None

if login_btn:
    token, err = login(api_url, username, password)
    if token:
        st.session_state.token = token
        st.sidebar.success("Logged in — token saved in session")
    else:
        st.sidebar.error(f"Login failed: {err}")

col1, col2 = st.columns(2)

with col1:
    st.header("Car features")
    company = st.text_input("Company", "maruti")
    year = st.number_input("Year", min_value=1900, max_value=2100, value=2015)
    owner = st.selectbox("Owner", ["First", "Second", "Third", "Fourth"], index=0)
    fuel = st.selectbox("Fuel", ["Petrol", "Diesel", "CNG", "LPG", "Electric"], index=0)
    seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"], index=1)
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"], index=0)

with col2:
    st.header("Technical specs")
    km_driven = st.text_input("KM Driven", "50000")
    mileage_mpg = st.text_input("Mileage (mpg)", "18.0")
    engine_cc = st.text_input("Engine (cc)", "1197")
    max_power = st.text_input("Max Power (bhp)", "74")
    torque_nm = st.text_input("Torque (nm)", "100")
    seats = st.number_input("Seats", min_value=1.0, max_value=12.0, value=5.0)

submit = st.button("Predict Price")

if submit:
    # Build payload according to API `CarFeatures`
    payload = {
        "company": company,
        "year": int(year),
        "owner": owner,
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "km_driven": str(km_driven),
        "mileage_mpg": str(mileage_mpg),
        "engine_cc": str(engine_cc),
        "max_power": str(max_power),
        "torque_nm": str(torque_nm),
        "seats": float(seats),
    }

    st.info("Sending request to prediction API...")
    result, err = predict(api_url, api_key, st.session_state.token, payload)
    if err:
        st.error(f"Prediction failed: {err}")
    else:
        st.success("Prediction received")
        st.json(result)

st.markdown("---")
st.caption("Change `API_URL` and `API_KEY` in the sidebar or set environment variables `API_URL` and `API_KEY` when deploying.")
