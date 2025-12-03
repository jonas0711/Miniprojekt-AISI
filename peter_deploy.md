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

---

## 🚀 EC2 Deployment (I Gang)

###  Problem: SSH Connection Timeout (LØST)

**Fejl:** `Connection timed out during banner exchange`
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

## Næste Skridt

Peter skal:
1. ✅ Løs SSH connection problem (AWS Security Group)
2. ⏳ Kør deployment commands ovenfor
3. ⏳ Test API virker på EC2
4. ⏳ Åbn port 8000 i Security Group
5. ⏳ Test API fra lokal PC (forskellige host environments)

