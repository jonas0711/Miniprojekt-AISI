# Deployment

Denne sektion beskriver deployment-processen af vores CIFAR-10 API server, fra containerization med Docker til hosting på AWS EC2.

## Docker Containerization

Vi har valgt at containerisere vores applikation ved hjælp af Docker for at sikre konsistens på tværs af udviklings- og produktionsmiljøer. Dette opfylder projektets krav om containerization (Modul 5).

### Dockerfile Design
Vores `Dockerfile` er bygget med fokus på effektivitet og "best practices" for layering:

1.  **Base Image:** Vi benytter `python:3.11-slim` for at holde image-størrelsen nede (~300MB) samtidig med at vi har en stabil Python version.
2.  **Layer Caching:** Vi kopierer `requirements.txt` og installerer dependencies *før* vi kopierer selve kildekoden. Dette udnytter Dockers cache-mekanisme, så vi undgår at geninstallere tunge biblioteker som PyTorch ved hver eneste kodeændring.
3.  **Security:** Vi kører applikationen som standard bruger (root i containeren), men eksponerer kun den nødvendige port (8000).

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Cloud Deployment på AWS EC2

Vi har deployet løsningen på en AWS EC2 instans i regionen `eu-north-1` (Stockholm).

**Server Specifikationer:**
- **Instance Type:** t3.micro (Free Tier eligible)
- **OS:** Ubuntu 24.04 LTS
- **IP:** 51.21.200.191

### Deployment Process
Deployment-processen fulgte disse trin:

1.  **Kode Overførsel:** Koden blev uploadet til serveren via SSH/SCP.
2.  **Build:** Docker imaget blev bygget direkte på serveren.
3.  **Execution:** Containeren køres i "detached mode" med restart policy for at sikre oppetid:
    ```bash
    docker run -d -p 8000:8000 --restart unless-stopped --name cifar10-api cifar10-api:v1.1
    ```

### Udfordringer og Løsninger

Under deployment stødte vi på to væsentlige udfordringer:

1.  **Out of Memory (OOM) under Build:**
    *   **Problem:** EC2 instansen (t3.micro) har kun 1GB RAM. Under installationen af tunge dependencies (PyTorch) løb serveren tør for hukommelse, og processen blev dræbt af Linux OOM-killer.
    *   **Løsning:** Vi oprettede en 2GB swap-fil på serveren, hvilket gav systemet virtuel hukommelse nok til at færdiggøre byggeprocessen.

2.  **NumPy/PyTorch Inkompatibilitet:**
    *   **Problem:** Efter deployment fejlede `/image_classify` endpointet med en "Internal Server Error". Logs viste en konflikt mellem PyTorch og den nyeste NumPy version (2.0+).
    *   **Løsning:** Vi opdaterede `requirements.txt` til eksplicit at kræve `numpy<2`, genopbyggede imaget (v1.1), og deployede igen.

## Verifikation

Deployment er verificeret ved at teste API'en fra forskellige miljøer ("host environments"), som krævet i opgavebeskrivelsen:

1.  **Lokal Test (Server):** Verificeret via `curl http://localhost:8000/health` på selve EC2 instansen.
2.  **Ekstern Test (Klient):** Verificeret fra en lokal laptop via vores Python klient (`client.py`) mod den offentlige IP.

Vi måtte konfigurere AWS Security Groups til at tillade indgående trafik på **port 8000** (Custom TCP) for at muliggøre ekstern adgang.
