r Er # Implementation Sektion - Rapport

**Forfatter:** Jonas  
**Dato:** 3. december 2025

---

## API Server Implementation

### FastAPI Framework Valg

Vi valgte FastAPI som framework til API serveren, da det er anbefalet i undervisningsmaterialet (Modul 3) og giver god performance med async support. FastAPI giver også automatisk API dokumentation og type validation gennem Pydantic.

### CIFAR-10 Model Valg og Implementation

Vi implementerede CIFAR-10 image classification ved hjælp af ResNet-18 arkitektur modificeret til 10 output klasser. CIFAR-10 er et standard dataset med 10 kategorier: airplane, car, bird, cat, deer, dog, frog, horse, ship, og truck.

**Model Implementation:**
- Brugte `torchvision.models.resnet18` som base arkitektur
- Modificerede sidste layer fra 1000 klasser (ImageNet) til 10 klasser (CIFAR-10)
- Model loader ved server startup gennem lifespan context manager
- Billeder preprocesses til 32x32 RGB format (CIFAR-10 standard)

**Hvorfor ResNet-18:**
- Simpel og effektiv arkitektur
- Kan køre på CPU (perfekt til EC2 serveren uden GPU)
- Let at modificere til CIFAR-10's 10 klasser

### API Routes Implementation

Vi implementerede 4 endpoints:

1. **GET `/`** - Root endpoint der returnerer velkomstbesked og liste af endpoints
2. **GET `/health`** - Health check endpoint der tjekker om serveren og modellen kører korrekt
3. **GET `/model/info`** - Returnerer information om CIFAR-10 modellen (navn, status, antal klasser)
4. **POST `/image_classify`** - Hovedendpoint med AI funktionalitet der klassificerer billeder

**Image Classification Endpoint:**
- Modtager base64 encoded image i JSON request body
- Dekoder base64 til PIL Image
- Preprocesser billede til 32x32 RGB format
- Kører inference gennem CIFAR-10 modellen
- Returnerer top 5 predictions med confidence scores

**Data Models:**
- Brugte Pydantic BaseModel til request/response validation
- `ImageRequest`: Validerer base64 image string
- `ClassificationResponse`: Struktureret response med predictions
- `ModelInfo`: Model information response

### Async Implementation

Vi brugte async/await pattern som demonstreret i Modul 3:
- `ImageClassifier` class med async `load_model()` og `classify_image()` metoder
- Lifespan context manager til at loade modellen ved server startup
- Sikrer at serveren kan håndtere multiple requests samtidigt

---

## Klientprogram Implementation

### Design Valg

Klientprogrammet er implementeret som et simpelt Python script der bruger `requests` library, som demonstreret i Modul 1 & 2. Dette gør det nemt at teste API'en fra lokal maskine.

### Funktionalitet

Klientprogrammet implementerer 3 funktioner:

1. **`check_health()`** - Tester GET `/health` endpoint
   - Verificerer at serveren kører
   - Tjekker model status
   - Returnerer True/False baseret på response

2. **`get_model_info()`** - Tester GET `/model/info` endpoint
   - Henter model information
   - Viser model navn, status og antal klasser

3. **`classify_image()`** - Tester POST `/image_classify` endpoint
   - Encoder billede til base64
   - Sender POST request med JSON body
   - Viser top predictions med confidence scores

### Base64 Image Encoding

Billeder encodes til base64 string for at kunne sendes gennem JSON, som demonstreret i Modul 3. Dette gør det muligt at sende billeder gennem standard HTTP POST requests.

### Error Handling

Klientprogrammet implementerer proper error handling:
- Try/except blocks omkring alle API kald
- Viser informative fejlbeskeder
- Tjekker response status codes
- Håndterer connection errors gracefully

---

## Design Beslutninger

### Simplicitet

Vi valgte at holde implementationen så simpel som muligt, som anbefalet i undervisningsmaterialet. Dette gør koden:
- Let at forstå
- Let at vedligeholde
- Let at debugge

### Følger Undervisningsmaterialet

Alle design valg følger eksempler fra modulerne:
- FastAPI struktur fra Modul 3
- Async pattern fra Modul 3
- Requests library fra Modul 1 & 2
- Base64 encoding fra Modul 3
- Pydantic models fra Modul 3

### Debug Logging

Vi tilføjede print statements til debugging, som anbefalet i reglerne. Dette gør det let at følge program flow og identificere problemer.

---

**Note:** Denne sektion skal inkluderes i den endelige rapport (3-4 sider).

