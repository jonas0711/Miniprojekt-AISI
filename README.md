# Mini Project - AI Systems & Infrastructure

**Projekt:** AI API Server med Containerization og Cloud Deployment  
**Kursus:** AI Systems & Infrastructure  
**Deadline:** 4. december 2025 kl. 23:59

---

## 📁 Projektstruktur

```
miniproject-aisa/
├── main.py                 # FastAPI server (kode)
├── client.py               # Klientprogram (kode)
├── requirements.txt        # Python dependencies (kode)
├── Dockerfile              # Docker containerization (kode)
├── README.md               # Denne fil
├── docs/                   # Dokumentation
│   ├── modules/            # Modul opsummeringer
│   │   ├── MODUL1_INTERACT_WITH_AI_SYSTEMS.md
│   │   ├── MODUL2_ADVANCED_APIS.md
│   │   ├── MODUL3_WRAP_AI_MODELS_WITH_APIS.md
│   │   ├── MODUL4_AI_COMPUTE_HARDWARE.md
│   │   ├── MODUL5_PACKAGING_CONTAINERIZATION.md
│   │   └── MODUL6_CLOUD_DEPLOYMENT.md
│   ├── guides/             # Guides og tutorials
│   │   ├── EC2_LOGIN_GUIDE.md
│   │   ├── EC2_FILOVERSIGT.md
│   │   ├── SSHFS_GUIDE.md
│   │   └── DEPLOYMENT_GUIDE.md
│   ├── project/            # Projekt specifik dokumentation
│   │   ├── MINIPROJEKT_KRAV.md
│   │   ├── PROJEKT_STATUS.md
│   │   ├── PROJEKT_OVERBLIK.md
│   │   └── TODO.md
│   ├── deployment/         # Deployment logs
│   │   ├── peter_deploy.md
│   │   └── JONAS_DEPLOYMENT.md
│   ├── report/            # Rapport sektioner
│   │   ├── RAPPORT_INTRODUCTION.md
│   │   └── RAPPORT_IMPLEMENTATION.md
│   ├── README_API.md      # API dokumentation
│   └── VERIFIKATION.md    # Verifikation dokumentation
└── scripts/                # Utility scripts
    ├── mount_ec2.sh       # Mount EC2 serveren lokalt
    └── unmount_ec2.sh     # Unmount EC2 serveren
```

---

## 📚 Dokumentation

### Modul Opsummeringer (`docs/modules/`)

Opsummeringer af alle moduler fra kurset:

- **MODUL1:** Interact with AI Systems - API fundamentals, versioning, rate limiting
- **MODUL2:** Advanced APIs - Streaming, WebSocket, MQTT, Kafka, MCP
- **MODUL3:** Wrap AI Models with APIs - FastAPI, AI model integration, authentication, database
- **MODUL4:** AI Compute Hardware - Von Neumann architecture, CPU/GPU/TPU/NPU
- **MODUL5:** Packaging & Containerization - Docker, Dockerfile, container deployment
- **MODUL6:** Cloud Deployment - Cloud infrastructure, VM setup, HTTPS, production

### Guides (`docs/guides/`)

Praktiske guides til at arbejde med EC2 serveren:

- **EC2_LOGIN_GUIDE.md:** Hvordan man logger ind på EC2 serveren
- **EC2_FILOVERSIGT.md:** Oversigt over filer på EC2 serveren
- **SSHFS_GUIDE.md:** Guide til at mounte EC2 serveren lokalt

### Projekt Dokumentation (`docs/project/`)

Projekt specifik information:

- **MINIPROJEKT_KRAV.md:** Komplet kravspecifikation for mini projektet
- **PROJEKT_STATUS.md:** Status over hvad vi har lavet og næste skridt
- **PROJEKT_OVERBLIK.md:** Overblik over projektet
- **TODO.md:** Opgaveliste og status

### Deployment Logs (`docs/deployment/`)

Deployment dokumentation:

- **peter_deploy.md:** Peter's deployment log
- **JONAS_DEPLOYMENT.md:** Jonas' deployment log

### Rapport (`docs/report/`)

Rapport sektioner:

- **RAPPORT_INTRODUCTION.md:** Introduction sektion
- **RAPPORT_IMPLEMENTATION.md:** Implementation sektion

---

## 🛠️ Scripts

### Mount EC2 Serveren

```bash
./scripts/mount_ec2.sh
```

Monterer EC2 serverens `/home/ubuntu` mappe til `~/ec2_mount` lokalt.

### Unmount EC2 Serveren

```bash
./scripts/unmount_ec2.sh
```

Unmonterer EC2 serveren.

---

## 🚀 Hurtig Start

### 1. Mount EC2 Serveren

```bash
cd ~/miniproject-aisa
./scripts/mount_ec2.sh
```

### 2. Læs Projekt Krav

```bash
cat docs/project/MINIPROJEKT_KRAV.md
```

### 3. Se Projekt Status

```bash
cat docs/project/PROJEKT_STATUS.md
```

---

## 📋 Projekt Krav (Opsummering)

### Påkrævet:
- ✅ API Server med flere routes (mindst én med AI funktionalitet)
- ✅ Containerization (Docker)
- ✅ Deployment på anden maskine end klienten (EC2 server)
- ✅ Klientprogram der kan interagere med serveren

### Anbefalet:
- ⭐ API versioning (`/v1/`, `/v2/`)
- ⭐ Rate limiting
- ⭐ Database integration (API key management)
- ⭐ REST principper
- ⭐ HTTPS setup

### Deadline:
- **4. december 2025 kl. 23:59** (Copenhagen time)

---

## 🔗 Vigtige Links

- **EC2 Server:** `51.21.200.191` (ssh ec2)
- **Mount Point:** `~/ec2_mount` (når mountet)
- **SSH Config:** `~/.ssh/config` (alias: `ec2`)

---

## 📝 Noter

- Alle modul opsummeringer er baseret på kursus materiale
- Scripts er testet og fungerer
- EC2 serveren er klar til deployment
- Docker er installeret på EC2 serveren

---

## 🎯 Næste Skridt

1. Planlæg API serverens struktur
2. Implementer API serveren
3. Opret Dockerfile
4. Deploy på EC2 serveren
5. Test funktionalitet
6. Skriv rapport

