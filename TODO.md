# TODO Liste - Mini Projekt AI Systems & Infrastructure

**Deadline:** 4. december 2025 kl. 23:59 (Copenhagen time)  
**Status:** 11/26 opgaver færdige (42%) - KUN PÅKRÆVET  
**Model:** CIFAR-10 (10 klasser image classification)  
**Server:** EC2 (51.21.200.191)

---

## ✅ Færdige Opgaver (11)

### Setup & Infrastructure
- [x] **EC2 Server opsætning** - SSH nøgler, SSH config, SSHFS scripts
- [x] **Verificer Docker og Python** - Installeret på EC2 serveren (Docker 29.1.1, Python 3.12.3)
- [x] **Dokumentation** - Guides og kravspecifikation oprettet

### API Server Implementation (Jonas)
- [x] **Opret FastAPI projekt struktur** - `main.py` med FastAPI app, uvicorn server
- [x] **Implementer CIFAR-10 image classification endpoint** - POST `/image_classify`
- [x] **Implementer mindst én ekstra route** - GET `/health` og GET `/model/info`
- [x] **Opret requirements.txt** - Dependencies for CIFAR-10

### Klientprogram (Jonas)
- [x] **Opret klientprogram** - Python script (`client.py`) med requests library
- [x] **Implementer API kald** - GET `/health` og POST `/image_classify`

### Docker Setup (Peter/Jonas)
- [x] **Opret Dockerfile** - Containerization er PÅKRÆVET ✅

---

## 📋 Opgaver der Mangler - KUN PÅKRÆVET

### 1. API Server Implementation (PÅKRÆVET) ✅ FÆRDIG

#### Planlægning ✅
- [x] **Planlæg API server routes** - Mindst 2 routes, hvoraf mindst 1 med AI funktionalitet ✅
  - Route 1: `/image_classify` (POST) - CIFAR-10 image classification (AI funktionalitet) ✅
  - Route 2: `/health` (GET) og `/model/info` (GET) - Utility routes ✅
- [x] **Forbered CIFAR-10 model** - Vælg implementation (PyTorch torchvision) ✅

#### FastAPI Implementation ✅
- [x] **Opret FastAPI projekt struktur** - `main.py` med FastAPI app, uvicorn server ✅
- [x] **Implementer CIFAR-10 image classification endpoint** - POST `/image_classify` ✅
  - Modtag base64 encoded image ✅
  - Load CIFAR-10 model (ResNet-18 modificeret til 10 klasser) ✅
  - Preprocess image til CIFAR-10 format (32x32 RGB) ✅
  - Kør inference ✅
  - Return top predictions med confidence scores ✅
- [x] **Implementer mindst én ekstra route** - GET `/health` og GET `/model/info` ✅
  - `/health`: Return server status ✅
  - `/model/info`: Return model information (CIFAR-10, 10 classes) ✅
- [x] **Forståelse af koden** - Skal kunne forklare CIFAR-10 model og API implementation ✅

---

### 2. Docker Setup (PÅKRÆVET)

**Note:** `requirements.txt` er en del af API Server Implementation (Jonas), men Dockerfile bruger den.

- [ ] **Opret Dockerfile** - Containerization er PÅKRÆVET (modul 5)
  - FROM python:3.11-slim
  - WORKDIR /app
  - COPY requirements.txt .
  - RUN pip install --no-cache-dir -r requirements.txt
  - COPY . .
  - EXPOSE 8000
  - CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
- [x] **Test Docker build lokalt** - `docker build -t cifar10-api:v1.0 .` og test med `docker run -p 8000:8000`
- [x] **Verificer container virker** - Test at API serveren kører korrekt i container

---

### 3. Deployment på EC2 (PÅKRÆVET)

- [ ] **Upload kode til EC2 serveren** - Via SSHFS (`./mount_ec2.sh`) eller SCP til `/home/ubuntu/`
- [ ] **Build container på EC2** - `docker build -t cifar10-api:v1.0 .` på serveren
- [ ] **Kør container på EC2** - Med port mapping:
  - `docker run -d -p 8000:8000 --restart unless-stopped --name cifar10-api cifar10-api:v1.0`
- [ ] **Test API fra serveren** - Lokalt med `curl http://localhost:8000/health` og verificer serveren kører
- [ ] **Verificer forskellige host environments** - Server på EC2 (51.21.200.191), klient på lokal PC (PÅKRÆVET)

---

### 4. Klientprogram (PÅKRÆVET)

- [x] **Opret klientprogram** - Python script (`client.py`) der kan kalde API serveren ✅
- [x] **Implementer API kald** - Test endpoints: ✅
  - GET `/health` - Tjek server status ✅
  - POST `/image_classify` - Send billede og få CIFAR-10 predictions ✅
- [ ] **Test klient fra lokal maskine** - Mod serveren på EC2 (51.21.200.191:8000) - PÅKRÆVET (forskellige host environments)

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

## 📊 Status Oversigt - KUN PÅKRÆVET

| Kategori | Færdige | Mangler | Total | Ansvar |
|----------|---------|---------|-------|--------|
| Setup & Infrastructure | 3 ✅ | 0 | 3 | Begge |
| API Server Implementation | 0 | 5 | 5 | Jonas |
| Docker Setup | 2 ✅ | 1 | 3 | Peter |
| Deployment på EC2 | 0 | 4 | 4 | Peter |
| Klientprogram | 0 | 3 | 3 | Jonas |
| Rapport | 0 | 5 | 5 | Begge |
| Submission | 0 | 2 | 2 | Begge |
| **TOTAL** | **5** | **20** | **25** | |

**Procent færdig:** 20% (5/25)

**Fordeling:**
- **Jonas:** 8 opgaver (API + Klient)
- **Peter:** 7 opgaver (Docker + Deployment)
- **Begge:** 4 opgaver (Planlægning + Rapport + Submission)

**Note:** Kun påkrævede opgaver er inkluderet. Tips og optional achievements er fjernet.

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

### Klassificering baseret på Miniprojekt Krav

#### ✅ PÅKRÆVET (Minimum for at opfylde krav):
- **API Server:** Mindst 2 routes, hvoraf mindst 1 med AI funktionalitet
- **FastAPI:** Framework (anbefalet)
- **AI Model:** Fra HuggingFace eller anden kilde
- **Containerization:** Docker (PÅKRÆVET)
- **Dockerfile:** Med proper layering (TIP)
- **Deployment:** Server og klient på forskellige host environments (PÅKRÆVET)
- **Klientprogram:** Kan demonstrere serverens funktionalitet

#### 💡 TIPS (Anbefalet men ikke påkrævet):
- **REST principper** - API endpoints design
- **API versioning** - Overvej versionering, selv hvis kun v1
- **Database integration** - API key management
- **Dockerfile layering** - Proper layering
- **Authentication** - API key management (hvis database implementeres)

#### 🚀 OPTIONAL ACHIEVEMENTS (Ekstra features):
- **Rate limiting** - Avanceret rate limit algoritme
- **Public access** - Domain navn, SSL certifikat
- **High availability** - Avancerede deployment strategier

---

---

## 📚 Referencer til Undervisning

### Modul 1 & 2: API Fundamentals
- API versioning (URL path versioning) - **TIP** (ikke påkrævet, men anbefalet)
- Rate limiting (sliding window, token bucket) - **OPTIONAL ACHIEVEMENT**
- REST principper - **TIP** (anbefalet)
- Error handling med proper status codes - **TIP** (anbefalet)

### Modul 3: Wrap AI Models with APIs
- FastAPI fundamentals (routes, Pydantic, async) - **PÅKRÆVET** (FastAPI er anbefalet framework)
- API versioning med APIRouter - **TIP** (ikke påkrævet)
- Authentication med HTTPBearer - **TIP** (ikke påkrævet)
- Database integration med SQLAlchemy - **TIP** (ikke påkrævet)
- Usage tracking i database - **TIP** (ikke påkrævet)

### Modul 5: Packaging & Containerization
- Dockerfile - **PÅKRÆVET** (containerization er påkrævet)
- Dockerfile med proper layering - **TIP** (anbefalet)
- Layer caching strategi (requirements først) - **TIP** (anbefalet)
- .dockerignore best practices - **TIP** (anbefalet)

### Modul 6: Cloud Deployment
- AWS security groups konfiguration - **TIP** (anbefalet, men ikke eksplicit påkrævet)
- UFW firewall setup - **TIP** (anbefalet)
- Container persistence (`--restart unless-stopped`) - **TIP** (anbefalet)
- HTTPS setup - **OPTIONAL ACHIEVEMENT**

---

---

## 👥 Opdeling mellem Peter og Jonas - Ligelig Fordeling

### FASE 1: Planlægning (Sammen - Fælles beslutninger) 🔄

**Begge skal være med (1 opgave):**
- [ ] **Planlæg API server routes og CIFAR-10 model** - Diskuter sammen:
  - Route 1: `/image_classify` (POST) - CIFAR-10 classification (AI funktionalitet) ✅
  - Route 2: `/health` (GET) eller `/model/info` (GET) - Utility route ✅
  - CIFAR-10 implementation: PyTorch torchvision eller HuggingFace

**Hvorfor sammen:** Disse er fundamentale design beslutninger der påvirker hele projektet.

---

### FASE 2: API Server Implementation (Opdelt arbejde) 🔀

#### Jonas - FastAPI & CIFAR-10 Backend (5 opgaver)
- [x] **Opret FastAPI projekt struktur** - `main.py` med FastAPI app, uvicorn server ✅
- [x] **Implementer CIFAR-10 image classification endpoint** - POST `/image_classify` ✅
  - Load CIFAR-10 model (fx `torchvision.models` eller pretrained) ✅
  - Modtag image (base64 eller file upload) ✅
  - Preprocess image til CIFAR-10 format (32x32 RGB) ✅
  - Kør inference ✅
  - Return top predictions med confidence scores ✅
- [x] **Implementer mindst én ekstra route** - GET `/health` eller GET `/model/info` ✅
  - `/health`: Return server status ✅
  - `/model/info`: Return CIFAR-10 model information (10 classes) ✅
- [x] **Opret requirements.txt** - Dependencies for CIFAR-10 ✅
- [x] **Forståelse af koden** - Skal kunne forklare CIFAR-10 model og API implementation ✅

**Jonas' filer (arbejder uafhængigt):**
- `main.py` (hovedfil med FastAPI app og routes)
- `requirements.txt`
- Eventuelt `cifar10_model.py` (CIFAR-10 model loading og inference)

---

### FASE 3: Docker & Deployment (Opdelt arbejde) 🐳

#### Peter - Docker Setup (3 opgaver)
- [x] **Opret Dockerfile** - Containerization er PÅKRÆVET ✅
  - FROM python:3.11-slim ✅
  - WORKDIR /app ✅
  - COPY requirements.txt . ✅
  - RUN pip install --no-cache-dir -r requirements.txt ✅
  - COPY . . ✅
  - EXPOSE 8000 ✅
  - CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] ✅
- [x] **Test Docker build lokalt** - `docker build -t cifar10-api:v1.0 .` og test med `docker run -p 8000:8000`
- [x] **Verificer CIFAR-10 model virker i container** - Test image classification lokalt i container

**Peter's filer (arbejder uafhængigt):**
- `Dockerfile`
- Eventuelt `.dockerignore` (optional)

#### Peter - EC2 Deployment (4 opgaver)
- [x] **Upload kode til EC2 serveren** - Via SSHFS (`./mount_ec2.sh`) eller SCP til `/home/ubuntu/` ✅
  - **Note:** Kun Jonas' filer er uploadet: `main.py` og `requirements.txt` ✅
- [ ] **Build container på EC2** - `docker build -t cifar10-api:v1.0 .` på serveren
- [ ] **Kør container på EC2** - Med port mapping:
  - `docker run -d -p 8000:8000 --restart unless-stopped --name cifar10-api cifar10-api:v1.0`
- [ ] **Test API fra serveren** - Lokalt på EC2 med `curl http://localhost:8000/health` og `curl http://localhost:8000/model/info`

**Peter's område (arbejder uafhængigt):**
- EC2 server deployment
- Container management på serveren
- Server-side testing

**Hvorfor Peter:**
- Har AWS adgang og kan deploye
- Håndterer hele deployment processen

---

### FASE 4: Klientprogram & Verifikation (Opdelt arbejde) 🧪

#### Jonas - Klientprogram (3 opgaver)
- [x] **Opret klientprogram** - Python script (`client.py`) med requests library ✅
- [x] **Implementer API kald** - Test endpoints: ✅
  - GET `/health` - Tjek server status ✅
  - POST `/image_classify` - Send billede og få CIFAR-10 predictions ✅
- [ ] **Test klient fra lokal maskine** - Mod serveren på EC2 (51.21.200.191:8000) - PÅKRÆVET

**Jonas' filer (arbejder uafhængigt):**
- `client.py`

**Jonas' område:**
- Klientprogram implementation
- Test fra lokal PC mod EC2 server
- Demonstrerer forskellige host environments (lokal PC → EC2 server)

**Hvorfor Jonas:**
- Jonas har implementeret API'en, så han kender endpoints bedst
- Kan teste sin egen implementation

---

### FASE 5: Rapport (Opdelt arbejde) 📝

#### Jonas - Implementation Sektion (1 opgave)
- [ ] **Skriv Implementation sektion** - API server design valg og klient
  - Forklar CIFAR-10 model valg og implementation
  - Forklar FastAPI routes (`/image_classify`, `/health` eller `/model/info`)
  - Forklar klientprogram implementation

**Jonas' område:**
- Implementation sektion i rapporten
- Forklarer sin egen kode

#### Peter - Deployment Sektion (1 opgave)
- [ ] **Skriv Deployment sektion** - Vigtige steps i deployment
  - Docker containerization
  - EC2 deployment process
  - Verificering af forskellige host environments

**Peter's område:**
- Deployment sektion i rapporten
- Forklarer sin egen deployment process

#### Begge - Fælles Sektioner (3 opgaver)
- [ ] **Skriv Introduction** - Problem analyse (sammen eller hver sin del)
- [ ] **Skriv Results sektion** - Evaluering og reflektioner (sammen)
  - Test CIFAR-10 classification accuracy
  - API response times
  - Deployment succes
- [ ] **Skriv Conclusion** - Afsluttende konklusion (sammen)

**Rapport struktur (3-4 sider):**
- Title og forfattere (Peter og Jonas)
- Introduction: Begge bidrager (kan dele op)
- Implementation: Jonas (API server + klient + CIFAR-10)
- Deployment: Peter (Docker + EC2)
- Results: Begge (sammen evaluering)
- Conclusion: Begge (sammen)

---

### FASE 6: Submission (Sammen) 📦

- [ ] **Pak alle filer** - Rapport PDF, kildekode, Dockerfile, requirements.txt, klient
- [ ] **Upload til DigitalExam** - Før deadline (4. dec 2025 kl. 23:59)

---

## 🔄 Git Workflow - Undgå Merge Conflicts

### Branch Strategi:
1. **`main`** - Production ready kode
2. **`jonas/cifar10-api`** - Jonas' API implementation
3. **`peter/docker`** - Peter's Docker setup

### Arbejdsflow (Ingen Overlap):
1. **FASE 1:** Begge på `main` (planlægning) - commit sammen
2. **FASE 2:** 
   - **Jonas:** `git checkout -b jonas/cifar10-api`
     - Arbejder på: `main.py`, `requirements.txt`, eventuelt `cifar10_model.py`
     - Commit ofte: `git add main.py requirements.txt && git commit -m "Add CIFAR-10 API"`
     - Push: `git push origin jonas/cifar10-api`
   - **Peter:** Vent til Jonas har committet `requirements.txt`, derefter:
     - `git checkout -b peter/docker`
     - Arbejder på: `Dockerfile`, eventuelt `.dockerignore`
     - Commit: `git add Dockerfile && git commit -m "Add Dockerfile"`
     - Push: `git push origin peter/docker`
3. **Merge (ingen conflicts fordi forskellige filer):**
   - Jonas merges først: `git checkout main && git merge jonas/cifar10-api`
   - Peter merges derefter: `git checkout main && git merge peter/docker`
   - Push: `git push origin main`
4. **FASE 3:**
   - **Peter:** Arbejder på `main` eller egen branch for deployment
   - Upload til EC2, build, kør container
5. **FASE 4:**
   - **Jonas:** Arbejder på `main` eller egen branch for klient
   - Opretter `client.py` (ingen overlap med Peter's filer)

### Kommunikation:
- **Daily sync:** Diskuter hvilke filer I arbejder på
- **Before merge:** Tjek `git status` og `git diff` før merge
- **Koordiner:** Peter venter til Jonas har `requirements.txt` før Docker
- **Ingen overlap:** Hver sin filer - ingen merge conflicts!

---

## 📊 Opgave Oversigt per Person - Ligelig Fordeling

| Person | Opgaver | Fokusområde |
|--------|---------|-------------|
| **Jonas** | 9 opgaver | FastAPI + CIFAR-10 Backend (5), Klientprogram (3), Implementation rapport (1) |
| **Peter** | 7 opgaver | Docker Setup (3), EC2 Deployment (4), Deployment rapport (1) |
| **Begge** | 4 opgaver | Planlægning (1), Rapport (Introduction/Results/Conclusion) (3), Submission (2) |

**Total påkrævede opgaver:** 20 (3 allerede færdige = 23 total)

**Fordeling:** 9 + 7 + 4 = 20 opgaver (mere ligeligt fordelt)

---

## ⚠️ Vigtige Noter

1. **CIFAR-10 Model:** 
   - 10 klasser: airplane, car, bird, cat, deer, dog, frog, horse, ship, truck
   - Input: 32x32 RGB billede
   - Kan bruge `torchvision.models` eller pretrained CIFAR-10 model
   - CPU-friendly (perfekt til EC2 serveren uden GPU)

2. **Ingen Overlap - Hver sin filer:**
   - **Jonas' filer:** `main.py`, `requirements.txt`, `client.py`, eventuelt `cifar10_model.py`
   - **Peter's filer:** `Dockerfile`, eventuelt `.dockerignore`
   - **Fælles:** Planlægning, Rapport sektioner, Submission

3. **Arbejdsflow:**
   - Jonas starter med FastAPI + CIFAR-10 (committer `requirements.txt` først)
   - Peter laver Dockerfile (efter `requirements.txt` er klar)
   - Ingen overlap = ingen merge conflicts!

4. **Communication:** Diskuter API interface før implementation
5. **Testing:** Test lokalt før deployment
6. **Backup:** Commit ofte, push til GitHub regelmæssigt
7. **AWS adgang:** Begge har adgang - kan hjælpe hinanden hvis nødvendigt
8. **EC2 server:** Koordiner deployment - ikke deploy samtidigt!
9. **EC2 IP:** 51.21.200.191 - Klient skal connecte til denne adresse

---

**Sidst opdateret:** 3. december 2025  
**Baseret på:** Modul 1, 2, 3, 5, 6 fra AI Systems & Infrastructure kursus

