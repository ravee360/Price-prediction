# Car Price Prediction System

A full-stack machine learning application for predicting car prices using machine learning models, FastAPI backend, and Streamlit UI. This project demonstrates production-ready deployment practices with containerization, monitoring, and caching.

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Directory Structure](#directory-structure)
4. [Technology Stack](#technology-stack)
5. [Setup & Installation](#setup--installation)
6. [Configuration](#configuration)
7. [Running the Application](#running-the-application)
8. [API Documentation](#api-documentation)
9. [Deployment](#deployment)
10. [Monitoring & Logging](#monitoring--logging)
11. [Development Guide](#development-guide)

---

## 🎯 Project Overview

This is a **Car Price Prediction System** that uses machine learning to predict car selling prices based on various features such as:
- Car company/brand
- Year of manufacture
- Owner history (First, Second, Third, Fourth owner)
- Fuel type (Petrol, Diesel, CNG, LPG, Electric)
- Seller type (Individual, Dealer, Trustmark Dealer)
- Transmission (Manual, Automatic)
- Technical specifications (KM driven, Mileage, Engine CC, Max Power, Torque, Seats)

**Key Features:**
- ✅ RESTful API with JWT authentication
- ✅ API Key-based authentication option
- ✅ Redis caching for prediction results
- ✅ Prometheus metrics & Grafana dashboard
- ✅ Streamlit web UI
- ✅ Docker containerization
- ✅ Production-ready logging and error handling

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────┐
│              Streamlit UI (Web Interface)            │
│         (Can be hosted separately)                   │
└──────────────────┬──────────────────────────────────┘
                   │ HTTP Requests
                   │
┌──────────────────▼──────────────────────────────────┐
│              FastAPI Backend                         │
│  ┌────────────────────────────────────────────────┐ │
│  │  Authentication Routes (/auth/login)           │ │
│  │  - JWT Token generation                        │ │
│  │  - Username/Password validation                │ │
│  └────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────┐ │
│  │  Prediction Routes (/api/predict)              │ │
│  │  - Token verification                          │ │
│  │  - API Key validation                          │ │
│  │  - Model inference                             │ │
│  └────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────┐ │
│  │  Middleware & Cross-Cutting Concerns           │ │
│  │  - Logging Middleware                          │ │
│  │  - Error Handling                              │ │
│  │  - Prometheus Instrumentation                  │ │
│  └────────────────────────────────────────────────┘ │
└──────────────────┬──────────────────────────────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
    ┌───────┐ ┌────────┐ ┌──────────────┐
    │ Redis │ │  ML    │ │  Prometheus  │
    │ Cache │ │ Model  │ │  Metrics     │
    └───────┘ └────────┘ └──────────────┘
                             │
                             ▼
                         ┌──────────┐
                         │ Grafana  │
                         │Dashboard│
                         └──────────┘
```

---

## 📁 Directory Structure

```
Price Prediction/
├── README.md                          # Original project README
├── README_DETAILED.md                 # This detailed documentation
├── requirements.txt                   # Python dependencies (backend + ML)
├── Dockerfile                         # Docker container configuration
├── docker-compose.yml                 # Multi-container orchestration
├── prometheus.yml                     # Prometheus configuration
├── render.yaml                        # Render.com deployment config
├── streamlit_app.py                   # Streamlit web interface
│
├── app/                               # Main application package
│   ├── __init__.py
│   ├── main.py                        # FastAPI app initialization
│   │
│   ├── api/                           # API route handlers
│   │   ├── __init__.py
│   │   ├── routes_auth.py             # Authentication endpoints
│   │   │   └── POST /auth/login       # Login endpoint
│   │   │
│   │   └── routes_predict.py          # Prediction endpoints
│   │       └── POST /api/predict      # Price prediction endpoint
│   │
│   ├── core/                          # Core application logic
│   │   ├── __init__.py
│   │   ├── config.py                  # Settings & environment variables
│   │   ├── security.py                # JWT token creation & verification
│   │   ├── dependencies.py            # Dependency injection (auth checks)
│   │   └── excetions.py               # Custom exception handlers
│   │
│   ├── services/                      # Business logic layer
│   │   ├── __init__.py
│   │   └── model_service.py           # ML model inference with caching
│   │
│   ├── cache/                         # Caching utilities
│   │   ├── __init__.py
│   │   └── redis_cache.py             # Redis cache operations
│   │
│   ├── middleware/                    # Custom middleware
│   │   ├── __init__.py
│   │   └── logging_middleware.py      # Request/response logging
│   │
│   └── models/                        # Serialized ML models
│       └── model.joblib               # Trained Random Forest model
│
├── training/                          # Model training scripts
│   ├── __init__.py
│   ├── train_model.py                 # Main training script
│   ├── train_utils.py                 # Helper functions for training
│   └── __pycache__/
│
├── data/                              # Datasets
│   └── car-details.csv                # Raw car data for training
│
├── notebooks/                         # Jupyter notebooks
│   ├── car-details.csv                # Data for notebooks
│   └── sample.ipynb                   # Sample analysis notebook
│
└── prometheus/                        # Prometheus configuration directory
    └── (prometheus.yml is here)
```

---

## 🛠️ Technology Stack

### Backend
- **FastAPI** (0.128.0) - Modern async web framework
- **Uvicorn** (0.38.0) - ASGI server
- **Python-Jose** (3.5.0) - JWT token handling
- **Python-Dotenv** (1.2.1) - Environment variable management

### Machine Learning
- **Scikit-Learn** (1.7.2) - ML algorithms & preprocessing
- **Pandas** (2.3.3) - Data manipulation
- **NumPy** (2.3.3) - Numerical computing
- **SciPy** (1.16.3) - Scientific computing
- **Joblib** (1.5.2) - Model serialization

### Caching & Database
- **Redis** (7.1.0) - In-memory caching

### Monitoring & Observability
- **Prometheus-FastAPI-Instrumentator** (7.1.0) - Metrics collection
- **Prometheus-Client** (0.24.1) - Prometheus metrics
- **Prometheus** (v2.52.0) - Metrics storage
- **Grafana** (10.4.2) - Visualization dashboard

### Frontend
- **Streamlit** (1.28.0) - Interactive web UI
- **Requests** (2.31.0) - HTTP client

### Containerization
- **Docker** - Container runtime
- **Docker Compose** - Multi-container orchestration

---

## 📦 Setup & Installation

### Prerequisites
- Python 3.12+
- Docker & Docker Compose (optional, for containerized setup)
- Redis (or use Docker)

### Local Installation

1. **Clone the repository:**
   ```bash
   cd "C:\Users\ravik\Desktop\Price Prediction"
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   ```bash
   # Windows
   .\venv\Scripts\Activate.ps1
   
   # Mac/Linux
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create `.env` file:**
   ```env
   API_KEY=demo-key-12345
   JWT_SECRET_KEY=your-secret-key-here
   REDIS_URL=redis://localhost:6379
   API_URL=http://localhost:8000
   ```

---

## ⚙️ Configuration

### Environment Variables (`app/core/config.py`)

| Variable | Default | Description |
|----------|---------|-------------|
| `API_KEY` | `demo-key` | API key for authentication |
| `JWT_SECRET_KEY` | `secret` | Secret key for JWT token signing |
| `JWT_ALGORITHM` | `HS256` | JWT algorithm |
| `REDIS_URL` | `redis://localhost:6379` | Redis connection URL |
| `API_URL` | `http://localhost:8000` | API base URL |

### Default Credentials
- **Username:** `admin`
- **Password:** `adminpass`

---

## 🚀 Running the Application

### Option 1: Run Locally (All Components)

#### 1. Start Redis (in a separate terminal)
```bash
# If you have Redis installed
redis-server

# Or using Docker
docker run -d -p 6379:6379 redis:alpine
```

#### 2. Start FastAPI Backend
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: `http://localhost:8000`

Swagger docs: `http://localhost:8000/docs`

#### 3. Start Streamlit Frontend (in another terminal)
```bash
streamlit run streamlit_app.py
```

Streamlit will be available at: `http://localhost:8501`

### Option 2: Run with Docker Compose (Recommended)

```bash
docker-compose up -d
```

This starts:
- **FastAPI** on `http://localhost:8000`
- **Redis** (internal)
- **Prometheus** on `http://localhost:9090`
- **Grafana** on `http://localhost:3000` (admin/admin)
- **Streamlit** manually: `streamlit run streamlit_app.py`

### Option 3: Host Streamlit Separately

Create a separate `requirements-streamlit.txt`:
```
streamlit==1.28.0
requests==2.31.0
python-dotenv==1.2.1
```

Deploy on services like:
- Streamlit Cloud (free)
- Heroku
- Vercel
- Railway
- Render

Configure API_URL in `.env` to point to your backend:
```env
API_URL=https://your-backend-api.com/
API_KEY=your-api-key
```

---

## 📡 API Documentation

### Authentication Endpoints

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "adminpass"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Prediction Endpoints

#### Predict Car Price
```http
POST /api/predict
Content-Type: application/json
Authorization: Bearer {token}
api-key: {api-key}

{
  "company": "maruti",
  "year": 2015,
  "owner": "First",
  "fuel": "Petrol",
  "seller_type": "Dealer",
  "transmission": "Manual",
  "km_driven": "50000",
  "mileage_mpg": "18.0",
  "engine_cc": "1197",
  "max_power": "74",
  "torque_nm": "100",
  "seats": 5.0
}
```

**Response:**
```json
{
  "predicted_price": 4500000.50
}
```

**Status Codes:**
- `200` - Successful prediction
- `401` - Unauthorized (invalid token/key)
- `422` - Validation error (missing/invalid fields)
- `500` - Server error

---

## 🐳 Deployment

### Render.com Deployment

The project includes `render.yaml` for automatic deployment:

```bash
# Push to GitHub
git push origin main

# Render automatically deploys from this config
```

### Docker Deployment

1. **Build image:**
   ```bash
   docker build -t car-price-api:1.0 .
   ```

2. **Run container:**
   ```bash
   docker run -p 8000:8000 \
     -e API_KEY=your-key \
     -e JWT_SECRET_KEY=your-secret \
     -e REDIS_URL=redis://redis:6379 \
     car-price-api:1.0
   ```

### Environment-Specific Configurations

Create `.env.production`:
```env
API_KEY=production-api-key
JWT_SECRET_KEY=production-secret-key
REDIS_URL=redis://redis-prod:6379
API_URL=https://car-price-api.example.com
```

---

## 📊 Monitoring & Logging

### Prometheus Metrics

Access Prometheus at: `http://localhost:9090`

**Available Metrics:**
- `http_requests_total` - Total HTTP requests
- `http_request_duration_seconds` - Request duration
- `http_exceptions_total` - Total exceptions
- Custom ML model metrics

### Grafana Dashboard

Access Grafana at: `http://localhost:3000`

**Default Credentials:**
- Username: `admin`
- Password: `admin`

**Add Prometheus Data Source:**
1. Configuration → Data Sources → Add
2. URL: `http://prometheus:9090`
3. Save & Test

### Application Logging

The `LoggingMiddleware` logs:
- Request method, path, and query parameters
- Response status code and latency
- Errors and exceptions

Log format:
```
[TIMESTAMP] - "METHOD /path" - STATUS_CODE - {latency}ms
```

---

## 🧠 Machine Learning Model

### Model Details (`training/train_model.py`)

**Algorithm:** Random Forest Regressor
- Estimators: 10
- Max Depth: 5
- Random State: 42

**Data Pipeline:**

```
Raw Data (car-details.csv)
    ↓
[Data Cleaning]
    ├─ Drop duplicates
    └─ Drop irrelevant columns (name, model, edition)
    ↓
[Feature Separation]
    ├─ Numerical: year, km_driven, engine_cc, etc.
    └─ Categorical: company, fuel, transmission, etc.
    ↓
[Preprocessing]
    ├─ Numerical: Impute (median) → Scale (StandardScaler)
    └─ Categorical: Impute (constant) → Encode (OneHotEncoder)
    ↓
[Random Forest Regressor]
    ↓
[Trained Model] → model.joblib
```

### Training the Model

```bash
python -m training.train_model
```

This will:
1. Load data from `data/car-details.csv`
2. Split into train/test (80/20)
3. Preprocess features
4. Train Random Forest model
5. Save to `app/models/model.joblib`
6. Display metrics (MAE, RMSE, R²)

---

## 🔐 Security

### Authentication Methods

**1. JWT Token (OAuth2-like)**
```python
# Login to get token
POST /auth/login
# Use in header
Authorization: Bearer {token}
```

**2. API Key**
```python
# Use in header
api-key: {api-key}
```

### Security Best Practices Implemented

- ✅ Password hashing (via python-jose)
- ✅ JWT token expiration (30 minutes default)
- ✅ Dependency injection for auth checks
- ✅ CORS support ready
- ✅ Input validation via Pydantic

### CORS Configuration

Add CORS middleware to `app/main.py` if needed:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-streamlit-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 💾 Caching Strategy

### Redis Caching (`app/cache/redis_cache.py`)

Predictions are cached based on input features:

```python
# Cache key = concatenation of all feature values
cache_key = "maruti_2015_First_Petrol_Dealer_Manual_50000_18.0_1197_74_100_5.0"

# Check cache first
if cached_result exists:
    return cached_result
else:
    compute prediction
    store in cache
    return prediction
```

**Benefits:**
- 🚀 Faster response for duplicate queries
- 📉 Reduced model inference load
- 💰 Lower computational costs

---

## 🐛 Troubleshooting

### Redis Connection Error
```
ConnectionError: Error 111 connecting to localhost:6379
```
**Solution:** Start Redis or update `REDIS_URL` in `.env`

### JWT Token Expired
```json
{"detail": "Token has expired"}
```
**Solution:** Login again to get a new token

### Model Not Found
```
FileNotFoundError: app/models/model.joblib not found
```
**Solution:** Run `python -m training.train_model` to train the model

### Port Already in Use
```
OSError: [Errno 48] Address already in use
```
**Solution:** Change port or kill the process using it:
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID {PID} /F

# Mac/Linux
lsof -i :8000
kill -9 {PID}
```

---

## 📚 Development Guide

### Adding a New Feature

1. **Create a new route** in `app/api/routes_*.py`
2. **Define request model** using Pydantic
3. **Add business logic** in `app/services/`
4. **Include in** `app/main.py` with router.include_router()
5. **Test** via Swagger docs at `/docs`

### Running Tests

```bash
# Install pytest
pip install pytest

# Run tests
pytest tests/ -v
```

### Code Structure Best Practices

```
app/
├── api/              # Route handlers (presentation layer)
├── services/         # Business logic (application layer)
├── core/             # Domain logic (core layer)
└── cache/            # Data access (persistence layer)
```

### Adding Environment Variables

1. Add to `.env` file
2. Load in `app/core/config.py`
3. Access via `settings.VARIABLE_NAME`

---

## 📝 API Response Examples

### Success Response
```json
{
  "predicted_price": 4500000.50
}
```

### Error Response
```json
{
  "detail": "Invalid API key"
}
```

### Validation Error Response
```json
{
  "detail": [
    {
      "loc": ["body", "year"],
      "msg": "ensure this value is greater than 1900",
      "type": "value_error.number.not_gt"
    }
  ]
}
```

---

## 🚀 Performance Optimization

### Model Inference Caching
- Predictions cached in Redis
- TTL: Default (until restart)
- Hit rate: ~40-50% for typical usage

### Database Indexing
- Redis uses in-memory hash tables
- O(1) average lookup time

### Async Operations
- FastAPI uses async/await
- Non-blocking request handling

### Batch Predictions
Currently single predictions only. For batch:
```python
@router.post("/api/predict-batch")
def predict_batch(cars: List[CarFeatures]):
    # Returns list of predictions
```

---

## 📦 Dependencies Summary

| Package | Version | Purpose |
|---------|---------|---------|
| fastapi | 0.128.0 | Web framework |
| uvicorn | 0.38.0 | ASGI server |
| scikit-learn | 1.7.2 | ML algorithms |
| pandas | 2.3.3 | Data processing |
| numpy | 2.3.3 | Numerical computing |
| redis | 7.1.0 | Caching |
| joblib | 1.5.2 | Model serialization |
| streamlit | 1.28.0 | Web UI |
| python-jose | 3.5.0 | JWT tokens |
| prometheus | 7.1.0 | Metrics |

---

## 📄 License

This project is part of a FastAPI capstone project.

---

## 👤 Contributing

1. Create a feature branch
2. Make changes
3. Test locally
4. Submit pull request

---

## 📞 Support

For issues or questions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review API docs at `/docs`
3. Check Prometheus metrics for system health

---

**Last Updated:** January 28, 2026

---
