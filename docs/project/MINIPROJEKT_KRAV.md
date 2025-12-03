# Mini Project - Krav og Specifikationer

**Kursus:** AI Systems & Infrastructure  
**Deadline:** 4. december 2025 kl. 23:59 (Copenhagen time)  
**Format:** 3-4 sider rapport (ekskl. referencer) + kildekode

---

## 🎯 Outcome (Mål)

Projektet skal resultere i:
- **En AI API server** (ligesom den fra modul 3) deployet på en anden maskine end din personlige PC
- **Et klientprogram** der kan interagere med serveren

---

## ✅ Nødvendige Krav

### 1. API Server Implementation

#### Flere Routes/Endpoints
- Serveren skal have **mere end én route** (API endpoint)
- **Mindst én route skal have "AI funktionalitet"** (billede eller sprog-relateret)

**Eksempler på routes:**
- `<domain>/v1/image_classify` (billedklassificering) + `<domain>/v1/conversation` (LLM samtale)
- Flere versioner: `<domain>/v1/image_classify` og `<domain>/v2/image_classify` med forskellig funktionalitet
- Utility routes: `<domain>/v1/model` (liste tilgængelige AI modeller)

#### Framework
- **FastAPI** (anbefalet, da det er det vi har lært)
- **Alternativer tilladt:** Flask, Django, eller andre sprog end Python

#### AI Modeller
- Kan bruge off-the-shelf modeller fra **HuggingFace**
- Modeller fra andre kurser
- Modeller fra andre kilder
- **Fokus er IKKE på modellen**, men på API og deployment

#### Kodekvalitet
- **FRIHED til at bruge biblioteker, AI hjælp, eller reference kode**
- **MÅ IKKE** kopiere og indsætte kode uden modifikation
- **SKAL forstå** implementeringen - især hvis koden kommer fra andre eller AI
- Gennemsigtig genbrug er OK, men forståelse er påkrævet

---

### 2. Deployment af API Serveren

#### Forskellige Host Environments
- Serveren og klienten skal køre på **forskellige host environments**
- **IKKE på samme maskine** (medmindre det er forskellige virtuelle maskiner)

**Acceptable eksempler:**
- Server på din PC, klient på kollegas PC
- Server på én PC, klient på anden PC
- Server på Raspberry Pi/Jetson, klient på PC (eller omvendt)
- Server på cloud computer, klient på PC (eller omvendt)
- Server og klient på samme fysiske maskine, men i forskellige virtuelle maskiner

#### Containerization
- **Serveren SKAL deployes med containerization** (modul 5)
- **Docker** (anbefalet) eller alternativer som Podman
- **MÅ IKKE** køre serveren direkte på host environment
- Skal køre i en container

---

### 3. Klient Program

#### Krav
- **Ingen strikte krav** til klientprogrammet
- Skal kunne **demonstrere serverens funktionalitet**
- Skal kunne **interagere med serveren** og validere at den virker korrekt

---

## 💡 Tips (Ikke Strikte Krav)

Disse aspekter bør overvejes for at demonstrere forståelse:

1. **REST principper** - API endpoints design der følger REST
2. **API versioning** - Overvej versionering, selv hvis du kun har v1 endpoints
3. **Database integration** - Integration med database til API key management
4. **Dedikeret AI hardware** - Udnyt dedikeret AI computing hardware hvis maskinen har det
5. **Dockerfile layering** - Byg server container image med Dockerfile og proper layering

---

## 🚀 Optional Achievements

For dem der synes kravene er for nemme:

1. **Rate limiting** - Record per user usage og implementer avanceret rate limit algoritme for AI endpoints
2. **High availability** - Gør serveren højtilgængelig (fx kør på cluster) eller implementer avancerede deployment strategier
3. **Public access** - Gør serveren offentligt tilgængelig med:
   - Offentlig IP adresse
   - Domain navn
   - SSL certifikat
4. **OpenAI/Anthropic replacement** - Gør API serveren en drop-in replacement ved at implementere multi-modal conversational APIs (modtager både sprog og billede input, genererer sprog output)

**Note:** Disse giver ikke automatisk højere score - projektet vurderes på forståelse, ikke kompleksitet.

---

## 📄 Rapport Krav

**Længde:** 3-4 sider (ekskl. referencer)

**Indhold:**
1. **Title og alle forfattere**
2. **Introduction** - Kort problem analyse
3. **Implementation** - Forklar vigtige design og implementation valg for:
   - API serveren
   - Klientprogrammet
4. **Deployment** - Demonstrer vigtige steps i deployment af API serveren
5. **Results** - Evaluering af API serverens funktionalitet og reflektioner
6. **Conclusion**

---

## 📦 Submission

**Format:** Én `.zip` eller `.tar.gz` fil (eller andet åbent format)

**Indhold:**
1. **Rapport i PDF format**
2. **Alle kildekoder nødvendige til at bygge API server containeren:**
   - API server kildekode
   - Dockerfile
   - requirements.txt (eller lignende)
   - Andre nødvendige filer
3. **Kildekode til klientprogrammet**

**Deadline:** 4. december 2025 kl. 23:59 (Copenhagen time)  
**Upload:** DigitalExam (én submission per gruppe)

**Vigtigt:** Tidsmæssig indlevering er forudsætning for at deltage i eksamen.

---

## 🎓 Eksamen

### Format
- **Individual oral exam** baseret på indsendt projekt
- **Varighed:** 15 minutter + 5 minutter overvejelse

### Agenda
1. **5-minutters præsentation** af det færdige miniprojekt (studerende)
2. **Vælg et emne** fra 5 tilgængelige emner og forklar grundlæggende koncepter
3. **Opfølgende spørgsmål** fra eksaminator og censor

### Emner (5 tilgængelige)
1. Interacting with & building APIs
2. Computing architecture & hardware
3. Containerization
4. Deployment on diverse infrastructures
5. High availability & advanced deployment strategies

### Vurdering
- **IKKE påkrævet** at skrive kode
- **IKKE påkrævet** at huske specifikke kommandoer eller kode syntaks
- **MÅ blive bedt om** at tegne diagrammer eller løse små opgaver manuelt
- **7-point skala** baseret på samlet vurdering af miniprojekt og mundtlig præstation

---

## 📋 Checklist

### API Server
- [ ] Mere end én route/endpoint
- [ ] Mindst én route med AI funktionalitet
- [ ] FastAPI eller andet framework
- [ ] AI model integreret
- [ ] Forståelse af koden

### Deployment
- [ ] Server kører i container (Docker/Podman)
- [ ] Server og klient på forskellige host environments
- [ ] Dockerfile med proper layering
- [ ] Server deployet og kører

### Klient
- [ ] Klientprogram der kan interagere med serveren
- [ ] Demonstrerer serverens funktionalitet

### Tips (Anbefalet)
- [ ] REST principper følges
- [ ] API versioning overvejet
- [ ] Database til API key management
- [ ] Dedikeret AI hardware udnyttet (hvis tilgængelig)

### Rapport
- [ ] 3-4 sider (ekskl. referencer)
- [ ] Title og forfattere
- [ ] Introduction
- [ ] Implementation
- [ ] Deployment
- [ ] Results
- [ ] Conclusion

### Submission
- [ ] Rapport i PDF
- [ ] Alle kildekoder til server
- [ ] Dockerfile
- [ ] requirements.txt
- [ ] Klientprogram kildekode
- [ ] Pakket i .zip eller .tar.gz
- [ ] Uploadet til DigitalExam før deadline

---

## 🎯 Næste Skridt

1. Planlæg API serverens routes og funktionalitet
2. Vælg AI model(ler) til brug
3. Implementer API serveren
4. Opret Dockerfile og container setup
5. Deploy serveren på EC2 (eller anden maskine)
6. Implementer klientprogrammet
7. Test hele systemet
8. Skriv rapport
9. Pak og indsend

