# Modul 5: Packaging & Containerization - Opsummering

**Kursus:** AI Systems & Infrastructure  
**Formål:** Lær hvordan containers løser deployment problemer ved at pakke applikationer med alt de har brug for til at køre konsistent overalt. Udforsk Docker fundamentals og byg en containerized AI API server.

---

## 📚 TL;DR

Har du nogensinde kæmpet med "it works on my machine" syndrom? Lær hvordan containers løser deployment headaches ved at pakke dine applikationer med alt de har brug for til at køre konsistent overalt. Vi udforsker Docker fundamentals og bygger en containerized AI API server.

---

## 🎯 Hovedbegreber

### Problem med Traditional Deployment

**Udfordringer:**
- Hvad sker der når du opdaterer din maskines operating system?
- Hvad hvis du vil deploye på en anden maskine med et andet operating system?
- Hvad når gruppemedlemmer prøver at køre det men har konflikterende Python versioner?
- "It works on my machine" hjælper ikke

**Løsning: Packaging og Containerization**
- I stedet for at replicere runtime hver gang vi deployer på en ny maskine
- Pak software sammen med runtime i en portable container
- Kør altid med et enkelt kommando uanset hvilken maskine det kører på
- Tager ekstra effort først, men sparer mange headaches senere for large-scale deployment

---

## 📦 Basics of Containers

### Hvad er Containers?

**Definition:**
- En lightweight package der inkluderer alt nødvendigt til at køre et stykke software
- Koden, runtime environment, libraries, og configurations
- Self-contained units der kan køre konsistent overalt

**Problem med Traditional Deployment:**
- Installere software og alle dependencies direkte på maskinen
- Kan være kedeligt hvis du deployer kompleks software i large-scale
- Kan lede til mange problemer:
  - To stykker software på samme maskine kræver forskellige versioner af samme library
  - Opdatering til operating system kan ødelægge nøje konfigurerede environment

**Hvordan Containers Løser Det:**
- Opretter isolerede environments der pakker din applikation med alt den har brug for
- Hver container fungerer som en sealed box med eget filesystem, libraries, og configurations
- Komplet separat fra andre containers og native environment af maskinen
- Utroligt effektive: starter på sekunder og bruger minimale ressourcer

**Analog: Kinesisk Middag vs Western-Style Plated Meal**
- **Traditionel:** Alle deler retter fra midten af bordet
- **Problem:** En person har brug for gluten-free soy sauce, en anden har brug for regular
- **Problem:** Nogen tilføjer ved et uheld peanuts til en delt ret når en anden gæst har allergier
- **Containers:** Giver hver person deres egen Western-style plated meal med præcis de seasonings og portions de har brug for
- **Fordele:** Ingen sharing conflicts, ingen kontamination mellem retter, alle får præcist hvad der virker for dem, mens de stadig sidder ved samme bord

**Industriens Standard:**
- Containerization er blevet industry standard for large-scale software deployment
- Meget høj chance for at en af applikationerne du bruger hver dag kører i containers
- Rapporteret at container usage i IT industrien har nået 92% i 2025
- Med containers kan virksomheder:
  - Deploye opdateringer uden downtime
  - Håndtere flere brugere ved at scale automatisk
  - Køre samme software pålideligt på tværs af forskellige hardware infrastrukturer

**Extended Reading:**
- Containers vs Virtual Machines (VMs)
  - **VMs:** Opretter komplet simulerede computere, hver kører sit eget fulde operating system
  - **Analog:** Bygge separate restauranter for hver type køkken, hver med eget køkken, spisestue, lager, og utility systemer
  - **Containers:** Deler host's operating system kernel mens de opretholder isolation
  - **Fordele:** Meget lettere og hurtigere at starte sammenlignet med VMs
  - **VMs:** Giver stærkere isolation for visse security-kritiske applikationer
  - **Analog:** Separate restauranter tilbyder mere komplet separation for health code eller dietary law compliance

### Hvordan Virker Containers?

**Layering System:**
- Secret sauce af containers' efficiency og flexibility er et smart lag-system

**Hamburger Analogi:**
- Start med basic bottom bun
- Tilføj beef patty som næste lag
- For cheeseburger: tilføj cheese lag på toppen
- For deluxe burger: tilføj lettuce, tomato, og special sauce som additional layers
- I stedet for at forberede alt fra scratch hver gang, kan du genbruge samme foundation (bun og patty) og bare tilføje unikke toppings der gør hver burger speciel

**Container Image Layers:**
- Hver container image er et system af layers
- Hvert lag repræsenterer et sæt ændringer fra det forrige
- **Eksempel med 4 layers:**
  1. Add Python runtime
  2. Install libraries
  3. Copy your application code
  4. Configure the startup commands

**Layer Sharing:**
- Containers kørende på én maskine har typisk common layers, især base layers som Python runtime
- Containers deler common layers så kun én kopi af laget eksisterer
- Duplikerede layers behøver ikke at blive lagret, så storage space spares
- Opdatering til hver container involverer ikke rebuilding af hele containeren, bare layers der er blevet modificeret

**Extended Reading:**
- **Writable Layer:** Når en container kører, har den brug for at modificere filer i layers, som at lagre temporary data
- Der er faktisk et temporary writable layer på toppen af read-only layers når en container kører
- Alle ændringer sker i dette writable layer under kørsel af container image, mens underlying layers af image selv er untouched
- **Copy-on-Write:** Når en read-only fil i image layers modificeres, bruger containeren en "copy-on-write" strategi: kopierer filen til writable layer før ændringer
- Dette er muligt med union filesystems (som OverlayFS) der merger multiple directories til et enkelt view

---

## 🐳 Container Frameworks

### Docker

**Hvad er Docker?**
- Docker gjorde containers accessible til de fleste udviklere
- Giver et omfattende toolkit til at arbejde med containers

**Docker Toolkit:**
1. **Docker Engine:**
   - Core runtime der styrer containers kørende på en maskine

2. **Docker CLI:**
   - Giver kommandoer til at styre containers som `docker run`

3. **Dockerfile:**
   - En opskrift til at bygge container images
   - Skrevet i plain text
   - Svarer til det lagrede system af images

4. **Docker Hub:**
   - Cloud registry til at dele container images

**Client-Server Architecture:**
- Docker bruger en client-server arkitektur der separerer hvad du interagerer med fra hvad faktisk gør arbejdet
- **Docker Client:** Program der tager dine kommandoer og sender tilsvarende requests til Docker Daemon
- **Docker Daemon:** Background service der gør det faktiske arbejde med at styre containers, som en server der kører på backend
- Docker Client og Docker Daemon behøver ikke nødvendigvis at køre på samme maskine

**Extended Reading:**
- **Alternative Frameworks:**
  - **Podman:** Kører uden background daemon (bedre security), næsten identiske CLI kommandoer til Docker (drop-in replacement)
  - **containerd:** Hvad Docker faktisk bruger under hood, minimal runtime der er default for Kubernetes
- **Open Container Initiative (OCI):**
  - Oprettede universelle standarder for container image format og runtime behavior
  - Containers bygget med ethvert OCI-compliant tool vil køre på ethvert OCI-compliant runtime
  - Eksempel: Container bygget af Docker kan køre fejlfrit i Podman's runtime, og omvendt

---

## 🚀 Use Containers

### Installation

**Docker Setup:**
- Installer Docker på din maskine
- **Docker Desktop:** Giver både Docker Client og Docker Daemon med user-friendly interface for Windows og macOS
- **Linux:** Installer typisk Docker Engine direkte
- Følg officiel Docker installation guide for dit operating system

### Images

#### Pulling Images from Registries

**Basic Command:**
```bash
docker pull python:3.11
```

**Forklaring:**
- Downloader officiel Python 3.11 image til din lokale maskine
- Format: `repository:tag`
  - `python` er repository navnet
  - `3.11` er tagget der specificerer versionen
- Hvis du udelader tagget, default Docker til `latest`

**Specific Variants:**
```bash
docker pull python:3.11-slim    # Smaller image with minimal packages
docker pull python:3.11-alpine  # Even smaller, based on Alpine Linux
```

**Extended Reading:**
- Docker Hub er bare én af mange container registries
- **Andre populære options:**
  - GitHub Container Registry (ghcr.io)
  - Google Container Registry (gcr.io)
- **Pull fra andre registries:**
  ```bash
  docker pull ghcr.io/joeferner/redis-commander:latest
  docker pull gcr.io/kaniko-project/executor:latest
  ```

#### Managing Images

**Essential Commands:**
```bash
# List all images on your machine
docker images

# Get detailed information about a specific image
docker inspect python:3.11

# Remove an image (only if no containers are using it)
docker rmi python:3.11

# Remove unused images to free up space
docker image prune
```

**Note:**
- `docker images` viser nyttig information som image størrelse, creation date, og unique image IDs
- Lignende images deler ofte layers, hvilket er hvorfor total størrelse af multiple Python images kan være mindre end forventet

### Running Containers

#### Basic Operations

**Basic Command:**
```bash
docker run python:3.11
```

**Forklaring:**
- Opretter og starter en ny container fra Python image
- Container starter og exit'er umiddelbart fordi der ikke er nogen long-running process til at holde den i live

**Useful Examples:**
```bash
# Run a simple Python command
docker run python:3.11 python -c "print('Hello from container!')"

# Run a container in the background that will run for one hour
docker run -d python:3.11 python -c "import time; time.sleep(3600)"
```

**Note:**
- `-d` flag kører containeren i "detached" mode (background uden at blokere din terminal)

#### Interactive Mode

**Get Shell Inside Container:**
```bash
# Get an interactive Python shell inside the container
docker run -it python:3.11 python

# Get a bash shell to explore the container
docker run -it python:3.11 bash
```

**Forklaring:**
- `-it` kombination giver dig en interaktiv terminal
- Inde i containeren kan du installere packages, køre scripts, eller udforske filesystem ligesom på enhver Linux maskine

#### Port Mapping

**For Web Applications eller APIs:**
```bash
# Run a simple HTTP server and map port 8000
docker run -p 8000:8000 python:3.11 python -m http.server 8000

# Map container port 8000 to host port 3000
docker run -p 3000:8000 python:3.11 python -m http.server 8000
```

**Forklaring:**
- `-p 8000:8000` mapper port 8000 inde i containeren til port 8000 på din host maskine
- Format: `host_port:container_port`
- Nu kan du besøge `http://localhost:8000` i din browser for at tilgå serveren kørende inde i containeren

#### Sharing Files and Configuration

**Volume Mounting:**
```bash
# Mount the current directory to /app inside the container
docker run -v $(pwd):/app python:3.11 ls /app

# Mount a specific file
docker run -v $(pwd)/script.py:/script.py python:3.11 python /script.py
```

**Forklaring:**
- `-v` flag opretter en volume mount med format `host_path:container_path`
- Filer du opretter eller modificerer i `/app` inde i containeren bliver faktisk lagret i dit nuværende directory på host maskinen

**Environment Variables:**
```bash
# Set environment variables
docker run -e DEBUG=true -e API_KEY=your_key python:3.11 python -c "import os; print(os.environ)"

# Load environment variables from a file
docker run --env-file .env python:3.11 python -c "import os; print(os.environ)"
```

**Note:**
- Særligt nyttigt til at konfigurere database connections, API keys, eller feature flags uden at hardcode dem i din applikation

### Managing Containers

#### Container Lifecycle

**Essential Commands:**
```bash
# List running containers
docker ps

# List all containers (including stopped ones)
docker ps -a

# Stop a running container
docker stop <container_id_or_name>

# Start a stopped container
docker start <container_id_or_name>

# Restart a container
docker restart <container_id_or_name>

# View container logs
docker logs <container_id_or_name>

# Follow logs in real-time
docker logs -f <container_id_or_name>
```

**Fun Fact:**
- Du behøver ikke at skrive fuld container ID
- Bare de første få karakterer er nok, så længe de er unikke

**Custom Names:**
```bash
# Run a container with a custom name
docker run --name my-python-app -d python:3.11 python -c "import time; time.sleep(300)"

# Now you can reference it by name
docker logs my-python-app
docker stop my-python-app
```

#### Executing Commands

**docker exec:**
```bash
# Execute a single command in a running container
docker exec my-python-app python -c "print('Hello from exec!')"

# Get an interactive shell in a running container
docker exec -it my-python-app bash

# Install additional packages in a running container
docker exec my-python-app pip install requests
```

**Note:**
- Utroligt nyttigt til debugging, installere additional tools, eller lave hurtige ændringer uden at recreere hele containeren

#### Cleaning Up

**Cleanup Commands:**
```bash
# Remove a specific stopped container
docker rm <container_id_or_name>

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove everything unused (containers, images, networks, build cache)
docker system prune
```

**Note:**
- Regelmæssig cleanup holder dit system ryddeligt og frigør disk plads

**Extended Reading:**
- **Docker Compose:**
  - Når du har brug for at køre multiple relaterede containers (fx web applikation med database)
  - Håndtering med individuelle `docker run` kommandoer bliver besværligt
  - Docker Compose løser dette ved at lade dig definere hele din multi-container applikation i en enkelt YAML fil
  - Kan også erstatte komplekse `docker run` kommandoer selv for single containers
  - Med `docker compose up` kan du starte alle services på én gang
  - Bliver essentielt for komplekse applikationer hvor containers har brug for at kommunikere med hinanden
  - Check Docker Compose quickstart og sample applications for praktiske eksempler

---

## 🔨 Build Containers

### Hvorfor Bygge Custom Images?

**Problem:**
- Pre-built images fra registries som Docker Hub er gode starting points
- Men de inkluderer ikke din specifikke kode, dependencies, eller configuration
- For at deploye image classification API serveren vi byggede i "Wrap AI Models with APIs", har vi brug for at oprette vores egen container image der bundler alt sammen

**Løsning:**
- Bygge custom container images transformerer din applikation fra noget der kræver manual setup på hver maskine
- Til en portable package der kører konsistent overalt
- I stedet for at bede brugere om at installere Python, downloade dependencies, konfigurere environment variables, og køre multiple kommandoer
- De kan simpelthen udføre `docker run your-app` og alt virker

### Interactive Approach (Ikke Anbefalet)

**Manual Approach:**
```bash
# Start an interactive Python container
docker run -it python:3.11 bash

# Inside the container, manually install dependencies
pip install fastapi uvicorn transformers torch pillow sqlalchemy

# Copy your application files (you'd need to mount or copy them somehow)
# Configure everything manually...

# Exit the container, then commit it as a new image
docker commit container_id my-app:latest
```

**Problemer:**
- Processen er ikke reproducible
- Ingen dokumentation af hvad der blev installeret
- Error-prone
- Kan ikke nemt version eller modificere dit setup
- Ligesom at lave mad uden opskrift - det virker måske én gang, men du vil kæmpe med at recreere det konsistent

### Dockerfile: The Recipe for Container Images

**Hvad er en Dockerfile?**
- En tekstfil der indeholder step-by-step instruktioner til at oprette dit image
- Husk lag-systemet vi diskuterede tidligere? En Dockerfile definerer præcist hvad der går ind i hvert lag
- Gør build processen komplet reproducible og dokumenteret

**Analog:**
- Tænk på en Dockerfile som en opskrift der fortæller Docker: "Start med denne base ingredient (base image), tilføj disse komponenter (dependencies), mix ind denne kode (din applikation), og server det på denne måde (startup command)"
- Enhver med din Dockerfile kan recreere det nøjagtige samme image, ligesom enhver kan følge en opskrift for at lave samme ret

**Layer Efficiency:**
- Hver instruktion i en Dockerfile opretter et nyt lag i dit image
- Hvis du kun ændrer din applikationskode, vil Docker genbruge alle cached layers for base image og dependencies
- Rebuilder kun hvad der er nødvendigt

### Dockerfile Instructions

**Foundation Instructions:**
- `FROM`: Specificerer hvilken base image at starte fra (altid første instruktion)
- `WORKDIR`: Sætter working directory for efterfølgende kommandoer

**File Operations:**
- `COPY`: Transfererer filer fra din host maskine til containeren
- `ADD`: Lignende til COPY men med additional features som at extracte archives

**Build-time Instructions:**
- `RUN`: Udfører kommandoer under build processen, som at installere packages
- `ARG`: Definerer build-time variabler der kan passes under build

**Runtime Configuration:**
- `ENV`: Sætter environment variabler der persisterer når containeren kører
- `EXPOSE`: Dokumenterer hvilke porte applikationen bruger (kun til dokumentation)
- `VOLUME`: Definerer mount points for persistent eller delt data

**Execution Instructions:**
- `CMD`: Giver default command og arguments (kan overrides)
- `ENTRYPOINT`: Sætter main command der altid kører (sværere at override)

**Struktur:**
- Start med foundation
- Tilføj dine filer
- Konfigurer build environment
- Sæt runtime properties
- Definer execution behavior

### Building the Image Classification Server

**Project Structure:**
```
my-ai-api/
├── Dockerfile
├── requirements.txt
├── main.py
└── ai_api.db (will be created)
```

**requirements.txt:**
```
fastapi==0.104.1
uvicorn==0.24.0
transformers==4.35.2
torch==2.1.1
pillow==10.1.0
sqlalchemy==2.0.23
```

**Dockerfile:**
```dockerfile
# Start with official Python 3.11 image (creates base layer)
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for better layer caching)
COPY requirements.txt .

# Install Python dependencies (creates dependency layer)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code (creates application layer)
COPY main.py .

# Create directory for database
RUN mkdir -p /app/data

# Expose port 8000 for the API
EXPOSE 8000

# Command to run when container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Forklaring af hver instruktion:**
- `FROM`: Specificerer base image. Vi bruger `python:3.11-slim` for mindre footprint
- `WORKDIR`: Sætter `/app` som working directory for efterfølgende kommandoer
- `COPY requirements.txt`: Kopierer kun requirements først for at udnytte Docker's layer caching
- `RUN pip install`: Installerer dependencies i et separat lag
- `COPY main.py`: Kopierer applikationskode i sit eget lag
- `EXPOSE`: Dokumenterer at containeren bruger port 8000 (publiserer faktisk ikke)
- `CMD`: Definerer default command når containeren starter

### Building and Running Your Container

**Build Image:**
```bash
# Navigate to your project directory
cd my-ai-api

# Build the image with a tag
docker build -t my-ai-classifier:v1.0 .
```

**Forklaring:**
- Docker vil udføre hver instruktion i din Dockerfile, oprette layers mens den går
- `-t` flag tagger image'et med et navn

**Run Container:**
```bash
# Run the container with port mapping
docker run -p 8000:8000 my-ai-classifier:v1.0

# Or run in detached mode with volume for persistent database
docker run -d -p 8000:8000 -v $(pwd)/data:/app/data --name ai-server my-ai-classifier:v1.0
```

**Resultat:**
- Din API server kører nu i en container!
- Du kan tilgå den på `http://localhost:8000` ligesom før
- Men nu kører alt i et komplet isoleret, reproducible environment

**Extended Reading:**
- **Advanced Practices:**
  - `.dockerignore` filer til at exclude unødvendige filer fra build context
  - Multi-stage builds for mindre production images
  - Dockerfile best practices for security og performance
- Disse teknikker bliver vigtigere som dine applikationer vokser i kompleksitet og du bevæger dig mod production deployments

---

## 📤 Distributing Your Images

### Container Registries

**Hvad er de?**
- Distribution hubs hvor du kan publicere dine images for andre at downloade og bruge
- Eksempler: Docker Hub, GitHub Container Registry, Google Container Registry

### Pushing to Docker Hub

**Process:**
```bash
# First, login to Docker Hub
docker login

# Tag your image with your Docker Hub username
docker tag my-ai-classifier:v1.0 yourusername/my-ai-classifier:v1.0

# Push the image to Docker Hub
docker push yourusername/my-ai-classifier:v1.0
```

**Forklaring:**
- Tagging step er crucial: følger format `registry/username/repository:tag`
- For Docker Hub, behøver du kun `username/repository:tag` da det er default registry

**Using Your Image:**
```bash
# Anyone can now run your containerized API server with a single command
docker run -p 8000:8000 yourusername/my-ai-classifier:v1.0
```

**Extended Reading:**
- **Andre Registries:**
  - GitHub Container Registry: `ghcr.io/username/repository:tag`
  - Google Container Registry: `gcr.io/project/repository:tag`
- **Automated Building:**
  - I stedet for at bygge images lokalt, kan du pushe din Dockerfile og source code til registry
  - Registry bygger image'et for dig
  - Særligt nyttigt for CI/CD pipelines hvor du vil have automated builds triggered af code changes
  - Services: Docker Hub's Automated Builds, GitHub Actions med Container Registry, cloud provider build services

---

## 📋 Opsummering til Mini Projekt

### Vigtige Koncepter (Påkrævet):

1. **Dockerfile** ✅ (Påkrævet)
   - Opret en omfattende Dockerfile
   - Brug instruktioner dækket i Dockerfile Instructions
   - Strukturer dine build layers korrekt for efficiency

2. **Build Process** ✅ (Påkrævet)
   - Følg processen demonstreret i Building and Running Your Container
   - Opret dit container image
   - Kør det med appropriate port mapping og volume mounting

3. **Test Functionality** ✅ (Påkrævet)
   - Verificer at din containerized API server virker identisk til original version
   - Alle endpoints skal være accessible og fungere korrekt

### Advanced Challenges (Optional):

4. **Optimization** ⭐ (Optional)
   - Implementer teknikker fra extended reading sektioner
   - Opret en `.dockerignore` fil
   - Udforsk multi-stage builds for mindre image størrelser

5. **Distribution** ⭐ (Optional)
   - Øv workflow fra Distributing Your Images
   - Push dit image til Docker Hub eller GitHub Container Registry
   - Gør det accessible til andre

### Dockerfile Best Practices:

1. **Layer Caching:**
   - Kopier `requirements.txt` først
   - Installer dependencies i separat lag
   - Kopier applikationskode sidst
   - Dette gør det muligt at genbruge cached layers når kun kode ændres

2. **Base Image:**
   - Brug `-slim` eller `-alpine` varianter for mindre images
   - `python:3.11-slim` er god balance mellem størrelse og funktionalitet

3. **Security:**
   - Brug `--no-cache-dir` med pip for at undgå at cache packages
   - Overvej at køre som non-root user (hvis muligt)

4. **Efficiency:**
   - Kombiner RUN kommandoer hvor muligt
   - Brug `.dockerignore` til at exclude unødvendige filer
   - Overvej multi-stage builds for production

### Eksempel Dockerfile til Mini Projekt:

```dockerfile
# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create data directory for database
RUN mkdir -p /app/data

# Expose API port
EXPOSE 8000

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### .dockerignore Eksempel:

```
__pycache__
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info
dist
build
.env
.venv
venv/
*.db
*.sqlite
.git
.gitignore
README.md
```

### Build og Run Commands:

```bash
# Build image
docker build -t ai-api-server:v1.0 .

# Run container
docker run -d -p 8000:8000 \
  -v $(pwd)/data:/app/data \
  --name ai-api-server \
  ai-api-server:v1.0

# View logs
docker logs -f ai-api-server

# Stop container
docker stop ai-api-server

# Remove container
docker rm ai-api-server
```

---

## ✅ Checklist til Mini Projekt

### Dockerfile
- [ ] Dockerfile oprettet
- [ ] FROM instruktion med appropriate base image
- [ ] WORKDIR sat
- [ ] Requirements kopieret først (for layer caching)
- [ ] Dependencies installeret
- [ ] Applikationskode kopieret
- [ ] Port exposed
- [ ] CMD eller ENTRYPOINT defineret
- [ ] .dockerignore oprettet (optional men anbefalet)

### Build Process
- [ ] Image bygget succesfuldt
- [ ] Ingen build errors
- [ ] Image tagget korrekt
- [ ] Image størrelse acceptable

### Running Container
- [ ] Container kører korrekt
- [ ] Port mapping fungerer
- [ ] Volume mounting fungerer (hvis nødvendigt)
- [ ] Environment variables sat (hvis nødvendigt)
- [ ] API server accessible fra host

### Testing
- [ ] Alle endpoints testet
- [ ] Funktionalitet identisk til non-containerized version
- [ ] Database persistence virker (hvis relevant)
- [ ] Logs viser korrekt

### Documentation
- [ ] Dockerfile kommenteret
- [ ] Build process dokumenteret
- [ ] Run kommandoer dokumenteret
- [ ] Eventuelle issues eller limitations dokumenteret

---

## 🎯 Exercise: Containerize Your AI API Server

**Opgave:** Transformer din image classification API server fra "Wrap AI Models with APIs" til en portable, reproducible container der kan køre overalt.

**Krav:**

1. **Write a Dockerfile:**
   - Opret en omfattende Dockerfile ved brug af instruktioner dækket i Dockerfile Instructions
   - Strukturer dine build layers korrekt for efficiency

2. **Build and Run:**
   - Følg processen demonstreret i Building and Running Your Container
   - Opret dit container image
   - Kør det med appropriate port mapping og volume mounting

3. **Test Functionality:**
   - Verificer at din containerized API server virker identisk til original version
   - Alle endpoints skal være accessible og fungere korrekt

**Advanced Challenges (Optional):**

4. **Optimization:**
   - Implementer teknikker fra extended reading sektioner
   - Opret en `.dockerignore` fil
   - Udforsk multi-stage builds for mindre image størrelser

5. **Distribution:**
   - Øv workflow fra Distributing Your Images
   - Push dit image til Docker Hub eller GitHub Container Registry
   - Gør det accessible til andre

**Mål:**
- Transformer din API fra en manual setup der kræver multiple installation steps
- Til en single-command deployment der virker konsistent på tværs af forskellige environments

---

## 🔗 Ressourcer

### Docker
- Docker Documentation: https://docs.docker.com/
- Docker Hub: https://hub.docker.com/
- Dockerfile Best Practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

### Docker Compose
- Docker Compose Documentation: https://docs.docker.com/compose/
- Docker Compose Quickstart: https://docs.docker.com/compose/gettingstarted/

### Alternative Frameworks
- Podman: https://podman.io/
- containerd: https://containerd.io/
- Open Container Initiative: https://opencontainers.org/

### Container Registries
- Docker Hub: https://hub.docker.com/
- GitHub Container Registry: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
- Google Container Registry: https://cloud.google.com/container-registry

### Advanced Topics
- Multi-stage Builds: https://docs.docker.com/build/building/multi-stage/
- .dockerignore: https://docs.docker.com/engine/reference/builder/#dockerignore-file
- Security Best Practices: https://docs.docker.com/develop/security-best-practices/

---

## 🎯 Konklusion

**Vigtige Takeaways:**

1. **Containers:**
   - Løser "it works on my machine" problem
   - Isolerede environments med alt nødvendigt
   - Portable og reproducible

2. **Docker:**
   - Industry standard container framework
   - Comprehensive toolkit (Engine, CLI, Dockerfile, Hub)
   - Client-server architecture

3. **Dockerfile:**
   - Recipe for container images
   - Layered system for efficiency
   - Reproducible builds

4. **For Mini Projekt:**
   - Dockerfile er påkrævet
   - Proper layer caching vigtigt
   - Test containerized version
   - Dokumenter build process

**Mål:**
- Transformer din API fra manual setup til single-command deployment
- Virker konsistent på tværs af forskellige environments
- Klar til deployment på EC2 serveren!

