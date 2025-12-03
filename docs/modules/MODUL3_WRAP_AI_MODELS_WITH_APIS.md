# Modul 3: Wrap AI Models with APIs - Opsummering

**Kursus:** AI Systems & Infrastructure  
**Formål:** Byg dine egne APIs til at serve AI modeller, fra basic server setup til authentication, database-backed user management, og rate limiting—transformér dig fra API consumer til API producer.

---

## 📚 TL;DR

Byg dine egne APIs til at serve AI modeller, dækker alt fra basic server setup og AI model integration til authentication, database-backed user management, og rate limiting—transformér dig fra API consumer til API producer.

---

## 🎯 Hovedbegreber

### Fra Consumer til Producer

**Problem:**
- I tidligere moduler har vi brugt APIs fra andre (OpenAI, Anthropic, etc.)
- Dette koster penge hver gang
- Det er tid til at serve dine egne APIs så du bliver producer (og måske tjene penge ved at lade andre bruge dine APIs)

**Eksempel:**
- Denne blog site er en fully self-hosted website med basic HTTP-based APIs
- Når du besøger et post, sender din browser en GET request til serveren
- Serveren svarer med HTML body for browseren at render
- At vide hvordan man implementerer egne APIs gør det muligt at lave mange seje ting du kan kontrollere helt selv!

**API Servers:**
- En type applikation der lytter til API requests sendt til dem og producerer de tilsvarende responses
- Ligesom køkkener der opretholder orden og delivery windows for at acceptere og opfylde ordrer
- Holder typisk processen af hvordan en ordre processeres bag dørene
- Publicly accessible APIs er ikke magi—de er served af API servers kørt af providers på en eller flere maskiner identificeret af APIs' tilsvarende domæner

---

## 🐍 Python API Servers

**Hvorfor Python?**
- Python er de facto sproget for at implementere AI modeller
- Når vi wrapper vores AI modeller med APIs, er det ligetil hvis API servers også er implementeret med Python
- Så kan vi implementere modeller og servers i ét Python program

**Tre populære Python frameworks:**

### 1. FastAPI

**Hvad er det?**
- Moderne og high-performance framework til at bygge APIs hurtigt og effektivt
- Relativt ny spiller i Python API frameworks, men er hurtigt blevet en af de hurtigst voksende frameworks
- Built-in support for essentielle komponenter af APIs som authentication og input validation
- Egnet til at implementere high-performing API servers takket være asynchronous support
- Tænk på et køkken der ikke bliver optaget af et par ordrer under processing og altid kan tage og processe nye requests

**Eksempel:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

### 2. Django

**Hvad er det?**
- Omfattende web framework designet til at implementere komplekse web applikationer (websites) i stedet for at fokusere på APIs
- Følger klassisk MVT (Model-View-Template) design pattern:
  - **Model:** Repræsenterer data du vil vise, typisk fra database
  - **View:** Håndterer indkommende requests og returnerer appropriate template og content
  - **Template:** HTML fil der definerer strukturen af web siden og inkluderer logik for at vise data
- Kommer med mange built-in moduler til at bygge web apps (database connectors, authentication)

**Eksempel:**
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]

# views.py
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"message": "Hello, World!"})
```

### 3. Flask

**Hvad er det?**
- Web framework lignende Django, men designet til at være lightweight og modular
- Built-in funktionaliteter er basic, men kan udvides gennem additional packages
- Egnet til at implementere smaller-scale applikationer eller prototyping
- Normalt betragtet som den mindst performante blandt de tre frameworks, pga. manglende asynchronous support

**Eksempel:**
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})
```

**Sammenligning:**
- FastAPI og Flask er simplere end Django
- Vi bruger **FastAPI** som primary eksempel i dette modul

---

## 🚀 FastAPI Fundamentals

### Basic Setup

**Packages nødvendige:**
- `fastapi` - Håndterer definitionen af serveren
- `uvicorn` - Server worker der faktisk gør API serving heavy-lifting

**Minimal Implementation:**
```python
# main.py
from fastapi import FastAPI

app = FastAPI(title="My AI API Server", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to my AI API server!"}
```

**Start Server:**
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Forklaring:**
- `main:app` - Peger på app objektet vi implementerede i main programmet
- `--reload` - Fortæller serveren at automatisk genstarte sig selv efter vi modificerer main.py (for development)
- `127.0.0.1` - IP af "localhost"—computeren vi kører serveren på
- `--host 127.0.0.1` - Serveren accepterer kun requests sendt fra samme computer
- `8000` - Porten vores server lytter på

**Test:**
- Send GET request til `http://127.0.0.1:8000` med requests library eller browser
- Du vil se log messages fra serveren

### Routes og URL Variables

**Specifikke Routes:**
```python
@app.get("/secret")
def get_secret():
    return {"message": "You find my secret!"}
```

**URL Template Variables:**
```python
@app.get("/parrot/{message}")
def repeat_message(message: str):
    return {"message": message}
```

**Multiple Variables:**
```python
@app.get("/parrot/{message}-{date}/secret/{user}")
def repeat_message(message: str, user: int, date: str):
    return {"message": f"A secret message {message} sent by user {user} on {date}."}
```

**URL Parameters (Query Parameters):**
```python
@app.get("/secret")
def get_secret(user: int = 0):
    return {"message": f"User {user} find my secret!"}
```

**Note:**
- URL parametre er variabler specificeret efter `?` i slutningen af URLs med format `<key>=<value>`
- Kan være `&`-separated for at specificere multiple variabler
- Eksempel: `https://www.youtube.com/watch?v=5tdsZwlWXAc&t=2s`
- I FastAPI fanges URL parametre af function parametre der ikke er dækket af URL templates

**Best Practice:**
- Følg REST principper
- Hold dine served URLs intuitive og ligetil

### Handle POST Requests

**Problem:**
- Routes vi implementerede ovenfor kan kun håndtere GET requests
- For at håndtere POST requests skal vi også læse indkommende data (request body)
- Indkommende og response data er ofte mere komplicerede og strukturerede for POST routes

**Løsning: Pydantic**

**Uden Pydantic (Problem):**
```python
@app.post("/receiver")
def receiver(data: dict):
    user = data['user']
    message = data['message']
    date = data['date']
    return {"message": f"User {user} send a secret message '{message}' on {date}."}
```

**Problem:** Du kan ikke sikre at data sendt af brugere faktisk overholder data typen du vil have. Fx vil en request body med `user` som string også blive accepteret, men kan forårsage problemer i senere processing.

**Med Pydantic (Løsning):**
```python
from pydantic import BaseModel

class ReceivedData(BaseModel):
    user: int
    message: str
    date: str

@app.post("/receiver")
def receiver(data: ReceivedData):
    user = data.user
    message = data.message
    date = data.date
    return {"message": f"User {user} sent a secret message '{message}' on {date}."}
```

**Fordele:**
- Automatisk type checking
- Hvis request body indeholder invalid data types, vil FastAPI afvise requesten og returnere `422 Unprocessable Content`
- Reusability
- Automatisk dokumentation generation

**Extended Reading:**
- https://data-ai.theodo.com/en/technical-blog/fastapi-pydantic-powerful-duo
- https://www.geeksforgeeks.org/python/fastapi-pydantic/

---

## 🔄 API Versioning

**Hvorfor?**
- Som dækket i "Advanced APIs in the Era of AI", tillader API versioning dig at introducere ændringer uden at bryde eksisterende integrationer
- Særligt vigtigt for AI APIs hvor modeller og features konstant udvikler sig

**Implementering i FastAPI:**
```python
from fastapi import APIRouter
from datetime import datetime

v1_router = APIRouter(prefix="/v1")
v2_router = APIRouter(prefix="/v2")

@v1_router.post("/receiver")
def receiver_v1(data: ReceivedData):
    return {"message": f"User {data.user} sent '{data.message}' on {data.date}"}

@v2_router.post("/receiver")
def receiver_v2(data: ReceivedData):
    return {
        "message": f"User {data.user} sent '{data.message}' on {data.date}",
        "version": "2.0",
        "timestamp": datetime.now().isoformat()
    }

app.include_router(v1_router)
app.include_router(v2_router)
```

**Resultat:**
- Din API understøtter begge versioner samtidigt
- Brugere kan tilgå `/v1/receiver` for original funktionalitet
- `/v2/receiver` giver enhanced features

**Extended Reading:**
- Streaming Protocols
- WebSockets
- MQTT
- Model Context Protocol

---

## 🤖 Build APIs for AI Models

### Barebone Implementation

**Image Classification API Server Eksempel**

**1. Image Classifier Class:**
```python
import asyncio
from PIL import Image
import torch
from transformers import pipeline, AutoImageProcessor, AutoModelForImageClassification

class ImageClassifier:
    def __init__(self):
        self.model = None
        self.processor = None
        self.model_name = "microsoft/resnet-18"
    
    async def load_model(self):
        """Load the image classification model asynchronously"""
        if self.model is None:
            print(f"Loading model: {self.model_name}")
            self.model = AutoModelForImageClassification.from_pretrained(self.model_name)
            self.processor = AutoImageProcessor.from_pretrained(self.model_name)
            print("Model loaded successfully")
    
    async def classify_image(self, image: Image.Image) -> dict:
        """Classify a single image"""
        if self.model is None:
            await self.load_model()
        
        # Process image
        inputs = self.processor(image, return_tensors="pt")
        
        # Run inference
        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits[0], dim=0)
        
        # Get top 5 predictions
        top_predictions = torch.topk(predictions, 5)
        results = []
        
        for score, idx in zip(top_predictions.values, top_predictions.indices):
            label = self.model.config.id2label[idx.item()]
            confidence = score.item()
            results.append({
                "label": label,
                "confidence": round(confidence, 4)
            })
        
        return {
            "predictions": results,
            "model": self.model_name
        }
```

**Note:**
- Vi bruger en meget lightweight image classification model `microsoft/resnet-18` der burde kunne køre på de fleste PCs
- `async` declaration på model loading og inference funktioner
- Sikrer at når serveren loader modellen eller processerer et indkommende billede, kan serveren stadig processere andre requests
- Serveren assigner altid en dedikeret person (thread) til at håndtere en indkommende request
- Hvis den modtager en anden request under processen, kan den assigne en anden person i stedet for at vente på at den forrige person færdiggør deres job

**2. Server App Setup:**
```python
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

# Initialize classifier
classifier = ImageClassifier()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await classifier.load_model()
    yield

app = FastAPI(title="AI Image Classification API", version="1.0.0", lifespan=lifespan)
```

**3. Data Models:**
```python
import base64
import io
from typing import List, Optional
from pydantic import BaseModel

class ImageRequest(BaseModel):
    image: str  # base64 encoded image
    filename: Optional[str] = None

class ClassificationResponse(BaseModel):
    predictions: List[dict]
    model: str

class ModelInfo(BaseModel):
    name: str
    status: str
    num_labels: Optional[int] = None

def decode_base64_image(base64_string: str) -> Image.Image:
    """Decode base64 string to PIL Image"""
    try:
        # Remove data URL prefix if present
        if base64_string.startswith('data:image'):
            base64_string = base64_string.split(',')[1]
        # Decode base64
        image_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
        return image
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid base64 image: {str(e)}")
```

**Note:**
- Vi bruger base64-encoded images så request body er JSON som vi kender

**4. Routes:**
```python
@app.get("/model/info", response_model=ModelInfo)
async def model_info():
    """Get model information"""
    if classifier.model is None:
        return ModelInfo(
            name=classifier.model_name,
            status="not_loaded"
        )
    return ModelInfo(
        name=classifier.model_name,
        status="loaded",
        num_labels=len(classifier.model.config.id2label)
    )

@app.post("/classify", response_model=ClassificationResponse)
async def classify_image(request: ImageRequest):
    """Classify a single base64 encoded image"""
    try:
        # Decode base64 image
        image = decode_base64_image(request.image)
        # Classify image
        result = await classifier.classify_image(image)
        return ClassificationResponse(**result)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
```

---

## 🔐 API Key Authentication

**Problem:**
- Lige nu er vores API server ubeskyttet
- Enhver der kan tilgå din PC kan sende requests og overloade din delicate PC
- Du har ingen idé om hvem der gør det
- Derfor er de fleste APIs beskyttet med authentication (typisk API keys)

**Basic Implementation:**
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # API key validation logic
    if credentials.credentials != "your-secret-api-key":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    return credentials.credentials

@app.post("/classify", response_model=ClassificationResponse)
async def classify_image(request: ImageRequest, api_key: str = Depends(verify_api_key)):
    # Remaining code
```

**Resultat:**
- Kun requests med authentication header `Authorization: Bearer your-secret-api-key` accepteres
- Ellers returneres `401 Unauthorized`

**Begrænsning:**
- API key er hardcoded
- I praksis vil du have en dynamisk liste af API keys, én for hver bruger
- Dette gør det også muligt at identificere hver request og holde styr på brugerens usage

**Extended Reading:**
- https://www.geeksforgeeks.org/python/authentication-and-authorization-with-fastapi/
- https://betterstack.com/community/guides/scaling-python/authentication-fastapi/

---

## 💾 Database Integration

**Hvorfor?**
- En almindelig praksis for at optegne listen af API keys og deres respektive brugere og anden information er gennem databases
- I tidligere AI og data kursus har vi allerede hands-on koncepter af databases og interagerer med databases gennem SQL queries
- Du kan direkte bruge database connectors og integrere SQL queries i din API server
- Men lignende til pydantic library til at håndtere data models, har vi også `sqlalchemy` til at håndtere data models for databases

**SQLAlchemy:**
- Giver high-level interface til at interagere med databases så du ikke behøver at skrive SQL queries selv
- Fokusér på abstract definition og manipulation af data models
- Lignende til pydantic der giver automatisk type verification, giver sqlalchemy også automatisk database initialization og SQL injection protection

**Data Models:**
```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from datetime import datetime
import time

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    api_key = Column(String, unique=True, nullable=False)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    requests = relationship("APIRequest", back_populates="user")

class APIRequest(Base):
    __tablename__ = "api_requests"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    endpoint = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    response_time_ms = Column(Float)
    status_code = Column(Integer)
    user = relationship("User", back_populates="requests")

# Database setup
engine = create_engine("sqlite:///ai_api.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
```

**Note:**
- Vi bruger SQLite som en simpel database til demonstration
- Følgende kode vil oprette databasen og tabeller når du starter serveren for første gang
- En af fordelene ved sqlalchemy: senere hvis du vil flytte til mere performante databases, skal du for det meste bare erstatte database URL og genbruge data model
- sqlalchemy håndterer forskellene mellem databases for dig

**Upgraded API Key Authentication:**
```python
security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.api_key == credentials.credentials).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return user

@app.post("/classify", response_model=ClassificationResponse)
async def classify_image(
    request: ImageRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Remaining code
```

### API Key Identification & Tracking

**Usage Tracking:**
```python
@app.post("/classify", response_model=ClassificationResponse)
async def classify_image(
    request: ImageRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Classify a single base64 encoded image"""
    start_time = time.time()
    try:
        # Classify image (your existing logic)
        image = decode_base64_image(request.image)
        result = await classifier.classify_image(image)
        
        # Log request
        api_request = APIRequest(
            user_id=user.id,
            endpoint="/classify",
            response_time_ms=(time.time() - start_time) * 1000,
            status_code=200
        )
        db.add(api_request)
        db.commit()
        
        return ClassificationResponse(**result)
    except Exception as e:
        # Log failed request
        api_request = APIRequest(
            user_id=user.id,
            endpoint="/classify",
            response_time_ms=(time.time() - start_time) * 1000,
            status_code=500
        )
        db.add(api_request)
        db.commit()
        raise HTTPException(status_code=500, detail=str(e))
```

**Resultat:**
- Når brugere sender requests til vores server, gemmes records i `api_requests` tabellen i vores database

**Usage Status Route:**
```python
@app.get("/usage")
async def get_usage(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    requests = db.query(APIRequest).filter(APIRequest.user_id == user.id).all()
    total = len(requests)
    successful = len([r for r in requests if r.status_code == 200])
    avg_time = sum(r.response_time_ms for r in requests) / total if total > 0 else 0
    
    return {
        "total_requests": total,
        "successful_requests": successful,
        "success_rate": round(successful / total * 100, 2) if total > 0 else 0,
        "avg_response_time_ms": round(avg_time, 2)
    }
```

**Response Eksempel:**
```json
{
    "avg_response_time_ms": 18.87,
    "success_rate": 100.0,
    "successful_requests": 5,
    "total_requests": 5
}
```

---

## ⏱️ Rate Limiting

**Hvorfor?**
- Med API key-based user tracking på plads, kan vi nu implementere rate limiting for hver bruger
- Forhindrer bad actors fra at overloade vores API server

**Simple DIY Implementation:**
```python
from datetime import datetime, timedelta

async def check_rate_limit(user: User, db: Session):
    """Check if user has exceeded their rate limits"""
    now = datetime.utcnow()
    # Check requests in the last minute
    minute_ago = now - timedelta(minutes=1)
    recent_requests = db.query(APIRequest).filter(
        APIRequest.user_id == user.id,
        APIRequest.timestamp >= minute_ago
    ).count()
    
    if recent_requests >= 5:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded: 5 requests per minute"
        )
```

**I Route:**
```python
@app.post("/classify", response_model=ClassificationResponse)
async def classify_image(
    request: ImageRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    await check_rate_limit(user, db)
    # Remaining code
```

**Resultat:**
- Hvis en bruger sender mere end 5 requests inden for ét minut, afvises deres requests med `429 Too Many Requests`

**Note:**
- I praksis vil du måske også gerne optegne brugernes rate limit threshold i User data model i stedet for at hardcode det
- Dette er en "sliding window" tilgang som introduceret i "Advanced APIs in the Era of AI"

**Extended Reading:**
- https://github.com/laurentS/slowapi
- https://github.com/long2ice/fastapi-limiter

---

## 📋 Opsummering til Mini Projekt

### Vigtige Koncepter at Inkludere:

1. **FastAPI Implementation** ✅ (Påkrævet)
   - Brug FastAPI fundamentals dækket i FastAPI Fundamentals
   - Proper route definition
   - Request handling
   - Pydantic data models

2. **AI Model Integration** ✅ (Påkrævet)
   - Integrer en AI model (fx image classification)
   - Følg patterns vist i Build APIs for AI Models
   - Brug en appropriate open-source model der kan køre på dit system
   - Async support for at håndtere multiple requests

3. **API Versioning** ✅ (Påkrævet)
   - Support API versioning ved brug af tilgangen vist i API Versioning
   - Brug APIRouter med prefixes

4. **Authentication System** ✅ (Påkrævet/Anbefalet)
   - Implementer API key authentication som demonstreret i API Key Authentication
   - Beskyt dine endpoints

5. **Database Integration** ⭐ (Optional men anbefalet)
   - Brug database integration teknikker fra Database Integration
   - User (API key) management
   - Usage tracking

6. **Rate Limiting** ⭐ (Optional men anbefalet)
   - Anvend rate limiting koncepter fra Rate Limiting
   - Forhindrer server overload
   - Implementer sliding window eller token bucket algoritme

### Eksempel API Struktur:

```
/api/v1/
  ├── /model/info      # GET - Get model information
  ├── /classify        # POST - Image classification (protected)
  └── /usage           # GET - Get usage stats (protected)

/api/v2/
  └── /classify        # POST - Improved classification (protected)
```

### Implementering Tips:

1. **Start Simple:**
   - Implementer basic FastAPI server først
   - Tilføj AI model integration
   - Tilføj authentication
   - Tilføj database og rate limiting senere

2. **Async Support:**
   - Brug `async`/`await` for AI model operations
   - Sikrer at serveren kan håndtere multiple requests samtidigt

3. **Error Handling:**
   - Proper error handling med HTTPException
   - Informative fejlbeskeder
   - Log failed requests

4. **Data Models:**
   - Brug Pydantic for request/response models
   - Automatisk validation og dokumentation

5. **Database:**
   - Start med SQLite (simpelt)
   - Kan senere flytte til PostgreSQL/MySQL hvis nødvendigt
   - SQLAlchemy gør det let at skifte

6. **Rate Limiting:**
   - Implementer fra start hvis muligt
   - Overvej at gemme rate limit threshold i database
   - Brug sliding window eller token bucket

### Dependencies (requirements.txt):

```
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
sqlalchemy==2.0.23
pillow==10.1.0
torch==2.1.0
transformers==4.35.0
python-multipart==0.0.6
```

### Dockerfile Eksempel:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ✅ Checklist til Mini Projekt

### FastAPI Implementation
- [ ] FastAPI server sat op
- [ ] Proper route definition
- [ ] GET og POST requests håndteret
- [ ] Pydantic data models defineret
- [ ] Error handling implementeret

### AI Model Integration
- [ ] AI model valgt og integreret
- [ ] Async support for model loading og inference
- [ ] Image/data processing funktioner
- [ ] Model info endpoint

### API Versioning
- [ ] APIRouter med prefixes implementeret
- [ ] Mindst v1 og v2 versioner
- [ ] Dokumenteret i rapporten

### Authentication
- [ ] API key authentication implementeret
- [ ] Protected endpoints
- [ ] Proper error messages (401 Unauthorized)

### Database Integration (Optional)
- [ ] SQLAlchemy models defineret
- [ ] User model med API keys
- [ ] APIRequest model til tracking
- [ ] Database initialization
- [ ] Usage tracking i routes

### Rate Limiting (Optional)
- [ ] Rate limiting funktion implementeret
- [ ] Sliding window eller token bucket algoritme
- [ ] Rate limit check i protected routes
- [ ] Proper error messages (429 Too Many Requests)

### Testing
- [ ] Alle endpoints testet
- [ ] Authentication testet
- [ ] Rate limiting testet (hvis implementeret)
- [ ] Error cases håndteret

---

## 🎯 Exercise: Image Classification API Server

**Opgave:** Byg en image classification API server der demonstrerer viden dækket i dette modul, reversér din rolle fra API consumer til producer.

**Krav:**

1. **FastAPI Implementation:**
   - Brug FastAPI fundamentals dækket i FastAPI Fundamentals
   - Inkluder proper route definition, request handling, og Pydantic data models

2. **AI Model Integration:**
   - Integrer en image classification model følgende patterns vist i Build APIs for AI Models
   - Brug en appropriate open-source model der kan køre på dit system

3. **API Versioning:**
   - Support API versioning ved brug af tilgangen vist i API Versioning

4. **Authentication System:**
   - Implementer API key authentication som demonstreret i API Key Authentication
   - Beskyt dine endpoints

5. **Client Integration:**
   - Modificer dit image analysis program fra API Fundamentals til at connecte til din server i stedet for third-party APIs

**Additional Functionalities (Optional):**

6. **Database Integration:**
   - Brug database integration teknikker fra Database Integration
   - User (API key) management
   - Usage tracking

7. **Rate Limiting:**
   - Anvend rate limiting koncepter fra Rate Limiting
   - Forhindrer server overload

---

## 🔗 Ressourcer

### FastAPI
- FastAPI Documentation: https://fastapi.tiangolo.com/
- FastAPI Tutorial: https://fastapi.tiangolo.com/tutorial/

### Pydantic
- Pydantic Documentation: https://docs.pydantic.dev/
- FastAPI + Pydantic: https://data-ai.theodo.com/en/technical-blog/fastapi-pydantic-powerful-duo

### SQLAlchemy
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/
- FastAPI + SQLAlchemy: https://fastapi.tiangolo.com/tutorial/sql-databases/

### Authentication
- FastAPI Security: https://fastapi.tiangolo.com/tutorial/security/
- Authentication Guide: https://www.geeksforgeeks.org/python/authentication-and-authorization-with-fastapi/

### Rate Limiting
- slowapi: https://github.com/laurentS/slowapi
- fastapi-limiter: https://github.com/long2ice/fastapi-limiter

### HuggingFace Models
- Transformers Library: https://huggingface.co/docs/transformers/
- Image Classification Models: https://huggingface.co/models?pipeline_tag=image-classification

