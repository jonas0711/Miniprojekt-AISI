# Guide: Forbindelse til EC2 Server

Denne guide beskriver hvordan man forbinder til projektets EC2 server, både via SSH for administration og via API'en for klienter.

## 🖥️ Server Information

- **IP Adresse:** `51.21.200.191`
- **DNS:** (Brug IP adressen)
- **Region:** eu-north-1 (Stockholm)
- **OS:** Ubuntu 24.04 LTS
- **Status:** ✅ Online (v1.1)


---

## 🔑 SSH Adgang (Administration)

For at logge ind på serveren og administrere Docker containere eller filer.

### Forudsætninger
- Du skal have SSH nøglen: `login.pem`
- Nøglen skal have korrekte rettigheder (`chmod 400 login.pem`)

### Kommando
```bash
ssh -i ~/Downloads/login.pem ubuntu@51.21.200.191
```
*(Tilpas stien til `login.pem` hvis den ikke ligger i Downloads)*

### Genveje (Alias)
Du kan tilføje dette til din `~/.ssh/config` for nemmere adgang:
```ssh
Host ec2
    HostName 51.21.200.191
    User ubuntu
    IdentityFile ~/Downloads/login.pem
```
Herefter kan du bare skrive: `ssh ec2`

---

## 🌐 API Adgang (Klienter)

API'en kører i en Docker container og er tilgængelig offentligt.

- **Base URL:** `http://51.21.200.191:8000`
- **Dokumentation (Swagger UI):** `http://51.21.200.191:8000/docs`

### Endpoints

| Metode | Endpoint | Beskrivelse |
|--------|----------|-------------|
| `GET` | `/health` | Tjek om serveren kører. Returnerer status. |
| `GET` | `/model/info` | Få information om den loadede AI model. |
| `POST` | `/image_classify` | Send et billede og få en klassificering (CIFAR-10). |

### Test forbindelsen
Du kan teste om API'en er oppe via din browser eller terminal:

```bash
curl http://51.21.200.191:8000/health
```
**Forventet svar:** `{"status":"healthy","model_status":"loaded"}`

---

## 🐍 Brug af Python Klient

Vi har et færdigt klientprogram (`client.py`) der håndterer kommunikationen.

### Installation af dependencies
```bash
pip install requests
```

### Kør klienten
```bash
# Tjek status og model info
python client.py

# Klassificer et billede
python client.py sti/til/billede.jpg
```

---

## 🛠️ Fejlfinding

### "Connection timed out" (SSH)
- Tjek at du bruger den rigtige IP.
- Tjek at din IP er tilladt i AWS Security Group (Port 22).
- Tjek at serveren kører i AWS Console.

### "Connection timed out" (API)
- Tjek at Docker containeren kører på serveren (`docker ps`).
- Tjek at **Port 8000** er åben i AWS Security Group (Inbound Rules).

### "Permission denied (publickey)"
- Tjek at du bruger den rigtige `.pem` fil.
- Tjek filrettigheder: `chmod 400 login.pem`.
