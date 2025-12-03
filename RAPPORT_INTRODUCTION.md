# Introduction - Rapport

**Forfattere:** Peter og Jonas  
**Dato:** 3. december 2025

---

## Problem Analyse

### Problemstilling

I moderne AI systemer er der behov for at gøre AI modeller tilgængelige gennem standardiserede API interfaces. Dette gør det muligt for forskellige applikationer at bruge AI funktionalitet uafhængigt af programmeringssprog eller platform.

**Hovedudfordringer:**
1. **Deployment kompleksitet:** At deploye AI modeller på forskellige maskiner kræver konsistent runtime environment
2. **Forskellige host environments:** Server og klient skal kunne køre på forskellige maskiner
3. **Containerization:** Sikrer at applikationen kører konsistent uanset host environment

### Projektets Mål

Dette projekt implementerer en CIFAR-10 image classification API server der:
- Klassificerer billeder i 10 kategorier (airplane, car, bird, cat, deer, dog, frog, horse, ship, truck)
- Kører i en Docker container på AWS EC2 server
- Kan tilgås fra en klient kørende på lokal maskine
- Demonstrerer forskellige host environments (cloud server + lokal PC)

### Projektets Omfang

Projektet dækker:
- **API Server:** FastAPI server med CIFAR-10 image classification
- **Containerization:** Docker container med proper layering
- **Deployment:** Cloud deployment på AWS EC2
- **Klientprogram:** Python klient der kan interagere med serveren
- **Verifikation:** Test af forskellige host environments

### Teknologier

- **FastAPI:** Moderne Python web framework med async support
- **PyTorch/Torchvision:** Deep learning framework til CIFAR-10 model
- **Docker:** Containerization platform
- **AWS EC2:** Cloud virtual machine til deployment
- **Python Requests:** HTTP client library til klientprogram

---

**Note:** Denne sektion skal inkluderes i den endelige rapport (3-4 sider).

