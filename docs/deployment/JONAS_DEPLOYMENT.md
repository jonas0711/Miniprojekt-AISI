# Jonas' Filer til AWS Deployment

## 📋 Jonas' Filer der SKAL på AWS

Kun disse filer skal uploades til EC2 serveren:

1. **`main.py`** - FastAPI server (Jonas' kode)
2. **`requirements.txt`** - Dependencies (Jonas' kode)

## ❌ Filer der IKKE skal på AWS

- `client.py` - Kører lokalt på din PC (ikke på serveren)
- `Dockerfile` - Peters opgave (han deployer)
- `.dockerignore` - Peters opgave
- `README_API.md` - Dokumentation (ikke nødvendig på serveren)
- `TODO.md` - Projekt management (ikke nødvendig på serveren)
- Alle andre filer

---

## 🚀 Deployment (Kun Jonas' Filer)

### Metode 1: SCP (Simple Copy)

```bash
# Opret mappe på serveren
ssh ec2 "mkdir -p ~/cifar10-api"

# Kopier KUN Jonas' filer
scp main.py requirements.txt ubuntu@51.21.200.191:~/cifar10-api/
```

### Metode 2: SSHFS Mount

```bash
# Mount serveren
./scripts/mount_ec2.sh

# Kopier KUN Jonas' filer
mkdir -p ~/ec2_mount/cifar10-api
cp main.py requirements.txt ~/ec2_mount/cifar10-api/

# Unmount
fusermount -u ~/ec2_mount
```

---

## ⚠️ Vigtigt

- **Kun upload Jonas' filer** (`main.py` og `requirements.txt`)
- **Lad Peter håndtere Dockerfile og deployment**
- **client.py skal IKKE på serveren** (kører lokalt)

---

**Note:** Efter upload skal Peter bygge Docker container og køre den.

