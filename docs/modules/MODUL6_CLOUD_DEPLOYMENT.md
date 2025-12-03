# Modul 6: Cloud Deployment - Opsummering

**Kursus:** AI Systems & Infrastructure  
**Formål:** Lær hvordan man deployer din containerized AI API til cloud VMs, dækker remote access, Docker installation, og production-ready HTTPS setup.

---

## 📚 TL;DR

"Clouden" er bare computere i data centers du kan leje remote. Lær hvordan man deployer din containerized AI API til cloud VMs, dækker remote access, Docker installation, og production-ready HTTPS setup.

---

## 🎯 Hvorfor Cloud Deployment?

**Problemer med at køre på egen PC:**
- AI systemer, især API servers, skal typisk køre 24/7
- Du bør ikke stole på din egen PC til dette
- Kører AI systemer bruger ofte mange computational ressourcer
- Producerer varme og støj, noget du sandsynligvis ikke nyder derhjemme

**Løsning:**
- Deploy på "clouden"
- Cloud infrastructure er essentielt computere inde i data centers
- Setup på en måde der kan tilgås remote
- Cloud deployment (i de fleste tilfælde) kommer ned til deployment på en remote computer

---

## ☁️ Cloud Infrastructure

### Hvad er "the Cloud"?

**Definition:**
- Når vi taler om "the cloud," taler vi virkelig om computere i data centers du kan tilgå over internettet
- Udtrykket kommer fra gamle network diagrams hvor ingeniører ville tegne en cloud form for at repræsentere "internettet" eller ethvert netværk hvis interne detaljer ikke var vigtige i det øjeblik
- Over tid blev dette symbol associeret med computing ressourcer tilgået remote

**Historie:**
- Cloud infrastructure opstod fra et praktisk problem
- Virksomheder som Amazon og Google byggede massive computing faciliteter til at håndtere peak loads
- Disse dyre ressourcer sad mest idle under normale tider
- De indså de kunne leje denne spare kapacitet ud til andre
- Moderne cloud industri blev født

**Key Technical Innovation: Virtualization**
- Tillader én fysisk maskine at blive divideret i mange isolerede virtual machines
- Hver virker som en separat computer med sit eget operating system
- En enkelt kraftfuld server kan køre dusinvis af virtual machines for forskellige kunder samtidigt
- Dette sharing model forbedrede drastisk efficiency

**Containers vs VMs:**
- **VMs:** Virtualiserer hele hardwaren, giver hver VM sit eget komplette operating system
- **Containers:** Deler host's operating system kernel og isolerer kun applikationen og dens dependencies
- **VMs:** Tungere men mere isolerede, egnet til at køre helt forskellige operating systems
- **Containers:** Lettere og hurtigere, ideelle til at pakke applikationer
- **I praksis:** Cloud infrastructure bruger ofte begge - VMs til at dividere fysiske servers mellem kunder, og containers kørende inde i disse VMs til at pakke og deploye applikationer

**Tre Lag:**
1. **Physical Layer:**
   - Tusindvis af servers organiseret i racks inde i data centers
   - Forbundet af high-speed networks
   - Massive storage arrays
   - Redundant power og cooling systemer

2. **Virtualization Layer:**
   - Hypervisors opretter og styrer virtual machines
   - Allokerer slices af fysiske ressourcer
   - Sikrer isolation mellem kunder

3. **Management Layer:**
   - APIs til programmatic control
   - Orchestration systemer til resource allocation
   - Monitoring tools til health tracking
   - Billing systemer der måler usage

**Extended Reading:**
- What is a Data Center? fra AWS
- Understanding Hypervisors fra Red Hat
- What is Cloud Computing? fra AWS

---

## 🏢 Major Cloud Providers

### Amazon Web Services (AWS)

**Hvad er det?**
- Markedsleder, lanceret i 2006
- Amazon startede med at leje sin excess computing kapacitet ud
- Mest omfattende service catalog med over 200 services
- Dækker alt fra basic compute til specialiserede AI tools

**Karakteristika:**
- Kraftfuld men kan være overvældende for begyndere
- Kendt for sin modenhed
- Global reach med data centers i dusinvis af regioner
- Omfattende dokumentation
- De fleste enterprise virksomheder bruger AWS i nogen kapacitet

### Google Cloud Platform (GCP)

**Hvad er det?**
- Kom ind på markedet senere men bragte Google's expertise i at håndtere massive scale
- Excellerer i data analytics og AI/ML services
- Tools som BigQuery for data warehousing og Vertex AI for machine learning

**Karakteristika:**
- Tender til at være mere developer-friendly
- Renere interfaces og bedre default configurations
- For AI system deployment, GCP's styrker i machine learning infrastructure og konkurrencedygtig GPU pricing gør det særligt attraktivt

### Microsoft Azure

**Hvad er det?**
- Stærk appel for enterprises der allerede bruger Microsoft produkter
- Integrerer seamlessly med Windows Server, Active Directory, og Office 365
- Naturligt valg for organisationer med eksisterende Microsoft infrastructure

**Karakteristika:**
- Vokset hurtigt og rivaliserer nu AWS i service offerings
- Særlig styrke i hybrid cloud scenarier hvor virksomheder har brug for at forbinde on-premises systemer med cloud ressourcer

### Alternativer

**Affordable og Simple:**
- **DigitalOcean** og **Linode:** Straightforward interfaces og konkurrencedygtig pricing, ideelle til startups og mindre projekter

**GPU-Focused for AI:**
- **Lambda Labs** og **CoreWeave:** Specialiserer sig i at levere cost-effective GPU instances optimeret til machine learning workloads

**European Providers:**
- **Hetzner (Tyskland):** Kendt for exceptionel price-performance ratios med data centers på tværs af Europa
- **OVHcloud (Frankrig):** Opererer en af Europas største cloud infrastrukturer
- **Scaleway (Frankrig):** Positionerer sig som et europæisk alternativ med stærke AI capabilities
- Disse providers koster ofte betydeligt mindre end US hyperscalers mens de holder data inden for EU jurisdiktion

---

## 🛠️ Common Cloud Services

### Virtual Machines (VMs)

**Hvad er det?**
- Dedikerede computing instances der opfører sig som traditionelle servers
- Du får fuld kontrol over operating systemet
- Kan installere hvad som helst software du har brug for

**Fordele:**
- Familiarity hvis du er komfortabel med traditionel server management
- Fuldt kontrol

**Ulemper:**
- Du er ansvarlig for alt maintenance, security patches, og configuration
- Du betaler for VM'en uanset om den aktivt processerer requests eller sidder idle

**Eksempler:**
- EC2 på AWS
- Compute Engine på GCP
- Virtual Machines på Azure

### Container Services

**Hvad er det?**
- Lader dig køre Docker containers vi lærte om i Packaging & containerization
- Cloud provider styrer underlying infrastructure mens du fokuserer på dine containerized applikationer
- Mange container services tilbyder automatisk scaling

**Fordele:**
- Automatisk scaling (spinner op flere containers når trafik stiger)
- Du betaler kun for faktisk usage

**Ulemper:**
- Learning curve kan være stejlere end VMs
- Debugging containerized applikationer i production kræver forskellige skills

**Eksempler:**
- ECS/EKS på AWS
- Cloud Run på GCP
- Container Instances på Azure

### GPU Instances

**Hvad er det?**
- Virtual machines med attached graphics processing units
- Essentielt til at træne store AI modeller eller køre inference på komplekse modeller

**Fordele:**
- Uden at købe dyrt hardware upfront, får du adgang til cutting-edge GPUs

**Ulemper:**
- Cost: GPU instances kan køre hundreder af dollars per dag
- Under peak times (fx når ny AI research skaber efterspørgsel), kan de være unavailable

**Eksempler:**
- P-series og G-series instances på AWS
- A2 og G2 instances på GCP
- NC og ND-series på Azure

### Managed AI Services

**Hvad er det?**
- Pre-konfigurerede platforms specifikt til at deploye machine learning modeller
- Disse services håndterer infrastructure scaling, model versioning, monitoring
- Ofte inkluderer tools til A/B testing forskellige model versioner

**Fordele:**
- Nemmeste måde at deploye AI systemer
- Kræver minimal DevOps viden

**Ulemper:**
- Mindre fleksibilitet
- Potentiel vendor lock-in, da disse platforms ofte bruger proprietary APIs

**Eksempler:**
- SageMaker på AWS
- Vertex AI på GCP
- Azure Machine Learning på Azure

### Object Storage

**Hvad er det?**
- Skalerbar storage til store datasets, model filer, og anden unstructured data
- Designet til durability og massive scale
- Filer er typisk replikerede på tværs af multiple data centers

**Fordele:**
- Data loss er ekstremt usandsynligt
- Storage costs er bemærkelsesværdigt billige (typisk få cents per gigabyte per måned)

**Ulemper:**
- Ikke designet til real-time access
- Operationer har højere latency end lokale disks
- Egnet til at lagre training data og model weights, men ikke til at serve predictions

**Eksempler:**
- S3 på AWS
- Cloud Storage på GCP
- Blob Storage på Azure

**Extended Reading:**
- **Serverless computing:** AWS Lambda, Google Cloud Functions
- **Managed databases:** RDS, Cloud SQL, Cosmos DB
- **Content delivery networks:** CloudFront, Cloud CDN

---

## 🎯 Choosing the Right Service

### Overvejelser

1. **Technical Expertise:**
   - Nogle services kræver dyb viden om server management
   - Andre abstracter det væk
   - Tænk over om du er komfortabel med at SSH ind i en server, styre operating system opdateringer, og debugge infrastructure issues

2. **Scaling Requirements:**
   - Hvis du forventer steady, forudsigelig trafik, virker en simpel always-on server fint
   - Hvis trafik fluktuerer drastisk, kan du drage fordel af services der skalerer automatisk

3. **Budget:**
   - Ikke bare om totalt beløb du kan bruge
   - Overvej om du har brug for forudsigelige månedlige omkostninger til planlægningsformål
   - Eller om du er komfortabel med variable regninger der afhænger af faktisk usage

4. **Level of Control:**
   - Nogle applikationer kræver specifikke system configurations, custom networking setups, eller særlige security arrangements
   - Kun low-level services som VMs kan levere dette

5. **Timeline:**
   - Hvor hurtigt har du brug for at få dit system kørende?
   - Nogle services lader dig deploye på timer, mens andre kræver dage eller uger af setup og læring

### Anbefaling: Start med VMs

**Fordele ved VMs med Fixed Pricing:**

1. **Cost Predictability:**
   - Når du lejer en VM til en fast månedlig rate, ved du præcist hvad du vil betale
   - Ingen overraskelser
   - Du kan køre din applikation, lave fejl under development, og eksperimentere frit uden at bekymre dig om en uventet regning ved månedens slutning
   - Særligt værdifuldt når du lærer eller kører services med steady traffic patterns

2. **Direct Control:**
   - Med en VM styrer du operating systemet, installerer software, og konfigurerer alt selv
   - Mens dette kræver mere arbejde upfront, bygger det din forståelse af hvordan systemer faktisk virker
   - Du kan troubleshoote issues ved at logge ind på serveren, tjekke processer, og undersøge logs direkte
   - Denne transparency gør debugging meget simplere sammenlignet med managed services hvor problemer kan være skjult bag abstraction layers

**Beware Usage-based Pricing Pitfalls:**
- Cloud industrien har talrige horror stories om uventede regninger
- I 2024 vågnede en udvikler op til en $104,500 regning fra Netlify for en simpel dokumentations site
- Et andet tilfælde så Cloudflare kræve $120,000 inden for 24 timer
- AWS Lambda funktioner kan se costs spike 11x fra network delays alene
- Selv en misconfigured S3 bucket resulterede i $1,300 i charges fra uautoriserede requests på en enkelt dag
- Disse er ikke sjældne edge cases
- De sker regelmæssigt fordi usage-based pricing gør costs svære at forudsige og nemme at miste track af

**Vendor Lock-in:**
- Når du bruger managed AI platforms som SageMaker eller Vertex AI, skriver du ofte kode der afhænger af deres proprietary APIs
- Research viser 71% af organisationer citerer vendor lock-in som en deterrent til at adoptere flere cloud services
- At migrere væk kræver at omskrive betydelige dele af din applikation
- Data formater kan være inkompatible
- Features du stolede på eksisterer måske ikke andre steder
- Switching costs bliver så høje at du effektivt er locked ind i den providers ecosystem

**Anbefaling for Image Classification API Server:**
- En lille VM der kører din Docker container
- Du får fuldt kontrol, forudsigelige månedlige omkostninger (typisk $5-20 for basic instances)
- Evnen til at scale op ved at skifte til en større VM når nødvendigt
- Denne tilgang lærer dig cloud fundamentals uden risikoen for surprise bills eller vendor lock-in
- Som du får erfaring og dine requirements bliver klarere, kan du træffe informerede beslutninger om hvorvidt managed services retfærdiggør deres additional kompleksitet og cost uncertainty

**Extended Reading:**
- The Dark Side of Cloud Computing: Unexpected Costs
- Critical Analysis of Vendor Lock-in
- Understanding AWS Lambda Costs

---

## 🚀 Cloud Deployment in Practice

### Selecting Your Virtual Machine

**Beslutninger du skal træffe:**

1. **Operating System:**
   - Vælg en Linux distribution
   - **Ubuntu LTS** (22.04 eller 24.04) er fremragende valg
   - Modtager security updates i fem år
   - Omfattende community dokumentation
   - De fleste cloud providers tilbyder Ubuntu som one-click option
   - Andre gode alternativer: Debian eller Rocky Linux

2. **CPU og Memory:**
   - For at køre vores containerized AI API server uden GPU acceleration, start med en beskeden konfiguration
   - **2-4 virtual CPUs** og **4-8 GB RAM** håndterer de fleste små til medium traffic loads komfortabelt
   - Husk: Du kører model inference på CPU, ikke træner den
   - Hvis du finder performance manglende senere, kan du upgrade til en større instance
   - At starte småt holder costs nede mens du lærer og tester

3. **Storage:**
   - Alloker **20-30 GB** disk plads
   - Dækker operating system (typisk 5-10 GB), Docker selv (et par GB), dine container images (varierer efter model størrelse, men typisk under 5 GB for vores API server), og plads til logs og temporary filer
   - De fleste providers opkræver ekstra for additional storage ud over et base beløb
   - Over-alloker ikke - du kan udvide storage senere hvis nødvendigt

4. **Network Configuration:**
   - Sørg for at din VM får en **public IP adresse** så du kan tilgå den fra internettet
   - De fleste providers tildeler en automatisk, men nogle kræver at du eksplicit anmoder om det
   - Du skal også konfigurere **security groups** eller **firewall rules** til at tillade indkommende trafik på specifikke porte
   - Minimum: Åbn port 22 for SSH access (så du kan logge ind) og port 8000 for din API server
   - Mange providers default til at blokere al indkommende trafik for security, så du skal eksplicit tillade disse porte

5. **Authentication:**
   - De fleste providers tilbyder **SSH key-based authentication** under VM oprettelse
   - Hvis givet muligheden, giv din public SSH key nu
   - Dette er mere sikkert end password authentication og sparer setup tid senere
   - Hvis du ikke har en SSH key endnu, kan du generere en lokalt før du opretter VM'en

**Cost:**
- En typisk lille VM egnet til vores formål koster **$5-20 per måned** afhængigt af provider og region
- Europæiske providers som Hetzner tilbyder ofte bedre price-performance ratios end de store cloud providers for basic VMs
- Start med den mindste konfiguration der opfylder minimum requirements
- Du kan altid scale op, men du kan ikke få penge tilbage for over-provisioning

### Accessing Your Remote Server

**SSH (Secure Shell):**
- SSH er en protokol der lader dig securely connecte til og kontrollere en remote computer over internettet
- Tænk på SSH som en sikker remote control til din server
- Krypterer al kommunikation mellem din lokale computer og remote serveren
- Når du SSH ind i en server, får du en command-line interface ligesom hvis du sad ved den maskines keyboard

**First Connection:**
- Efter din VM er oprettet, giver din cloud provider dig dens public IP adresse (fx `203.0.113.42`)
- Du har også brug for et brugernavn, som varierer efter provider
- Mange VMs default til root user (administrator kontoen med fulde system privilegier)
- Ubuntu VMs fra store cloud providers bruger typisk `ubuntu`
- Azure bruger ofte `azureuser`
- Nogle providers lader dig vælge under oprettelse

**Connect:**
```bash
ssh username@203.0.113.42
```

- Første gang du connecter, vil du se en advarsel der spørger om du stoler på denne server
- Type `yes` for at fortsætte
- Hvis du satte password authentication op, bliver du bedt om en password
- Når autentificeret, vil du se en command prompt der indikerer du nu kontrollerer remote serveren

**SSH Keys (More Secure):**
- Password authentication virker, men SSH keys er mere sikre og bekvemme
- Et SSH key par består af en private key (holdes hemmeligt på din computer) og en public key (deles med servers)
- Tænk på det som en speciel lås og nøgle: du giver servers en kopi af låsen (public key), og kun din nøgle (private key) kan åbne den

**Generate SSH Key Pair:**
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

- Dette opretter to filer i `~/.ssh/`:
  - `id_ed25519` (private key, del aldrig denne)
  - `id_ed25519.pub` (public key)
- Når bedt om passphrase, kan du trykke Enter for at springe over for bekvemmelighed, selvom at tilføje en giver ekstra security

**Add Public Key to Server:**
```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "your-public-key-content-here" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

- Hvis du oprettede din VM uden at give en public key, kan du tilføje den nu ved at logge ind med password authentication og køre ovenstående kommandoer
- Fra da af kan du SSH uden passwords

**First Tasks After Login:**
```bash
# Update package lists and upgrade existing packages
sudo apt update && sudo apt upgrade -y

# Create a new user (skip if you already have a non-root user)
adduser yourname

# Give the new user sudo privileges
usermod -aG sudo yourname
```

- Dette sikrer dit system har de seneste security patches
- `sudo` kommandoen kører kommandoer som administrator (root user)
- På Ubuntu har default user sudo privilegier
- Hvis du er logget ind som root direkte, kan du udelade sudo fra kommandoer, selvom det stadig er god praksis at oprette en regular user til dagligt arbejde
- At arbejde som root for rutineopgaver er risikabelt fordi det er for let at ved et uheld skade systemet med en mistyped kommando

**Configure Firewall:**
```bash
# Allow SSH so you don't lock yourself out
sudo ufw allow 22/tcp

# Allow your API server port
sudo ufw allow 8000/tcp

# Enable the firewall
sudo ufw enable
```

- Denne firewall kører på VM'en selv og tilføjer et ekstra lag af beskyttelse ud over din cloud providers security groups
- Nu har du en frisk konfigureret, sikker server klar til at installere Docker og deploye din applikation

### Installing Docker

**Why Not Convenience Scripts?**
- Du finder måske guides der foreslår du kan installere Docker med en enkelt kommando: `curl https://get.docker.com | sh`
- Mens dette virker, advarer Docker's egen dokumentation mod at bruge det i production environments
- Scriptet giver dig ikke kontrol over hvilken version der bliver installeret og kan opføre sig uventet under system opdateringer
- For læring og production deployments, bygger at tage den proper tilgang bedre vaner

**Installation Steps:**
```bash
# Remove any old or conflicting Docker installations
sudo apt remove docker docker-engine docker.io containerd runc

# Install packages to allow apt to use repositories over HTTPS
sudo apt install -y ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Set up the Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update apt package index
sudo apt update

# Install Docker Engine, containerd, and Docker Compose
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

- Disse kommandoer sætter Docker's officielle package repository op så apt ved hvor den skal downloade Docker fra
- Dette installerer flere komponenter:
  - `docker-ce` er Docker Engine selv
  - `docker-ce-cli` giver command-line interface
  - `containerd.io` er container runtime
  - Plugins tilføjer nyttige features som at bygge images og styre multi-container applikationer

**Verify Installation:**
```bash
sudo docker run hello-world
```

- Du skulle se en besked der forklarer at Docker successfully pulled og kørte et test image
- Dette bekræfter alt virker

**Adding Your User to the Docker Group:**
```bash
# Add your user to the docker group
sudo usermod -aG docker $USER

# Apply the group change (or log out and back in)
newgrp docker
```

- Nu kan du køre Docker kommandoer uden `sudo`
- Vær opmærksom på at dette er en security overvejelse: brugere i docker gruppen har effektivt root-level privilegier fordi de kan køre containers med fuldt system access
- For en personlig læringsserver er denne trade-off acceptable
- I multi-user production environments, vil du have brug for mere omhyggelig access controls

**Test:**
```bash
docker run hello-world
```

- Hvis dette virker uden at kræve en password, er du klar
- Docker er nu installeret og klar til at køre dine containerized applikationer

### Deploying Your Container

**Option 1: Pull from a Registry (Anbefalet)**
```bash
docker pull yourusername/my-ai-classifier:v1.0
```

- Hvis du pushed dit image til Docker Hub eller en anden registry som beskrevet i Packaging & containerization, kan du pull det direkte på din server
- Dette downloader dit image fra registry
- Det er den reneste tilgang fordi image building skete på din lokale maskine eller i et automatiseret build system, og serveren skal bare køre det

**Option 2: Build on the Server**
```bash
# Run this on your local machine, not the server
scp -r ~/path/to/my-ai-api username@203.0.113.42:~/

# Then SSH into your server and build the image
cd ~/my-ai-api
docker build -t my-ai-classifier:v1.0 .
```

- Hvis du ikke har publiceret dit image til en registry, kan du bygge det direkte på serveren
- Først, transfer dine projekt filer (Dockerfile, requirements.txt, main.py) til serveren ved brug af SCP (Secure Copy)
- Derefter SSH ind i din server og byg image'et
- At bygge på serveren virker men bruger server ressourcer og tager længere tid
- For production workflows, er det renere at bruge en registry og tillader dig at teste images lokalt før du deployer dem

**Running Your Container:**
```bash
docker run -d -p 8000:8000 --restart unless-stopped --name ai-api my-ai-classifier:v1.0
```

**Forklaring af hver flag:**
- `-d`: Kører containeren i detached mode (i baggrunden)
- `-p 8000:8000`: Mapper port 8000 på host til port 8000 i containeren, gør din API accessible
- `--restart unless-stopped`: Fortæller Docker at automatisk genstarte containeren hvis den crasher eller når serveren rebooter (men ikke hvis du manuelt stoppede den)
- `--name ai-api`: Giver containeren et venligt navn så du kan referere til den nemt
- `my-ai-classifier:v1.0`: Er image navnet og tag at køre

**With Persistent Data:**
```bash
docker run -d -p 8000:8000 --restart unless-stopped \
  -v ~/ai-data:/app/data \
  --name ai-api my-ai-classifier:v1.0
```

- Hvis din applikation har brug for persistent data (som SQLite databasen fra vores API server), mount en volume
- Dette opretter en directory `~/ai-data` på din server og mount den til `/app/data` inde i containeren
- Så database filer persisterer selv hvis containeren bliver recreated

**Verification:**
```bash
# Check that your container is running
docker ps

# View the container's logs to ensure it started properly
docker logs ai-api

# Test the API locally on the server
curl http://localhost:8000
```

- Du skulle se din `ai-api` container listet med status "Up"
- View container's logs for at sikre den started korrekt
- Du skulle se output fra uvicorn der indikerer serveren started successfully
- Nu test API'en lokalt på serveren
- Hvis du får et response (sandsynligvis din API's root endpoint besked), virker containeren
- Endelig, test fra din lokale maskine ved at besøge `http://203.0.113.42:8000` i din browser (erstat med din servers faktiske IP)
- Hvis du ser din API respondere, tillykke! Din containerized AI applikation kører nu på clouden

**Troubleshooting:**
- Hvis du ikke kan tilgå den eksternt, dobbelttjek at din cloud providers security group tillader indkommende trafik på port 8000
- Og at UFW tillader det (`sudo ufw status` skulle vise port 8000 allowed)

---

## 🔧 Production Considerations

### Container Persistence

**--restart unless-stopped:**
- Vi brugte `--restart unless-stopped` når vi kørte containeren, hvilket håndterer to vigtige scenarier
- Hvis din applikation crasher på grund af en bug eller løber tør for memory, genstarter Docker automatisk den
- Vigtigere: Når du rebooter din server for system opdateringer, starter containeren automatisk op igen
- Uden dette flag, skulle du manuelt køre `docker start ai-api` efter hver server restart

**Verify:**
```bash
# View container details including restart policy
docker inspect ai-api | grep -A 5 RestartPolicy
```

### Basic Monitoring

**Essential Commands:**
```bash
# Check if the container is running
docker ps

# View recent logs (last 50 lines)
docker logs --tail 50 ai-api

# Follow logs in real-time
docker logs -f ai-api

# Check resource usage
docker stats ai-api
```

- `docker stats` kommandoen viser CPU og memory usage
- Hvis du bemærker memory stige stabilt over dage, har du måske en memory leak i din applikation
- For vores API server, skulle memory usage forblive relativt stabilt

**Monitor Disk Space:**
```bash
# Check overall disk usage
df -h

# See Docker's disk usage
docker system df
```

- Monitor disk plads regelmæssigt fordi Docker images og logs forbruger plads

**Cleanup:**
```bash
# Remove unused images
docker image prune -a

# Remove everything unused (images, containers, networks)
docker system prune
```

- Vær forsigtig med `docker system prune` da det fjerner alle stoppede containers og unused images
- Kør kun det når du er sikker på du ikke har brug for dem

### Simple Maintenance

**Update Process:**
```bash
# Pull the new version of your image
docker pull yourusername/my-ai-classifier:v2.0

# Stop and remove the old container
docker stop ai-api
docker rm ai-api

# Run the new version
docker run -d -p 8000:8000 --restart unless-stopped \
  -v ~/ai-data:/app/data \
  --name ai-api yourusername/my-ai-classifier:v2.0
```

- Denne tilgang forårsager downtime mens du skifter containers
- For de fleste læring og små production use cases, er et par sekunders downtime under off-peak timer acceptable

### Backing Up Data

**If your container uses volumes for persistent data:**
```bash
# Create a backup directory
mkdir -p ~/backups

# Backup the data directory
tar -czf ~/backups/ai-data-$(date +%Y%m%d).tar.gz ~/ai-data
```

- Kør dette som en cron job for automatiske daglige backups
- Du kan også kopiere backups til din lokale maskine:
```bash
# On your local machine
scp username@203.0.113.42:~/backups/ai-data-*.tar.gz ~/local-backups/
```

**Extended Reading:**
- **BorgBackup:** Automatiseret, krypteret, og deduplicated backups
- **Docker Log Rotation:** Forhindrer logs i at forbruge al disk plads
- **Zero-Downtime Deployments:** Blue-green strategier tillader dig at opdatere containers uden service interruption

---

## 🔒 Enabling HTTPS for Production

### Hvorfor HTTPS?

**Problem:**
- Din API server kører nu og er accessible på `http://your-server-ip:8000`
- Dette virker til testing, men er ubrugeligt til production
- Moderne web browsers håndhæver strikte security policies der gør HTTP APIs upraktiske for rigtige applikationer

**The Mixed Content Problem:**
- Hvis din frontend website serveres over HTTPS (hvilket den skal være for at brugere stoler på den), vil browsers blokere ethvert HTTP requests den prøver at lave
- Dette kaldes mixed content blocking
- I 2024 bruger cirka 93% af alle web requests HTTPS
- Browsers som Firefox opgraderer eller blokerer automatisk non-HTTPS ressourcer
- Du kan simpelthen ikke have en moderne web applikation der laver HTTP API calls fra en HTTPS side

**Security Implications:**
- HTTP trafik transmitteres i plain text
- Enhver mellem dine brugere og din server (din ISP, coffee shop WiFi, eller malicious actors) kan læse og modificere dataene
- Med en AI API der potentielt håndterer sensitiv information eller brugerdata, er dette uacceptabelt
- HTTPS krypterer al kommunikation, sikrer data integritet og fortrolighed

**Professional Expectations:**
- Brugere forventer at se et padlock ikon i deres browsers address bar
- Browsers viser prominente advarsler for HTTP sites, skader tillid før brugere endda interagerer med din service
- Search engines straffer også HTTP sites i rankings

**For at gøre din API production-ready, har du brug for HTTPS, hvilket kræver et domain navn og et SSL/TLS certifikat**

### Understanding SSL/TLS Basics

**HTTPS:**
- HTTPS virker gennem SSL/TLS certifikater, som er digitale dokumenter der beviser du ejer et domain og muliggør krypteret kommunikation
- Når en bruger connecter til `https://yourdomain.com`, udfører deres browser og din server en "handshake" hvor de udveksler certifikater og etablerer en krypteret forbindelse
- Al efterfølgende data flyder gennem denne krypterede kanal, forhindrer eavesdropping og tampering

**Certificate Authorities (CAs):**
- Trusted organisationer der udsteder certifikater efter at verificere du kontrollerer et domain
- Historisk kostede SSL certifikater hundreder af dollars per år, skabte en barriere for små projekter og hobbyister
- Dette ændrede sig i 2016 da Let's Encrypt, en nonprofit CA, begyndte at tilbyde gratis automatiseret certifikater
- I dag har Let's Encrypt udstedt certifikater til over 700 millioner websites, gør HTTPS accessible til alle

**The Role of Reverse Proxies:**
- Din containerized applikation kører på port 8000 inde i serveren, lytter efter plain HTTP requests
- Vi vil ikke modificere containeren til at håndtere HTTPS direkte fordi at styre certifikater inde i containers er komplekst og ufleksibelt
- I stedet bruger vi en reverse proxy (Nginx) der sidder foran din container
- Proxien håndterer HTTPS på port 443 (standard HTTPS port), terminerer SSL forbindelsen, og forwarder dekrypterede requests til din container på port 8000
- Din container ved aldrig HTTPS er involveret, holder arkitekturen simpel

### Getting a Domain Name

**Free Option: DuckDNS**
- DuckDNS giver gratis subdomains perfekt til læring og personlige projekter
- Du får et domain som `yourname.duckdns.org` uden at betale noget
- Service er simpel:
  1. Besøg duckdns.org og log ind med GitHub, Google, eller Twitter (ingen separat registrering nødvendig)
  2. Vælg et tilgængeligt subdomain navn
  3. Peg det til din servers IP adresse gennem deres web interface
- DuckDNS giver også en API til at opdatere din IP hvis den ændrer sig, nyttigt til home servers
- Hovedbegrænsning: Dit domain vil være længere (fx `my-ai-api.duckdns.org`) og mindre professionelt end et custom domain
- Til læring og testing HTTPS setup, er DuckDNS perfekt

**Paid Option: Domain Registrars**
- Til production applikationer, overvej at købe dit eget domain
- **Cloudflare Registrar:** Sælger domains til cost med ingen markup. Et .com domain koster omkring $10/year. Højt anbefalet af udviklere for transparent pricing og fremragende DNS management tools
- **Porkbun:** Kendt for konsistent pricing med ingen renewal hikes. .com domains omkring $11/year
- **Namecheap:** Populært valg med gode features og support. .com domains omkring $16/year for renewals. Inkluderer gratis WHOIS privacy
- Når du vælger en registrar, fokuser på renewal priser, ikke bare first-year promotional rates

### Setting Up DNS Records

**Process:**
1. Find din servers public IP adresse (vist i din cloud providers dashboard)
2. I din domain providers DNS indstillinger, opret en A record:
   - **Name:** `@` (eller lad blank for root domain) eller et subdomain som `api`
   - **Type:** A
   - **Value:** Din servers IP adresse (fx `203.0.113.42`)
   - **TTL:** 3600 (eller default)
3. For DuckDNS, indtaster du simpelthen din IP i deres web interface
4. For andre registrars, naviger til DNS management sektionen af dit dashboard
5. DNS ændringer kan tage et par minutter til et par timer at propagere worldwide, selvom de typisk er effektive inden for 15 minutter

**Verify DNS:**
```bash
ping yourdomain.com
```

- Hvis det resolver til din servers IP adresse, er DNS konfigureret korrekt

### Manual SSL Setup (Nginx + Certbot)

**Setting Up Nginx Reverse Proxy:**

**Install Nginx:**
```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl status nginx
```

- Nginx starter automatisk efter installation
- Du kan verificere den kører

**Create Nginx Configuration:**
```bash
sudo nano /etc/nginx/sites-available/your-domain
```

**Add Configuration:**
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

- Erstat `yourdomain.com` med dit faktiske domain
- Denne konfiguration fortæller Nginx at:
  - Lytte på port 80 for HTTP requests
  - Acceptere requests for dit domain
  - Forwarde alle requests til localhost:8000 (hvor din Docker container kører)
  - Pass along vigtige headers så din applikation ved den originale clients IP og protokol

**Enable the Configuration:**
```bash
# Create a symbolic link to enable the site
sudo ln -s /etc/nginx/sites-available/your-domain /etc/nginx/sites-enabled/

# Test the configuration for syntax errors
sudo nginx -t

# If the test passes, reload Nginx
sudo systemctl reload nginx
```

**Test the Proxy:**
```bash
curl http://yourdomain.com
```

- Nu skulle du kunne tilgå din API gennem dit domain navn ved brug af HTTP
- Din browser skulle også virke på `http://yourdomain.com`
- Containeren kører stadig på port 8000, men Nginx proxier nu requests til den fra port 80
- På dette tidspunkt har du en working reverse proxy, men du bruger stadig HTTP
- Næste step er at tilføje SSL certifikater for HTTPS

**Obtaining SSL Certificates with Certbot:**

**Install Certbot:**
```bash
sudo apt install certbot python3-certbot-nginx -y
```

- `python3-certbot-nginx` package inkluderer Nginx plugin der tillader Certbot at automatisk konfigurere Nginx for HTTPS

**Configure Firewall:**
```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

- Før du kører Certbot, sikre trafik på porte 80 og 443 er tilladt
- Let's Encrypt bruger port 80 til domain validation, og port 443 er til HTTPS trafik
- Du skal konfigurere dette på to steder:
  1. Opdater din servers firewall (UFW)
  2. Sikre din cloud providers security group eller firewall rules også tillader disse porte
- I din cloud providers dashboard, tjek security group attached til din VM og verificer at inbound rules tillader TCP trafik på porte 80 og 443 fra anywhere (0.0.0.0/0)
- Uden dette kan Let's Encrypt ikke nå din server for at validere domain ownership

**Obtain and Install Certificate:**
```bash
sudo certbot --nginx -d yourdomain.com
```

- Erstat `yourdomain.com` med dit faktiske domain
- Hvis du bruger et subdomain (som `api.yourdomain.com`), brug det i stedet

**Certbot Process:**
1. Spørger om din email adresse (til renewal notifications)
2. Spørger dig om at acceptere terms of service
3. Spørger om du vil modtage EFF newsletters (optional)
4. Validerer at du kontrollerer domainet ved at placere en temporary fil på din server og verificere Let's Encrypt kan tilgå den via HTTP
5. Obtener SSL certifikatet
6. Automatisk modificerer din Nginx konfiguration til at bruge certifikatet
7. Sætter automatisk HTTP til HTTPS redirection op

**How Domain Validation Works:**
- Let's Encrypt har brug for at verificere du kontrollerer domainet før udstedelse af certifikat
- HTTP-01 challenge virker ved:
  1. Certbot opretter en fil i `/var/www/html/.well-known/acme-challenge/`
  2. Let's Encrypt's servers anmoder om denne fil via `http://yourdomain.com/.well-known/acme-challenge/[random-string]`
  3. Hvis filen successfully hentes, er domain ownership bevist
  4. Certifikatet udstedes
- Dette er hvorfor dit domain allerede skal pege på din servers IP og port 80 skal være accessible fra internettet

**Automatic Renewal:**
```bash
# Test the renewal process
sudo certbot renew --dry-run

# Check the renewal timer status
sudo systemctl status certbot.timer
```

- Let's Encrypt certifikater udløber hver 90. dag, men Certbot sætter automatisk en systemd timer op til at fornye certifikater før de udløber
- Hvis denne kommando lykkes, er automatisk renewal konfigureret korrekt
- Du behøver ikke at gøre noget andet; certifikater vil fornye automatisk i baggrunden

**What Certbot Changed:**
- Efter Certbot er færdig, vil din Nginx konfigurationsfil (`/etc/nginx/sites-available/your-domain`) se betydeligt anderledes ud
- Certbot tilføjede:
  - Et nyt server block der lytter på port 443 for HTTPS
  - Stier til dit SSL certifikat og private key
  - SSL security indstillinger
  - En redirect fra HTTP (port 80) til HTTPS (port 443)

**View Updated Configuration:**
```bash
sudo cat /etc/nginx/sites-available/your-domain
```

- Din API er nu accessible via HTTPS på `https://yourdomain.com`

### Automatic SSL Setup (Traefik)

**Hvad er Traefik?**
- Traefik er en moderne reverse proxy bygget til dynamiske container environments
- I modsætning til Nginx der kræver konfigurationsfiler, watcher Traefik dine Docker containers og konfigurerer sig selv automatisk baseret på labels du tilføjer til disse containers
- Når en ny container starter med appropriate labels, begynder Traefik umiddelbart at route trafik til den og kan automatisk anmode om et SSL certifikat

**Hvorfor Vælge Traefik?**
- Traefik excellerer i environments der kører multiple containerized services
- I stedet for at redigere Nginx konfigurationsfiler og køre Certbot for hvert nyt domain, tilføjer du simpelthen labels til din Docker container
- Traefik håndterer resten: routing, SSL certifikater, renewals, og load balancing
- For en enkelt API server, kan dette virke som overkill, men det demonstrerer moderne cloud-native patterns og skalerer effortless som din infrastructure vokser

**Setting Up Traefik:**
```bash
# Create a Docker network
docker network create traefik-network

# Create a directory to store SSL certificates
mkdir ~/traefik-certs
chmod 600 ~/traefik-certs

# Start the Traefik container
docker run -d \
  --name traefik \
  --network traefik-network \
  -p 80:80 \
  -p 443:443 \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v ~/traefik-certs:/letsencrypt \
  --restart unless-stopped \
  traefik:v3.0 \
  --providers.docker=true \
  --providers.docker.exposedbydefault=false \
  --entrypoints.web.address=:80 \
  --entrypoints.websecure.address=:443 \
  --certificatesresolvers.letsencrypt.acme.tlschallenge=true \
  --certificatesresolvers.letsencrypt.acme.email=your-email@example.com \
  --certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json
```

- Erstat `your-email@example.com` med din faktiske email adresse til Let's Encrypt notifications
- Denne kommando fortæller Traefik at:
  - Watch Docker for containers (via Docker socket mounted med `-v`)
  - Lytte på porte 80 og 443
  - Bruge TLS challenge til Let's Encrypt validation
  - Lagre certifikater i mounted volume

**Configuring Your Application Container:**
```bash
# Stop the existing container
docker stop ai-api
docker rm ai-api

# Start with Traefik labels
docker run -d \
  --name ai-api \
  --network traefik-network \
  --label "traefik.enable=true" \
  --label "traefik.http.routers.api.rule=Host(\`yourdomain.com\`)" \
  --label "traefik.http.routers.api.entrypoints=websecure" \
  --label "traefik.http.routers.api.tls=true" \
  --label "traefik.http.routers.api.tls.certresolver=letsencrypt" \
  --label "traefik.http.services.api.loadbalancer.server.port=8000" \
  --restart unless-stopped \
  my-ai-classifier:v1.0
```

**Notice:**
- Ingen `-p 8000:8000` port publishing (Traefik håndterer ekstern access)
- `--network traefik-network` forbinder til Traefik's network, dette er vigtigt for de to containers at tale sammen
- Den kritiske del er labels der konfigurerer routing og SSL
- Disse labels fortæller Traefik:
  - `traefik.enable=true`: Styr denne container
  - `traefik.http.routers.api.rule`: Route requests for `yourdomain.com` til denne container
  - `traefik.http.routers.api.entrypoints=websecure`: Brug HTTPS (port 443)
  - `traefik.http.routers.api.tls=true`: Enable TLS
  - `traefik.http.routers.api.tls.certresolver=letsencrypt`: Brug Let's Encrypt til certifikater
  - `traefik.http.services.api.loadbalancer.server.port=8000`: Forward til port 8000 inde i containeren

**HTTP to HTTPS Redirect:**
```bash
--label "traefik.http.routers.api-http.rule=Host(\`yourdomain.com\`)" \
--label "traefik.http.routers.api-http.entrypoints=web" \
--label "traefik.http.routers.api-http.middlewares=redirect-to-https" \
--label "traefik.http.middlewares.redirect-to-https.redirectscheme.scheme=https"
```

**How Automatic SSL Works:**
1. Traefik detekterer den nye container gennem Docker socket
2. Læser labels og opretter routing rules
3. Ser at TLS er enabled med Let's Encrypt resolver
4. Automatisk anmoder om et certifikat fra Let's Encrypt for `yourdomain.com`
5. Fuldfører TLS challenge (lignende til Certbot's HTTP challenge)
6. Installerer certifikatet
7. Begynder at route HTTPS trafik til din container

- Alt dette sker automatisk inden for sekunder af at starte din container
- Ingen manuelle Certbot kommandoer, ingen Nginx konfiguration redigering

**Automatic Renewal:**
- Traefik overvåger certifikat udløbsdatoer og fornyer dem automatisk før de udløber
- Du sætter ikke cron jobs eller systemd timers op; Traefik håndterer det internt

**Trade-offs:**
- **Fordele:** Fuldt automatisk SSL management, label-baseret konfiguration eliminerer separate konfigurationsfiler, native Docker integration
- **Ulemper:** Initial setup er mere kompleks end Nginx, kræver forståelse af Docker networks og labels, automation betyder mindre transparency
- For en enkelt container deployment som vores API server, kan Traefik være overkill
- Nginx og Certbot tilgangen lærer fundamentale koncepter og giver klar visibility i hvert step, gør det bedre til læring
- Traefik's værdi bliver tydelig når du styrer multiple services hvor dens automation betydeligt reducerer maintenance overhead

**Extended Reading:**
- Traefik v3 Docker Compose Guide
- Traefik TLS configuration
- DNS-Based Challenges for Fully Automatic SSL (Cloudflare, DuckDNS)

### Testing Your HTTPS Setup

**Access Your API via HTTPS:**
- Åbn din browser og naviger til `https://yourdomain.com`
- Bemærk du ikke behøver at specificere port 443 fordi det er default HTTPS port, ligesom port 80 er default for HTTP
- Du skulle se:
  1. Et padlock ikon i din browsers address bar
  2. Din API's response (sandsynligvis root endpoint besked)
  3. Ingen security advarsler
- Klik på padlock ikonet for at se certifikat detaljer
- Du skulle se certifikatet er udstedt af "Let's Encrypt" og er validt for dit domain

**Test HTTP to HTTPS Redirect:**
```bash
# Test with curl, following redirects
curl -L http://yourdomain.com
```

- Prøv at tilgå `http://yourdomain.com` (eksplicit ved brug af HTTP)
- Du skulle automatisk blive redirected til `https://yourdomain.com`
- Dette sikrer brugere altid bruger den krypterede forbindelse selv hvis de skriver eller bookmarker HTTP versionen
- `-L` flag fortæller curl at følge redirects
- Du skulle se din API's response

**Din API er nu production-ready med HTTPS!**
- Brugere kan tilgå den på `https://yourdomain.com` med fuld kryptering
- Certifikater vil fornye automatisk
- Din container fortsætter med at køre uændret på port 8000, komplet uvidende om HTTPS kompleksiteten der sker foran den

---

## 📋 Opsummering til Mini Projekt

### Vigtige Koncepter (Påkrævet):

1. **Cloud VM Setup** ✅ (Påkrævet)
   - Opret en VM på en cloud provider (fx AWS EC2)
   - Vælg appropriate OS (Ubuntu LTS anbefalet)
   - Konfigurer security groups/firewall rules
   - Sæt SSH keys op

2. **Docker Installation** ✅ (Påkrævet)
   - Installer Docker på VM'en
   - Verificer installation
   - Tilføj bruger til docker group

3. **Container Deployment** ✅ (Påkrævet)
   - Deploy din containerized API server
   - Test funktionalitet
   - Verificer at API er accessible

### Advanced Challenges (Optional):

4. **Domain og HTTPS** ⭐ (Optional men anbefalet)
   - Sæt et domain op (DuckDNS eller betalt)
   - Konfigurer DNS records
   - Sæt HTTPS op (Nginx + Certbot eller Traefik)
   - Test HTTPS funktionalitet

5. **Client Testing** ⭐ (Optional)
   - Interager med din API server ved brug af klientprogram kørende på en anden maskine (fx din personlige computer)
   - Test gennem HTTPS-enabled API endpoints

### Deployment Checklist:

**VM Setup:**
- [ ] VM oprettet på cloud provider
- [ ] Ubuntu LTS installeret
- [ ] Public IP adresse tildelt
- [ ] Security groups konfigureret (porte 22, 8000)
- [ ] SSH keys sat op

**Server Configuration:**
- [ ] System opdateret (`apt update && apt upgrade`)
- [ ] Firewall konfigureret (UFW)
- [ ] Docker installeret
- [ ] Docker installation verificeret
- [ ] User tilføjet til docker group

**Container Deployment:**
- [ ] Container image tilgængelig (pulled eller built)
- [ ] Container kørende med `--restart unless-stopped`
- [ ] Port mapping konfigureret
- [ ] Volume mounting sat op (hvis nødvendigt)
- [ ] Container logs tjekket
- [ ] API testet lokalt på serveren
- [ ] API testet fra ekstern maskine

**HTTPS Setup (Optional):**
- [ ] Domain navn oprettet
- [ ] DNS records konfigureret
- [ ] Nginx eller Traefik installeret
- [ ] SSL certifikat opnået
- [ ] HTTPS testet
- [ ] HTTP til HTTPS redirect testet

**Documentation:**
- [ ] Deployment process dokumenteret
- [ ] Server IP og domain dokumenteret
- [ ] Eventuelle issues eller limitations dokumenteret

---

## 🎯 Exercise: Deploy Your API Server Container on the Cloud

**Opgave:** Deploy containeren vi byggede i forrige modul på en cloud maskine for at frigøre computational ressourcer fra din personlige computer.

**Krav:**

1. **Connect til en cloud maskine:**
   - Vælg en cloud maskine af dit valg
   - Installer nødvendig container runtime (Docker)

2. **Deploy Container:**
   - Pull container image du pushed til container image registry, eller upload al source code og byg image'et på cloud maskinen direkte
   - Kør containeren og test dens funktionalitet

**Advanced Challenges (Optional):**

3. **Domain og HTTPS:**
   - Hvis din cloud maskine har en publicly accessible IP adresse, sæt et domain op der peger på din API server og enable HTTPS

4. **Client Testing:**
   - Interager med din API server ved brug af klientprogram kørende på en anden maskine (fx din personlige computer) gennem HTTPS-enabled API endpoints

---

## 🔗 Ressourcer

### Cloud Providers
- AWS: https://aws.amazon.com/
- Google Cloud: https://cloud.google.com/
- Microsoft Azure: https://azure.microsoft.com/
- Hetzner: https://www.hetzner.com/
- DigitalOcean: https://www.digitalocean.com/

### SSH
- SSH Documentation: https://www.openssh.com/
- SSH Key Generation: https://www.ssh.com/academy/ssh/keygen

### Docker
- Docker Installation: https://docs.docker.com/engine/install/ubuntu/
- Docker Documentation: https://docs.docker.com/

### Nginx
- Nginx Documentation: https://nginx.org/en/docs/
- Nginx Reverse Proxy: https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/

### SSL/TLS
- Let's Encrypt: https://letsencrypt.org/
- Certbot: https://certbot.eff.org/
- SSL Labs: https://www.ssllabs.com/ssltest/

### Traefik
- Traefik Documentation: https://doc.traefik.io/traefik/
- Traefik Docker Guide: https://doc.traefik.io/traefik/getting-started/install-traefik/

### Domain Registrars
- Cloudflare Registrar: https://www.cloudflare.com/products/registrar/
- DuckDNS: https://www.duckdns.org/
- Porkbun: https://porkbun.com/
- Namecheap: https://www.namecheap.com/

---

## 🎯 Konklusion

**Vigtige Takeaways:**

1. **Cloud Infrastructure:**
   - "Clouden" er computere i data centers du kan leje remote
   - Virtualization gør det praktisk
   - Tre lag: Physical, Virtualization, Management

2. **Cloud Providers:**
   - AWS, GCP, Azure er de store tre
   - Mange alternativer tilgængelige (Hetzner, DigitalOcean, etc.)
   - Vælg baseret på behov, budget, og expertise

3. **Cloud Services:**
   - VMs: Fuldt kontrol, forudsigelige omkostninger
   - Container Services: Automatisk scaling, usage-based pricing
   - GPU Instances: Til AI workloads, men dyre
   - Managed AI Services: Nemmest, men vendor lock-in

4. **Deployment Process:**
   - Opret VM
   - SSH access
   - Installer Docker
   - Deploy container
   - Test funktionalitet

5. **Production Considerations:**
   - Container persistence (`--restart unless-stopped`)
   - Basic monitoring
   - Backups
   - Maintenance procedures

6. **HTTPS:**
   - Påkrævet til production
   - Domain navn nødvendigt
   - SSL certifikater (Let's Encrypt gratis)
   - Reverse proxy (Nginx eller Traefik)

**For Mini Projekt:**
- Deploy på EC2 serveren (vi har allerede adgang!)
- Installer Docker (hvis ikke allerede installeret)
- Deploy containerized API server
- Test funktionalitet
- Overvej HTTPS setup (optional men anbefalet)

**Mål:**
- Din API server kører på clouden
- Accessible fra internettet
- Production-ready med HTTPS (hvis implementeret)
- Klar til at demonstrere i projektet!

