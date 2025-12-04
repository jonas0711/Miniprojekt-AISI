# Submission Checklist - Miniprojekt AISI

**Deadline:** 4. december 2025 kl. 23:59 (Copenhagen time)
**Upload til:** DigitalExam
**Format:** `.zip` eller `.tar.gz`

---

## 📦 Filer der Skal Medtages

### 1. Rapport (PDF) - PÅKRÆVET ✅

**Filnavn:** `rapport.pdf` eller `miniprojekt_rapport.pdf`

**Indhold (3-4 sider ekskl. referencer):**
- ✅ Title og alle forfattere (Peter + Jonas)
- ✅ Introduction (problem analyse)
- ✅ Implementation (API server + klient design valg)
- ✅ Deployment (vigtige steps i deployment)
- [ ] Results (evaluering og reflektioner)
- [ ] Conclusion (afsluttende konklusion)

**Status:**
- ✅ Introduction skrevet (`docs/report/RAPPORT_INTRODUCTION.md`)
- ✅ Implementation skrevet (`docs/report/RAPPORT_IMPLEMENTATION.md`)
- ✅ Deployment skrevet (`docs/deployment/peter_deploy.md`)
- [ ] Results (mangler)
- [ ] Conclusion (mangler)
- [ ] Kombineret til én PDF fil

---

### 2. API Server Kildekode - PÅKRÆVET ✅

#### `main.py` - FastAPI Server
- ✅ FastAPI app med alle routes
- ✅ CIFAR-10 image classification endpoint (`POST /image_classify`)
- ✅ Health endpoint (`GET /health`)
- ✅ Model info endpoint (`GET /model/info`)
- ✅ Pydantic models for request/response
- ✅ Async support

**Status:** ✅ FÆRDIG (Jonas)

---

### 3. Containerization Filer - PÅKRÆVET ✅

#### `Dockerfile` - Docker Container Setup
- ✅ FROM python:3.11-slim
- ✅ WORKDIR /app
- ✅ COPY requirements.txt + RUN pip install
- ✅ COPY application code
- ✅ EXPOSE 8000
- ✅ CMD uvicorn server

**Status:** ✅ FÆRDIG (Peter)

#### `requirements.txt` - Python Dependencies
- ✅ fastapi==0.104.1
- ✅ uvicorn[standard]==0.24.0
- ✅ python-multipart==0.0.6
- ✅ pydantic==2.5.0
- ✅ requests==2.31.0
- ✅ pillow==10.1.0
- ✅ torch==2.1.0
- ✅ torchvision==0.16.0
- ✅ numpy<2

**Status:** ✅ FÆRDIG (Jonas)

---

### 4. Klientprogram - PÅKRÆVET ✅

#### `client.py` - Klient til API Test
- ✅ Python script med requests library
- ✅ Kan kalde `/health` endpoint
- ✅ Kan kalde `/image_classify` endpoint
- ✅ Demonstrerer API funktionalitet
- ✅ Test mod EC2 server (51.21.200.191:8000)

**Status:** ✅ FÆRDIG (Jonas)

---

### 5. Ekstra Filer (Anbefalet) 🌟

#### `.dockerignore` - Docker Best Practice
- ✅ Ekskluderer unødvendige filer fra Docker image
- ✅ Python cache, virtual environments, docs, etc.

**Status:** ✅ FÆRDIG (Peter)

#### `README.md` - Projekt Dokumentation (Optional)
- ✅ Projekt beskrivelse
- ✅ Hurtig start guide
- ✅ API endpoints dokumentation

**Status:** ✅ FÆRDIG (Begge)

---

## 📁 Fil Struktur i Submission

```
miniprojekt_submission.zip
├── rapport.pdf                # Rapport (3-4 sider)
├── main.py                    # API server kildekode
├── client.py                  # Klientprogram
├── Dockerfile                 # Container setup
├── requirements.txt           # Python dependencies
├── .dockerignore              # Docker ignore fil (optional)
└── README.md                  # Projekt dokumentation (optional)
```

---

## ✅ Submission Checklist

### Før Pakning:
- [ ] **Rapport er færdig** - Alle sektioner skrevet (Introduction, Implementation, Deployment, Results, Conclusion)
- [ ] **Rapport konverteret til PDF** - Fra Markdown til PDF format
- [ ] **Alle filer er testet** - Verificer at koden virker
- [ ] **Docker build virker** - Test `docker build -t cifar10-api:v1.0 .`
- [ ] **API kører i container** - Test `docker run -p 8000:8000 cifar10-api:v1.0`
- [ ] **Klient virker** - Test `python client.py` mod EC2 server

### Pakning:
- [ ] **Opret submission mappe** - `mkdir miniprojekt_submission`
- [ ] **Kopier alle påkrævede filer** til submission mappen:
  ```bash
  cp rapport.pdf miniprojekt_submission/
  cp main.py miniprojekt_submission/
  cp client.py miniprojekt_submission/
  cp Dockerfile miniprojekt_submission/
  cp requirements.txt miniprojekt_submission/
  cp .dockerignore miniprojekt_submission/  # optional
  cp README.md miniprojekt_submission/      # optional
  ```
- [ ] **Pak filer** - Zip eller tar.gz:
  ```bash
  # Option 1: ZIP
  zip -r miniprojekt_submission.zip miniprojekt_submission/

  # Option 2: TAR.GZ
  tar -czf miniprojekt_submission.tar.gz miniprojekt_submission/
  ```
- [ ] **Verificer arkiv** - Test at det kan udpakkes:
  ```bash
  # Test ZIP
  unzip -l miniprojekt_submission.zip

  # Test TAR.GZ
  tar -tzf miniprojekt_submission.tar.gz
  ```

### Upload:
- [ ] **Log ind på DigitalExam** - Før deadline
- [ ] **Upload submission fil** - `miniprojekt_submission.zip` eller `.tar.gz`
- [ ] **Verificer upload** - Tjek at filen er uploadet korrekt
- [ ] **Deadline tjek** - Før 4. december 2025 kl. 23:59 (Copenhagen time)

---

## 📊 Status Oversigt

| Fil | Status | Ansvarlig | Note |
|-----|--------|-----------|------|
| **rapport.pdf** | ⏳ Mangler | Begge | 3/5 sektioner færdige (Introduction, Implementation, Deployment) |
| **main.py** | ✅ FÆRDIG | Jonas | API server med CIFAR-10 |
| **client.py** | ✅ FÆRDIG | Jonas | Klientprogram testet mod EC2 |
| **Dockerfile** | ✅ FÆRDIG | Peter | Proper layering (Modul 5) |
| **requirements.txt** | ✅ FÆRDIG | Jonas | Alle dependencies inkluderet |
| **.dockerignore** | ✅ FÆRDIG | Peter | Best practice (optional) |
| **README.md** | ✅ FÆRDIG | Begge | Projekt dokumentation (optional) |

**Samlet Status:** 6/7 filer færdige (86%)
**Mangler:** Rapport PDF (Results + Conclusion sektioner)

---

## 🚨 VIGTIG INFORMATION

### Deadline:
- **Dato:** 4. december 2025
- **Tid:** 23:59 (Copenhagen time)
- **Platform:** DigitalExam

### Krav for Godkendelse:
- ✅ **Tidsmæssig indlevering** - Forudsætning for at deltage i eksamen
- ✅ **Alle påkrævede filer** - Rapport PDF + kildekode
- ✅ **Containerization** - Dockerfile der virker
- ✅ **Forskellige host environments** - Server (EC2) + Klient (lokal PC)

### Hvad Sker hvis vi Mangler Noget:
- ❌ **Ingen rapport PDF** → Kan ikke deltage i eksamen
- ❌ **Mangler Dockerfile** → Opfylder ikke containerization krav
- ❌ **Mangler main.py** → Kan ikke bygge API server
- ❌ **Mangler client.py** → Kan ikke demonstrere funktionalitet

---

## 📝 Hurtig Kommando til Pakning

```bash
# Navigér til projekt root
cd ~/path/to/Miniprojekt-AISI

# Opret submission mappe
mkdir -p submission

# Kopier påkrævede filer
cp rapport.pdf submission/              # HUSK: Lav rapport.pdf først!
cp main.py submission/
cp client.py submission/
cp Dockerfile submission/
cp requirements.txt submission/
cp .dockerignore submission/            # optional
cp README.md submission/                # optional

# Pak filer
zip -r miniprojekt_submission.zip submission/

# Verificer indhold
unzip -l miniprojekt_submission.zip

# Upload til DigitalExam
echo "✅ Ready for upload to DigitalExam!"
```

---

## ✅ Færdig Checklist

**Peter + Jonas skal:**
1. [ ] Skriv Results sektion i rapport (sammen)
2. [ ] Skriv Conclusion sektion i rapport (sammen)
3. [ ] Kombinér alle rapport sektioner til én fil
4. [ ] Konvertér rapport til PDF format
5. [ ] Pak alle filer i .zip eller .tar.gz
6. [ ] Upload til DigitalExam før deadline

**Estimeret tid tilbage:** 2-3 timer (rapport + pakning)

---

**Sidst opdateret:** 3. december 2025 kl. 17:35
