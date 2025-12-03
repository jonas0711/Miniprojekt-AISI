# Komplet filoversigt for EC2-serveren

**Dato:** 2. december 2025  
**Server:** ec2-51-21-200-191.eu-north-1.compute.amazonaws.com  
**Mount point:** `~/ec2_mount`

---

## 📊 Oversigt

- **Total antal filer:** 2016 filer
- **Diskforbrug:** 3.2 GB brugt af 19 GB (18%)
- **Hovedmappe:** `/home/ubuntu`

---

## 📁 Mapper og indhold

### 1. **P/** (4 KB)
- Tom mappe
- Oprettet: 29. november 2025
- Ingen filer

### 2. **.vscode-server/** (414 MB)
- VS Code Remote Server installation
- Indeholder:
  - VS Code server binary (24 MB)
  - Extensions (GitHub Copilot, Pull Requests, etc.)
  - Logs fra VS Code sessions
  - Data og cache filer
- Største filer:
  - `code-bf9252a2fb45be6893dd8870c0bf37e2e1766d61` (24 MB)
  - Extension VSIXs (GitHub Copilot, Pull Requests)

### 3. **.dotnet/** (232 KB)
- .NET CoreFX installation
- Indeholder corefx biblioteker

### 4. **.local/** (12 KB)
- Lokale brugerdata
- Minimalt indhold

### 5. **.cache/** (16 KB)
- Microsoft cache filer
- Minimalt indhold

### 6. **.ssh/** (1.9 KB)
- SSH autoriserede nøgler
- **authorized_keys** indeholder 3 SSH-nøgler:
  1. Jonas' nøgle (den du lige sendte)
  2. En anden Jonas nøgle
  3. En "login" nøgle

### 7. **Konfigurationsfiler**
- `.bashrc` (3.7 KB) - Bash konfiguration
- `.bash_history` (1.1 KB) - Kommando historik
- `.profile` (807 bytes) - Profil konfiguration
- `.bash_logout` (220 bytes) - Logout script

---

## 🔍 Vigtige oplysninger

### SSH Nøgler
Serveren har 3 autoriserede SSH-nøgler i `authorized_keys`:
- 2 nøgler fra "jonas"
- 1 nøgle fra "login"

### Docker
- Docker er installeret (version 29.1.1)
- Ingen containere kører
- Ingen images installeret

### Software installeret
- ✅ Docker 29.1.1
- ✅ Python 3.12.3
- ✅ Git
- ✅ .NET CoreFX
- ✅ VS Code Remote Server
- ❌ Node.js (ikke installeret)
- ❌ Nginx/Apache (ikke installeret)

### Bash historik
Sidste kommandoer inkluderer:
- Docker installation
- SSH nøgle opsætning
- System reboot

---

## 📂 Filtyper fundet

- **VS Code logs:** Flere log filer fra VS Code sessions
- **Extension filer:** VSIX packages for VS Code extensions
- **Konfigurationsfiler:** Bash, SSH, system configs
- **Cache filer:** Microsoft og VS Code cache

---

## 🎯 Konklusion

Serveren er en **frisk EC2-instans** med:
- Basis software installeret (Docker, Python, Git)
- VS Code Remote Server sat op
- SSH adgang konfigureret
- **Ingen projekter eller applikationer** kører endnu
- Tom P/ mappe klar til projekter

**Status:** Serveren er klar til at deploye projekter og applikationer.

