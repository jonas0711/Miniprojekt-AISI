# TODO Liste - Mini Projekt AI Systems & Infrastructure

**Deadline:** 4. december 2025 kl. 23:59 (Copenhagen time)  
**Status:** 3/33 opgaver færdige (9%)

---

## ✅ Færdige Opgaver (3)

### Setup & Infrastructure
- [x] **EC2 Server opsætning** - SSH nøgler, SSH config, SSHFS scripts
- [x] **Verificer Docker og Python** - Installeret på EC2 serveren (Docker 29.1.1, Python 3.12.3)
- [x] **Dokumentation** - Guides og kravspecifikation oprettet

---

## 📋 Opgaver der Mangler (36)

### 1. API Server Implementation (15 opgaver)

#### Planlægning (Baseret på Modul 1, 2, 3)
- [ ] **Planlæg API server routes** - Mindst 2 routes, hvoraf mindst 1 med AI funktionalitet
- [ ] **Vælg AI model(ler)** - Fra HuggingFace (fx ResNet-18 til image classification - CPU-friendly)
- [ ] **Design API struktur** - Følg REST principper (GET, POST, PUT, DELETE) fra Modul 1 & 2

#### FastAPI Fundamentals (Modul 3)
- [ ] **Opret FastAPI projekt struktur** - main.py med FastAPI app, uvicorn server
- [ ] **Implementer Pydantic data models** - Request/response models med automatisk validation
- [ ] **Implementer async support** - Brug async/await for AI model operations (vigtigt fra Modul 3)

#### Routes & Endpoints (Modul 3)
- [ ] **Implementer mindst én AI endpoint** - Fx `/v1/image_classify` (POST) eller `/v1/conversation` (POST)
- [ ] **Implementer yderligere routes** - Fx `/v1/model/info` (GET), `/v1/health` (GET), `/v1/usage` (GET)
- [ ] **Implementer API versioning** - Med APIRouter og prefixes (fx `/v1/`, `/v2/`) - PÅKRÆVET fra Modul 1 & 2
- [ ] **Implementer error handling** - HTTPException med proper status codes (200, 400, 401, 429, 500) - PÅKRÆVET fra Modul 2

#### Authentication & Security (Modul 3)
- [ ] **Implementer authentication** - API key authentication med HTTPBearer - PÅKRÆVET/ANBEFALET fra Modul 3
- [ ] **Implementer protected endpoints** - Beskyt AI endpoints med authentication dependency

#### Database Integration (Modul 3 - Anbefalet)
- [ ] **Opret SQLAlchemy models** - User model (id, api_key, email, created_at) og APIRequest model (usage tracking)
- [ ] **Implementer database setup** - SQLite database med engine, SessionLocal, Base.metadata.create_all
- [ ] **Implementer usage tracking** - Log alle API requests med timestamp, response_time_ms, status_code

#### Rate Limiting (Modul 1 & 2 - Anbefalet)
- [ ] **Implementer rate limiting** - Sliding window eller token bucket algoritme - ANBEFALET fra Modul 1 & 2
- [ ] **Rate limit check i routes** - Check rate limits før AI model inference, return 429 ved overskridelse

---

### 2. Docker Setup (4 opgaver) - Modul 5

- [ ] **Opret Dockerfile** - Med proper layering fra Modul 5:
  - FROM python:3.11-slim (base layer)
  - WORKDIR /app
  - COPY requirements.txt først (for layer caching)
  - RUN pip install --no-cache-dir -r requirements.txt (dependency layer)
  - COPY . . (application layer)
  - EXPOSE 8000
  - CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
- [ ] **Opret requirements.txt** - Med alle dependencies:
  - fastapi==0.104.1
  - uvicorn[standard]==0.24.0
  - pydantic==2.5.0
  - sqlalchemy==2.0.23 (hvis database)
  - transformers==4.35.0
  - torch==2.1.0
  - pillow==10.1.0
  - python-multipart==0.0.6
- [ ] **Opret .dockerignore** - Exclude __pycache__, *.pyc, .env, venv/, *.db, .git (anbefalet fra Modul 5)
- [ ] **Test Docker build lokalt** - `docker build -t ai-api-server:v1.0 .` og test med `docker run -p 8000:8000`

---

### 3. Deployment på EC2 (7 opgaver) - Modul 6

- [ ] **Upload kode til EC2 serveren** - Via SSHFS (`./mount_ec2.sh`) eller SCP
- [ ] **Build container på EC2** - `docker build -t ai-api-server:v1.0 .` på serveren
- [ ] **Konfigurer AWS security groups** - Åbn port 8000 (og 22 for SSH) i AWS console - PÅKRÆVET fra Modul 6
- [ ] **Konfigurer UFW firewall** - `sudo ufw allow 8000/tcp` på serveren (ekstra lag af beskyttelse)
- [ ] **Kør container på EC2** - Med `--restart unless-stopped` og port mapping:
  - `docker run -d -p 8000:8000 --restart unless-stopped --name ai-api ai-api-server:v1.0`
  - Hvis database: `-v ~/ai-data:/app/data` for persistent data
- [ ] **Test API fra serveren** - Lokalt med `curl http://localhost:8000` og `curl http://localhost:8000/v1/health`
- [ ] **Sæt HTTPS op** - Med domain, DNS records, Nginx + Certbot eller Traefik (optional achievement fra Modul 6)

---

### 4. Klientprogram (3 opgaver) - Modul 1 & 3

- [ ] **Opret klientprogram** - Python script der kan kalde API serveren (fx med requests library)
- [ ] **Implementer API kald** - Test alle endpoints (GET /v1/model/info, POST /v1/image_classify, etc.)
- [ ] **Test klient fra lokal maskine** - Mod serveren på EC2 (demonstrerer forskellige host environments)

---

### 5. Rapport (5 opgaver)

- [ ] **Skriv Introduction** - Med problem analyse
- [ ] **Skriv Implementation sektion** - API server + klient design valg
- [ ] **Skriv Deployment sektion** - Vigtige steps i deployment
- [ ] **Skriv Results sektion** - Evaluering og reflektioner
- [ ] **Skriv Conclusion** - Afsluttende konklusion

**Rapport krav:** 3-4 sider (ekskl. referencer)

---

### 6. Submission (2 opgaver)

- [ ] **Pak alle filer** - Rapport PDF, kildekode, Dockerfile, requirements.txt, klient i .zip/.tar.gz
- [ ] **Upload til DigitalExam** - Før deadline (4. dec 2025 kl. 23:59)

---

## 📊 Status Oversigt

| Kategori | Færdige | Mangler | Total |
|----------|---------|---------|-------|
| Setup & Infrastructure | 3 | 0 | 3 |
| API Server Implementation | 0 | 15 | 15 |
| Docker Setup | 0 | 4 | 4 |
| Deployment på EC2 | 0 | 7 | 7 |
| Klientprogram | 0 | 3 | 3 |
| Rapport | 0 | 5 | 5 |
| Submission | 0 | 2 | 2 |
| **TOTAL** | **3** | **36** | **39** |

**Procent færdig:** 8% (3/39)

---

## 🎯 Næste Skridt (Prioriteret)

1. **Planlæg API server routes** - Bestem hvilke endpoints der skal implementeres
2. **Vælg AI model(ler)** - Fx ResNet-18 til image classification
3. **Opret FastAPI projekt** - Grundlæggende struktur
4. **Implementer AI endpoint** - Første funktionelle endpoint

---

## 📝 Noter

### Server Information
- **EC2 IP:** 51.21.200.191
- **SSH Alias:** `ssh ec2`
- **Docker:** 29.1.1 (installeret)
- **Python:** 3.12.3 (installeret)
- **Status:** Server klar til deployment

### Vigtige Krav
- ✅ Server og klient på forskellige host environments (EC2 + lokal PC)
- ✅ Containerization påkrævet (Docker)
- ✅ Mindst 2 routes, hvoraf mindst 1 med AI funktionalitet
- ✅ FastAPI anbefalet
- ✅ Forståelse af koden påkrævet

### Anbefalede Features (Baseret på Undervisning)

#### Fra Modul 1 & 2 (Påkrævet/Anbefalet):
- ✅ **API versioning** (`/v1/`, `/v2/`) - PÅKRÆVET, URL path versioning
- ✅ **REST principper** - Proper HTTP metoder (GET, POST, PUT, DELETE) - PÅKRÆVET
- ✅ **Rate limiting** - Sliding window eller token bucket - ANBEFALET
- ✅ **Error handling** - Proper status codes (200, 400, 401, 429, 500) - PÅKRÆVET
- ⭐ **Streaming support** - SSE for conversational endpoints (optional)

#### Fra Modul 3 (Påkrævet/Anbefalet):
- ✅ **Pydantic data models** - Request/response validation - PÅKRÆVET
- ✅ **Async support** - async/await for AI model operations - PÅKRÆVET
- ✅ **Authentication** - API key med HTTPBearer - PÅKRÆVET/ANBEFALET
- ✅ **Database integration** - SQLAlchemy til user management og usage tracking - ANBEFALET

#### Fra Modul 5 (Påkrævet):
- ✅ **Dockerfile layering** - Proper layer caching (requirements først) - PÅKRÆVET
- ✅ **.dockerignore** - Exclude unødvendige filer - ANBEFALET

#### Fra Modul 6 (Påkrævet/Optional):
- ✅ **Security groups** - Konfigurer AWS firewall - PÅKRÆVET
- ✅ **UFW firewall** - Ekstra lag af beskyttelse - ANBEFALET
- ⭐ **HTTPS setup** - Domain, DNS, SSL certifikat (optional achievement)

---

---

## 📚 Referencer til Undervisning

### Modul 1 & 2: API Fundamentals
- API versioning (URL path versioning) - **PÅKRÆVET**
- Rate limiting (sliding window, token bucket) - **ANBEFALET**
- REST principper - **PÅKRÆVET**
- Error handling med proper status codes - **PÅKRÆVET**

### Modul 3: Wrap AI Models with APIs
- FastAPI fundamentals (routes, Pydantic, async)
- API versioning med APIRouter
- Authentication med HTTPBearer - **PÅKRÆVET/ANBEFALET**
- Database integration med SQLAlchemy - **ANBEFALET**
- Usage tracking i database

### Modul 5: Packaging & Containerization
- Dockerfile med proper layering - **PÅKRÆVET**
- Layer caching strategi (requirements først)
- .dockerignore best practices - **ANBEFALET**

### Modul 6: Cloud Deployment
- AWS security groups konfiguration - **PÅKRÆVET**
- UFW firewall setup - **ANBEFALET**
- Container persistence (`--restart unless-stopped`)
- HTTPS setup (optional achievement)

---

**Sidst opdateret:** 3. december 2025  
**Baseret på:** Modul 1, 2, 3, 5, 6 fra AI Systems & Infrastructure kursus

