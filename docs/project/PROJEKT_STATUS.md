# Projekt Status - Hvad har vi lavet?

**Dato:** 3. december 2025  
**Projekt:** AI Systems & Infrastructure - Mini Project

---

## ✅ Hvad vi har lavet indtil videre

### 1. **EC2 Server Opsætning**
- ✅ SSH nøgler oprettet og konfigureret
- ✅ SSH config sat op med alias `ec2` for nem adgang
- ✅ SSHFS installeret og konfigureret til at mounte serveren lokalt
- ✅ Scripts til mounting/unmounting oprettet (`mount_ec2.sh`, `unmount_ec2.sh`)

### 2. **Server Undersøgelse**
- ✅ Komplet filoversigt over EC2-serveren (`EC2_FILOVERSIGT.md`)
- ✅ Verificeret at Docker, Python, Git er installeret
- ✅ Tjekket at serveren er klar til deployment

### 3. **Dokumentation**
- ✅ Login guide til EC2-serveren (`EC2_LOGIN_GUIDE.md`)
- ✅ SSHFS guide (`SSHFS_GUIDE.md`)
- ✅ Komplet kravspecifikation (`MINIPROJEKT_KRAV.md`)

### 4. **Filer i Projektet**
```
miniproject-aisa/
├── EC2_LOGIN_GUIDE.md          # Guide til at logge ind på serveren
├── EC2_FILOVERSIGT.md           # Oversigt over filer på serveren
├── MINIPROJEKT_KRAV.md          # Komplet kravspecifikation
├── SSHFS_GUIDE.md               # Guide til SSHFS mounting
├── mount_ec2.sh                 # Script til at mounte serveren
└── unmount_ec2.sh               # Script til at unmounte serveren
```

---

## 🖥️ AWS EC2 Server Status

### Server Information
- **IP:** 51.21.200.191
- **Hostname:** ip-172-31-37-19
- **OS:** Ubuntu 24.04.3 LTS
- **Status:** ✅ TILGÆNGELIG OG FUNKTIONEL

### Installeret Software
- ✅ **Docker** 29.1.1 - Klar til containerization
- ✅ **Python** 3.12.3 - Klar til API server
- ✅ **Git** - Klar til version control
- ✅ **.NET CoreFX** - Installeret
- ✅ **VS Code Remote Server** - Sat op

### Forbindelse
- ✅ SSH forbindelse virker perfekt (testet 3. dec 2025)
- ✅ Kan logge ind med: `ssh ec2`
- ✅ SSHFS kan mounte serveren lokalt
- ✅ Docker service kører og er aktiv
- ✅ Python 3.12.3 fungerer korrekt
- ✅ Ingen porte er åbne endnu (klar til at eksponere API)

### Disk og Ressourcer
- **Disk:** 3.2 GB brugt af 19 GB (18% - masser af plads)
- **Hukommelse:** 393 MB brugt af 914 MB
- **Status:** Klar til deployment

---

## 🎯 Kan AWS Serveren være en del af projektet?

### ✅ JA - Serveren er PERFEKT til projektet!

**Hvorfor:**
1. **Forskellige Host Environments** ✅
   - Serveren kører på AWS EC2 (cloud)
   - Klienten kan køre på din lokale PC (WSL)
   - Dette opfylder kravet om forskellige host environments

2. **Containerization** ✅
   - Docker er installeret og klar
   - Vi kan deploye API serveren i en Docker container
   - Dette opfylder containerization kravet

3. **Netværksadgang** ✅
   - Serveren har offentlig IP (51.21.200.191)
   - Kan tilgås via SSH
   - Kan konfigureres til at eksponere API endpoints

4. **Ressourcer** ✅
   - Nok diskplads (16 GB ledig)
   - Nok hukommelse
   - Python og Docker klar til brug

---

## 📋 Næste Skridt

### 1. **Planlæg API Server**
- [ ] Vælg routes/endpoints
- [ ] Vælg AI model(ler)
- [ ] Design API struktur

### 2. **Implementer API Server**
- [ ] Opret FastAPI projekt
- [ ] Implementer routes
- [ ] Integrer AI model(ler)
- [ ] Tilføj error handling

### 3. **Docker Setup**
- [ ] Opret Dockerfile
- [ ] Opret requirements.txt
- [ ] Test lokalt med Docker
- [ ] Build container image

### 4. **Deploy på EC2**
- [ ] Upload kode til serveren
- [ ] Build container på serveren
- [ ] Kør container med port mapping
- [ ] Test API endpoints

### 5. **Klient Program**
- [ ] Opret klient der kan kalde API
- [ ] Test alle endpoints
- [ ] Dokumenter funktionalitet

### 6. **Rapport**
- [ ] Skriv rapport (3-4 sider)
- [ ] Dokumenter implementation
- [ ] Dokumenter deployment
- [ ] Evaluer resultater

---

## 🔧 Tekniske Detaljer

### SSH Config
```bash
Host ec2
    HostName 51.21.200.191
    User ubuntu
    IdentityFile ~/.ssh/id_rsa
    ServerAliveInterval 30
    ServerAliveCountMax 4
```

### Mount Serveren
```bash
./mount_ec2.sh        # Mount serveren
./unmount_ec2.sh      # Unmount serveren
```

### Test Forbindelse
```bash
ssh ec2 "docker --version"  # Test Docker
ssh ec2 "python3 --version" # Test Python
```

---

## ✅ Konklusion

**AWS EC2 serveren er PERFEKT til projektet!**

- ✅ Opfylder alle krav (forskellige host environments, containerization)
- ✅ Er klar til deployment (Docker, Python installeret)
- ✅ Har nok ressourcer
- ✅ Forbindelse virker perfekt
- ✅ Vi har allerede sat alt op til at arbejde med serveren

**Vi er klar til at begynde implementation!**

