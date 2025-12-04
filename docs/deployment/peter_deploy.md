# Peter's Deployment Log - EC2 Docker Deployment

**Dato:** 3. december 2025
**Server:** EC2 (51.21.200.191)
**Opgave:** Deploy CIFAR-10 API til EC2 med Docker

---

## ✅ Færdige Opgaver

### 1. Docker Setup (Lokal)
- ✅ `.dockerignore` oprettet (combined med Jonas' version)
- ✅ `Dockerfile` oprettet med proper layering (Modul 5)
- ✅ Pushed til GitHub
- ✅ Testet Docker build lokalt (v1.0)
- ✅ Verificeret container virker lokalt (health check OK)

**Dockerfile struktur:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Test Resultater (Lokal):**
- Build tid: ~45 sekunder
- Image size: ~300MB (python:3.11-slim base)
- Health check: `{"status":"healthy","model_status":"loaded"}`
- Model info: `{"name":"ResNet-18 (CIFAR-10)","status":"loaded","num_labels":10}`

---

## 🚀 EC2 Deployment (I Gang)

### ✅ Step 1: Upload kode til EC2
- Uploadet `main.py` og `requirements.txt` til `/home/ubuntu/Miniprojekt-AISI`
- Brugte SSHFS/SCP

### ❌ Step 2: Build & Run (Fejlet)
- **Fejl:** Server crashede under `docker build` (sandsynligvis OOM - Out Of Memory)
- **Status:** Server svarer ikke (Connection timed out)
- **Løsning:** Skal genstartes via AWS Console
- **Forebyggelse:** Vi skal oprette en swap file før næste forsøg
- ✅ **Løst:** Oprettet 2GB swap file (se nedenfor)

### ✅ Step 3: Recovery & Build (I Gang)
1. ✅ Oprettet 2GB swap file
2. ✅ Clonet repo på ny
3. ✅ Docker build færdig (Success!)

**Swap file oprettelse:**
```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```
Resultat: `Swap: 2.0Gi` tilgængelig.

**Build Resultat:**
- Image: `cifar10-api:v1.0`
- Status: Success

### ⏳ Step 4: Run Container (Næste)
- Kør container med restart policy
- Verificer health check

**Kommando:**
```bash
docker run -d -p 8000:8000 --restart unless-stopped --name cifar10-api cifar10-api:v1.0
```
Resultat: Container ID `0aa8fad...`

### ✅ Step 5: Verify on Server (Success)
- `curl http://localhost:8000/health`
- Resultat: `{"status":"healthy","model_status":"loaded"}`

### ✅ Step 6: Verify External Access (Success)
- Test: `curl http://51.21.200.191:8000/health`
- Resultat: `{"status":"healthy","model_status":"loaded"}`
- **Status:** Deployment Fuldført! 🚀

### 🏁 Konklusion
Serveren kører nu korrekt på EC2 og kan tilgås udefra.
- **IP:** 51.21.200.191
- **Port:** 8000
- **API:** http://51.21.200.191:8000

**Server:** 51.21.200.191:22
**SSH Key:** `~/Downloads/login.pem`

**Løsning:** EC2 instance genstartet i AWS Console

**Mulige årsager var:**
1. AWS Security Group blokerer port 22 fra din IP
2. EC2 instance var stoppet/termineret ✅ (dette var problemet)
3. Firewall (UFW) på serveren blokerer SSH

**Løsninger (gennemført):**

#### 1. Tjek EC2 Instance Status i AWS Console:
- Log ind på AWS Console
- Gå til EC2 Dashboard
- Tjek om instancen kører (Instance State: `running`)
- Tjek Public IPv4 address matcher: 51.21.200.191

#### 2. Tjek AWS Security Group:
- I EC2 Console, select instance
- Gå til "Security" tab
- Tjek Security Group rules
- **Skal have:** Inbound rule for SSH (port 22) fra din IP eller 0.0.0.0/0

#### 3. Alternativ: Brug AWS Session Manager/Console
Hvis SSH ikke virker, kan du bruge AWS Console til at connecte direkte

###  Kommandoer til EC2 Deployment (når SSH virker):

#### Step 1: Clone repo på EC2
```bash
ssh -i ~/Downloads/login.pem ubuntu@51.21.200.191 "cd /home/ubuntu && rm -rf Miniprojekt-AISI && git clone https://github.com/jonas0711/Miniprojekt-AISI.git"
```

#### Step 2: Build Docker image på EC2
```bash
ssh -i ~/Downloads/login.pem ubuntu@51.21.200.191 "cd /home/ubuntu/Miniprojekt-AISI && docker build -t cifar10-api:v1.0 ."
```

#### Step 3: Stop og fjern gammel container (hvis den findes)
```bash
ssh -i ~/Downloads/login.pem ubuntu@51.21.200.191 "docker stop cifar10-api 2>/dev/null || true && docker rm cifar10-api 2>/dev/null || true"
```

#### Step 4: Kør ny container
```bash
ssh -i ~/Downloads/login.pem ubuntu@51.21.200.191 "docker run -d -p 8000:8000 --restart unless-stopped --name cifar10-api cifar10-api:v1.0"
```

#### Step 5: Verificer container kører
```bash
ssh -i ~/Downloads/login.pem ubuntu@51.21.200.191 "docker ps"
```

#### Step 6: Test API endpoint
```bash
ssh -i ~/Downloads/login.pem ubuntu@51.21.200.191 "curl http://localhost:8000/health"
```

#### Step 7: Test fra lokal maskine (hvis port 8000 er åben)
```bash
curl http://51.21.200.191:8000/health
```

---

## 🎉 DEPLOYMENT FÆRDIG!

**Dato:** 3. december 2025 kl. 17:30

### ✅ Alle Opgaver Gennemført:

1. ✅ SSH connection til EC2 genoprettet (instance restarted)
2. ✅ Docker image bygget på EC2: `cifar10-api:v1.1` (5.16GB)
3. ✅ Container kører på EC2: Container ID `2a997915acb6`
4. ✅ API svarer på EC2:
   - `/health` → `{"status":"healthy","model_status":"loaded"}` ✅
   - `/model/info` → `{"name":"ResNet-18 (CIFAR-10)","status":"loaded","num_labels":10}` ✅
5. ✅ Port 8000 åben i AWS Security Group
6. ✅ API tilgængelig fra lokal PC: `http://51.21.200.191:8000` ✅

### Container Status:
```bash
Container ID: 2a997915acb6
Image: cifar10-api:v1.1
Status: Up 3 hours
Ports: 0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp
```

### Test Resultater:

**Fra EC2 (localhost):**
```bash
curl http://localhost:8000/health
# → {"status":"healthy","model_status":"loaded"}

curl http://localhost:8000/model/info
# → {"name":"ResNet-18 (CIFAR-10)","status":"loaded","num_labels":10}
```

**Fra lokal PC (ekstern adgang):**
```bash
curl http://51.21.200.191:8000/health
# → {"status":"healthy","model_status":"loaded"} ✅
```

### ✅ Krav Verificeret:

- ✅ **Containerization:** Docker container kører på EC2 (PÅKRÆVET)
- ✅ **Forskellige host environments:** Server (EC2 51.21.200.191) + Klient (lokal PC) (PÅKRÆVET)
- ✅ **API med AI funktionalitet:** CIFAR-10 image classification (PÅKRÆVET)
- ✅ **Mindst 2 routes:** `/health`, `/model/info`, `/image_classify` (PÅKRÆVET)
- ✅ **Proper Dockerfile layering:** requirements.txt kopieret først (TIP)

### Peter's Opgaver - ALLE FÆRDIGE! 🎉

**Docker Setup:**
- ✅ `.dockerignore` oprettet
- ✅ `Dockerfile` med proper layering
- ✅ Docker build og test lokalt

**EC2 Deployment:**
- ✅ Upload kode til EC2
- ✅ Build container på EC2
- ✅ Kør container med port mapping
- ✅ Test API fra serveren
- ✅ Port 8000 åben eksternt
- ✅ Test fra lokal PC

**Status:** Peter's deployment er 100% færdig! ✅

