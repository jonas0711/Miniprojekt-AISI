# Deployment Guide - EC2 Server

## 📋 Forberedelse

### Filer der skal deployes:
- `main.py` - FastAPI server
- `requirements.txt` - Dependencies
- `Dockerfile` - Container definition
- `.dockerignore` - Ignore filer

---

## 🚀 Deployment Steps

### 1. Upload filer til EC2

**Option A: SCP (Simple Copy)**
```bash
# Opret mappe på serveren
ssh ec2 "mkdir -p ~/cifar10-api"

# Kopier filer
scp main.py requirements.txt Dockerfile .dockerignore ubuntu@51.21.200.191:~/cifar10-api/
```

**Option B: SSHFS Mount**
```bash
# Mount serveren lokalt
./scripts/mount_ec2.sh

# Kopier filer til mount point
cp main.py requirements.txt Dockerfile .dockerignore ~/ec2_mount/cifar10-api/

# Unmount
fusermount -u ~/ec2_mount
```

### 2. SSH ind på EC2 serveren

```bash
ssh ec2
```

### 3. Naviger til projekt mappen

```bash
cd ~/cifar10-api
```

### 4. Build Docker container

```bash
docker build -t cifar10-api:v1.0 .
```

**Forklaring:**
- `-t cifar10-api:v1.0` - Tag image med navn og version
- `.` - Build context (nuværende mappe)

### 5. Kør container

```bash
docker run -d -p 8000:8000 --restart unless-stopped --name cifar10-api cifar10-api:v1.0
```

**Forklaring:**
- `-d` - Kør i baggrunden (detached mode)
- `-p 8000:8000` - Map port 8000 på host til port 8000 i container
- `--restart unless-stopped` - Genstart automatisk ved reboot
- `--name cifar10-api` - Giv containeren et navn
- `cifar10-api:v1.0` - Image navn og tag

### 6. Test API lokalt på serveren

```bash
# Test health endpoint
curl http://localhost:8000/health

# Test model info
curl http://localhost:8000/model/info

# Test root endpoint
curl http://localhost:8000/
```

### 7. Verificer container kører

```bash
# Se kørende containere
docker ps

# Se container logs
docker logs cifar10-api

# Følg logs i real-time
docker logs -f cifar10-api
```

---

## 🧪 Test fra lokal maskine

### Test med klientprogram

```bash
# Test health
python client.py

# Test med billede
python client.py test_image.jpg
```

**API URL:** `http://51.21.200.191:8000`

---

## 🔧 Troubleshooting

### Container starter ikke

```bash
# Se logs
docker logs cifar10-api

# Tjek om port er i brug
sudo netstat -tulpn | grep 8000
```

### Port ikke tilgængelig

```bash
# Tjek firewall
sudo ufw status

# Tillad port 8000 (hvis nødvendigt)
sudo ufw allow 8000/tcp
```

### Container crasher

```bash
# Se container status
docker ps -a

# Se logs
docker logs cifar10-api

# Genstart container
docker restart cifar10-api
```

---

## 📝 Noter

- **Server IP:** 51.21.200.191
- **Port:** 8000
- **Container navn:** cifar10-api
- **Image tag:** cifar10-api:v1.0

---

## ✅ Verificering

Efter deployment skal følgende virke:

1. ✅ Container kører (`docker ps`)
2. ✅ Health endpoint svarer (`curl http://localhost:8000/health`)
3. ✅ Model info endpoint svarer (`curl http://localhost:8000/model/info`)
4. ✅ Klient kan connecte fra lokal PC (`python client.py`)

---

**Sidst opdateret:** 3. december 2025

