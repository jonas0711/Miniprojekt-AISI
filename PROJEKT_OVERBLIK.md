# Projekt Overblik - CIFAR-10 Image Classification API

**Dato:** 3. december 2025  
**Status:** 11/26 opgaver færdige (42%)  
**Deadline:** 4. december 2025 kl. 23:59

---

## 📊 Status Oversigt

### ✅ Færdige Opgaver (10)

#### API Server Implementation (Jonas)
- ✅ FastAPI projekt struktur (`main.py`)
- ✅ CIFAR-10 image classification endpoint (`POST /image_classify`)
- ✅ Utility routes (`GET /health`, `GET /model/info`)
- ✅ Requirements.txt med dependencies

#### Docker Setup (Peter)
- ✅ Dockerfile (oprettet)


#### Klientprogram (Jonas)
- ✅ Klientprogram (`client.py`) med requests library
- ✅ API kald implementeret (health, model/info, image_classify)

### ⏳ Manglende Opgaver (16)

#### Docker Setup (Peter)
- ⏳ Test Docker build lokalt
- ⏳ Verificer container virker

#### EC2 Deployment (Peter)
- ⏳ Upload kode til EC2
- ⏳ Build container på EC2
- ⏳ Kør container på EC2
- ⏳ Test API fra serveren

#### Klientprogram Test (Jonas)
- ⏳ Test klient fra lokal maskine mod EC2

#### Rapport (Begge)
- ⏳ Introduction
- ⏳ Implementation sektion
- ⏳ Deployment sektion
- ⏳ Results sektion
- ⏳ Conclusion

#### Submission (Begge)
- ⏳ Pak alle filer
- ⏳ Upload til DigitalExam

---

## 📁 Projektstruktur

```
miniproject-aisa/
├── main.py                 # FastAPI server (Jonas)
├── client.py               # Klientprogram (Jonas)
├── requirements.txt        # Dependencies (Jonas)
├── Dockerfile              # Docker setup (Peter)
├── README_API.md          # API dokumentation
├── TODO.md                 # Opgaveliste
├── docs/                   # Dokumentation
│   ├── modules/           # Modul opsummeringer
│   ├── guides/            # EC2 guides
│   └── project/           # Projekt specifikation
└── scripts/               # Utility scripts
    ├── mount_ec2.sh       # Mount EC2 server
    └── unmount_ec2.sh     # Unmount EC2 server
```

---

## 🖥️ Server Information

**EC2 Server:**
- **IP:** 51.21.200.191
- **Hostname:** ec2-51-21-200-191.eu-north-1.compute.amazonaws.com
- **OS:** Ubuntu 24.04.3 LTS
- **Docker:** 29.1.1 (installeret)
- **Python:** 3.12.3 (installeret)
- **Status:** Klar til deployment

**SSH Adgang:**
- Alias: `ssh ec2`
- User: `ubuntu`
- SSH keys: Konfigureret

---

## 🔧 API Endpoints

### 1. GET `/`
Root endpoint - velkomstbesked

### 2. GET `/health`
Health check - tjekker server status

### 3. GET `/model/info`
Model information - returnerer CIFAR-10 model info

### 4. POST `/image_classify`
Image classification - klassificerer billede i 10 kategorier

**Request:**
```json
{
  "image": "base64_encoded_image_string",
  "filename": "optional_filename.jpg"
}
```

**Response:**
```json
{
  "predictions": [
    {"label": "airplane", "confidence": 0.8542},
    ...
  ],
  "model": "ResNet-18 (CIFAR-10)"
}
```

---

## 🚀 Deployment Status

### Lokal Udvikling
- ✅ API server implementeret
- ✅ Klientprogram implementeret
- ✅ Dockerfile (oprettet)

### EC2 Deployment
- ✅ Server klar (Docker, Python installeret)
- ⏳ Kode upload (venter på Dockerfile)
- ⏳ Container build
- ⏳ Container kørsel
- ⏳ API test

---

## 📋 Næste Skridt

### Prioriteret Rækkefølge:

1. **Peter: Docker Setup**
   - Test lokalt
   - Verificer container

2. **Peter: EC2 Deployment**
   - Upload kode til EC2
   - Build container
   - Kør container
   - Test API

3. **Jonas: Klient Test**
   - Test klient mod EC2 server
   - Verificer forskellige host environments

4. **Begge: Rapport**
   - Skriv alle sektioner
   - 3-4 sider (ekskl. referencer)

5. **Begge: Submission**
   - Pak filer
   - Upload til DigitalExam

---

## 🎯 Krav Status

### ✅ Opfyldte Krav
- ✅ Mere end én route (4 endpoints)
- ✅ Mindst én route med AI funktionalitet (`/image_classify`)
- ✅ FastAPI framework
- ✅ AI model (CIFAR-10, ResNet-18)
- ✅ Klientprogram
- ✅ Forskellige host environments (EC2 + lokal PC)

### ⏳ Manglende Krav
- ⏳ Containerization (Dockerfile oprettet, mangler test)
- ⏳ Server deployet på EC2
- ⏳ Rapport (3-4 sider)
- ⏳ Submission

---

## 📝 Noter

- **Model:** CIFAR-10 (10 klasser: airplane, car, bird, cat, deer, dog, frog, horse, ship, truck)
- **Framework:** FastAPI (anbefalet)
- **Containerization:** Docker (påkrævet)
- **Deployment:** EC2 server (51.21.200.191)
- **Klient:** Lokal PC (WSL)

---

**Sidst opdateret:** 3. december 2025

