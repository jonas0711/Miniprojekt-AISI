# Modul 4: AI Compute Hardware - Opsummering

**Kursus:** AI Systems & Infrastructure  
**Formål:** Forstå computer arkitektur, begrænsninger ved generisk hardware, og specialiseret hardware til AI computing

---

## 📚 TL;DR

Moderne "AI computere" er ikke fundamentalt forskellige: de bruger stadig den 80-årige Von Neumann arkitektur. Mens CPUs excellerer ved sekventiel processing, har AI workloads brug for massive parallel computation og høj memory bandwidth. Denne mismatch ledte til specialiseret hardware.

---

## 🎯 Hovedbegreber

### AI Computers - Hype eller Realitet?

**Vigtig Pointe:**
- De fleste "AI computere" er stadig baseret på Von Neumann arkitektur fra 1945
- 80 år senere bruger de fleste computere på Jorden stadig denne arkitektur
- Hardware capabilities er vokset drastisk, men grundlæggende arkitektur forbliver den samme

**Hvorfor det er vigtigt:**
- Capabilities af computer hardware er vokset hurtigt siden arkitekturen blev introduceret
- Dette er en af de vigtigste motivationer og fundamenter for udviklingen af AI modeller og systemer
- Vi skal starte fra basics og se på arkitekturen der startede det hele

---

## 🏗️ Computer Architecture

### Von Neumann Architecture (1945)

**Hvad er det?**
- Dokumenteret af John von Neumann i 1945
- Den mest indflydelsesrige computer arkitektur design i historien
- Etablerede fundamentet der stadig styrer de fleste computere i dag
- Fra smartphones til supercomputers

**Analog: Restaurant Kitchen**
- En travl restaurant køkken med ordrer og opskrifter (instructions) der kommer ind
- Ingredienser (data) klar til at blive kogt
- Kokke (CPU) følger ordrer og opskrifter og forbereder retter
- Pantry og counter (memory unit) til at lagre ingredienser og opskrifter
- Tjenere (input/output devices) bringer ordrer ind og leverer retter
- Korridorer (bus) forbinder alt personale og rum

### Komponenter i Von Neumann Architecture

#### 1. Instruction & Data

**Instructions (Opskrifter):**
- Fortæller computeren præcist hvilke operationer der skal udføres
- Ligesom opskrifter i en restaurant
- Step-by-step guide på hvordan man håndterer ingredienser og kogeredskaber

**Eksempel - Recipe:**
```
1. Cut onion into pieces
2. Heat up pan to medium heat
3. Add 2 tablespoons oil
4. Sauté onions until golden
```

**Eksempel - Computer Instructions:**
```
1. LOAD dkk_price
2. MULTIPLY dkk_price by conversion_factor
3. STORE result in usd_price
4. DISPLAY usd_price
```

**Data (Ingredienser):**
- Repræsenterer informationen der skal processeres
- Ligesom ingredienser i en restaurant

**Eksempel:**
```
- 2 large onions
- Olive oil
- dkk_price: 599
- conversion_factor: 0.1570
- usd_price: to be calculated
```

#### 2. Central Processing Unit (CPU)

**Hvad er det?**
- Hjernen af computeren
- Ligesom gruppen af kokke i restauranten
- Kan være sammensat af forskellige typer sub-units, især i moderne CPUs

**To essentielle typer:**

1. **Control Unit (CU) - Executive Chef:**
   - Læser ordrer og opskrifter
   - Forstår hvad der skal gøres for at opfylde ordrer
   - Koordinerer alt personale og udstyr til at udføre hvert step
   - **Specifikke opgaver:**
     - Henter næste instruction fra memory
     - Fortolker instruction's operation code og operands
     - Koordinerer execution ved at sende signals til andre komponenter

2. **Arithmetic Logic Unit (ALU) - Kokke der laver maden:**
   - Gør det faktiske arbejde (cooking)
   - Processerer ingredienser efter kommandoer fra CU
   - **Kan håndtere:**
     - Arithmetic (addition, subtraction, multiplication, division)
     - Logical (AND, OR, NOT, XOR)
     - Comparison (equals to, greater than, less than)
     - Bit manipulation (shifts, rotations, etc.)

#### 3. Memory

**Hvad er det?**
- Hvor både instructions og data lagres
- Ligesom en omfattende pantry hvor både ingredienser og opskriftbøger lagres
- Har et address system, lignende pantry der har et unified shelving system

**Karakteristika:**
- **Unified address space:** Både instructions og data bruger samme addressing scheme
- **Random access:** Enhver memory location kan tilgås direkte i konstant tid
- **Volatile storage:** Indhold går tabt når strømmen fjernes

#### 4. Input/Output (I/O)

**Hvad er det?**
- Håndterer kommunikation mellem computeren og den eksterne verden
- Ligesom tjenere i restauranten der bringer ordrer ind og leverer færdige retter

**Abstract Standpoint:**
- **I/O controllers:** Device management og protocol handling
- **I/O methods:** Forskellige typer interaktioner mellem I/O devices og computeren

**Physical Standpoint:**
- **Input devices:** Keyboard, mouse, trackpad, microphone, camera
- **Output devices:** Monitor, speaker, printer

#### 5. Bus

**Hvad er det?**
- Giver kommunikationsveje på tværs af alle komponenter i en computer
- Ligesom korridorer i køkkenet for personale at bevæge sig rundt, kommunikere, tilgå forskellige komponenter, og bære kogeredskaber, ingredienser og retter

**Tre sub-systemer:**

1. **Address Bus:**
   - Specificerer memory eller I/O device location der skal tilgås

2. **Data Bus:**
   - Bærer faktisk data transfereret mellem komponenter

3. **Control Bus:**
   - Bærer control signals og koordinerer forskellige komponenter

**Factorio Analogi:**
- For scalable production har du typisk også et bus system der forbinder storage boxes, I/O endpoints, og maskiner der producerer eller forbruger ting
- Sådant system gør det let at tilføje et nyt sub-system til eksisterende

### Von Neumann Architecture i Praksis

**Eksempel: Raspberry Pi 5**

**Komponenter:**
- **CPU:** BCM2712 processor (center-left på boardet)
  - Har multiple cores (flere kokke arbejder sammen)
- **Memory (RAM):** Positioneret meget tæt på CPU
  - For at sænke access latency
  - Ligesom at sætte counters tættere betyder hurtigere adgang til ting kokke har brug for
- **I/O Interfaces:**
  - PCI Express interface for high-speed peripherals
  - Ethernet og USB connectors
  - MIPI DSI/CSI connectors til kameraer
  - Raspberry Pi RP1 I/O controller håndterer forbindelser
- **Bus System:**
  - Traces overalt på boardet
  - Fysisk implementering af bus systemet
  - Essentielt kobbertråde der forbinder alle komponenter sammen

---

## ⚠️ Limitations of Generic Hardware

### Problem: CPU vs AI Workloads

**To hovedproblemer:**

#### 1. Sequential Processing vs. Parallel Demands

**CPUs:**
- Excellerer ved **sequential processing**
- Kan udføre komplekse instructions en efter en
- **Analog:** Universitetsprofessor der kan løse komplekse matematikproblemer
- Kan løse ethvert kendt problem, men kun ét problem ad gangen
- Moderne CPUs har typisk **8 cores** (consumer tier) eller **64 cores** (professional server tier)

**AI Models:**
- Tungt afhængige af **matrix-related computation**
- Matrix manipulation udgør **45-60% af runtime** i Transformer modeller (store sprogmodeller)
- Manipulationer involverer typisk relativt simple instructions (add, multiply)
- Men hver manipulation inkluderer **tusindvis af uafhængige beregninger** der kunne ske i parallel
- **Analog:** Giv en professor tusind simple ligninger at løse
  - Hver ligning er meget simpel for professoren
  - Men vil stadig tage meget tid at løse dem alle
  - En gruppe (hundreder) af folkeskoleelever, selvom hver er inkompetent til at løse komplekse ligninger, vil sandsynligvis være hurtigere til at håndtere disse tusind ligninger

#### 2. Memory Bus Bottleneck

**CPU Memory Bus:**
- Designet til at være **low latency**
- CPUs er typisk ansvarlige for at udføre komplekse instructions der involverer fetching og storing data spredt i forskellige lokationer i memory
- **Latency er vigtigere** for CPUs

**AI Models:**
- Tungt afhængige af **large-scale parallel instructions** på matricer
- Matricer er typisk lagret i en relativt lokal blok i memory
- **Low latency memory bus' fordel bliver ulempe her**
- Low latency memory bus kommer typisk med ulempen af **low bandwidth**
- **Bandwidth er mere kritisk** for de fleste AI modeller
- Evnen til at flytte en stor chunk af data hurtigt er en mere kritisk metrik

**Konklusion:**
- Fundamentalt mismatch mellem CPU arkitektur og AI workload
- Kalder på specialiseret hardware til at speede op AI computing
- Vi har brug for hardware der excellerer i parallel processing og har high-bandwidth memory

---

## 🚀 Specialized Hardware

### Graphics Processing Unit (GPU)

**Oprindelse:**
- Oprindeligt designet til at processere computer graphics
- Oprindeligt designet i 1980'erne til at accelerere 3D graphics rendering for videospil
- Rendering af 3D videospil involverer beregning af lighting, shading, og texture mapping
- Viser millioner af pixels med højt optimerede algoritmer der bryder sådanne beregninger i små units
- Units er sammensat af simple instructions og kan gøres i parallel

**Design:**
- Excellerer ved **parallel processing**
- **Moderne CPU:** Mindre end 100 kraftfulde cores
- **Moderne GPU:** Tusindvis af svage cores
- Hver core kan kun håndtere simple instructions—ligesom en folkeskoleelev
- Men alle cores kombineret kan færdiggøre en paralleliseret opgave meget hurtigere end en CPU

**Memory:**
- Designet omkring **high-bandwidth**
- Store chunks af data kan tilgås hurtigt
- **DDR memory (CPUs):** ~50-100 GB/s bandwidth
- **GDDR memory (GPUs):** Op til **1.5 TB/s bandwidth**
- **HBM memory (AI workloads):** Op til **2 TB/s bandwidth**

**AI Computing:**
- Behovet for parallel processing og high-bandwidth af computer graphics aligner godt med AI computing
- GPU er blevet den dominerende type specialiseret hardware for AI workloads i de seneste år
- Desværre betyder dette at store GPU brands ikke længere giver en skid for gamere og generelle forbrugere

### Tensor Processing Unit (TPU)

**Hvad er det?**
- Google's TPU (Tensor Processing Unit)
- Hardware specifikt designet til AI computing
- Introduceret som AI industrien vokser hurtigt

**Arkitektur:**
- Tusindvis af simple processor cores aligned i et grid
- Indkommende data og instructions flyder gennem gridet som bølger
- Hver processor core laver en lille beregning og passerer resultatet til sine naboer

**Fordele:**
- Højt specialiseret i AI computing
- Kan være mere effektiv for AI workloads sammenlignet med GPU
- GPU skal stadig håndtere graphics og andre generelle computing tasks

**Ulemper:**
- Upraktisk for alle andre opgaver
- Nu om dage primært set i data centers, især dem bygget af Google selv

### Neural Processing Unit (NPU)

**Hvad er det?**
- Specialiseret AI computing hardware i personlige computing devices (PCs, smartphones)
- Fokuserer på **power efficiency**
- Mål: Levere AI computing acceleration mens den forbruger minimal power og fysisk plads

**Karakteristika:**
- **Miniaturisering:**
  - Fokuserer på at køre pre-trained modeller i stedet for at træne nye
  - Bruger typisk low-precision arithmetic (8-bit eller endda 4-bit) sammenlignet med fuld 32-bit
- **Forskellige designs:**
  - **Apple:** Neural Engine (integreret i smartphone chips fra iPhone 8)
  - **Qualcomm:** AI Engine (arbejder samarbejdende med GPUs i deres chips)

**Moderne Eksempler:**
- Apple's M4 desktop chip
- AMD's Ryzen AI series laptop chip
- Qualcomm's Snapdragon X Elite laptop chip

---

## 🔄 Return to Von Neumann Architecture

**Vigtig Pointe:**
- På trods af al den hypede specialiserede hardware til AI computing, adherer de fleste moderne computere stadig fundamentalt til Von Neumann arkitekturen på system niveau
- Uanset om GPUs, TPUs, eller NPUs er integreret i computere, vil denne hardware stadig:
  - Forbinde til CPUs via bus systemet
  - Dele unified memory address space
  - Blive ultimate managed og koordineret af CPUs

**Analog:**
- CPU forbliver "executive chef" der koordinerer systemet
- Specialiserede processorer fungerer som højt kvalificerede sous chefs der håndterer specifikke opgaver

**Von Neumann Architecture's Geni:**
- Ligger ikke i specifikke komponenter, men i dens **modulære design**
- Fortsætter med at accommodate nye typer processing units som computational needs udvikler sig
- **Factorio analogi:** Mens nye assembly lines måske skal bygges til at producere nye typer produkter introduceret af opdateringer til spillet, vil bus systemet forblive den gyldne standard arkitektur hvis du vil have din fabrik til at være scalable og produktiv

---

## 📋 Opsummering til Mini Projekt

### Vigtige Koncepter at Overveje:

1. **Hardware Valg** ✅
   - Overvej hvilken hardware din AI model kræver
   - CPU: Til simple modeller eller development
   - GPU: Til større modeller der kræver parallel processing
   - NPU: Hvis du deployer på edge devices

2. **Memory Requirements** ✅
   - Overvej hvor meget memory din model kræver
   - GPU memory er typisk begrænset sammenlignet med system memory
   - Overvej model størrelse og batch size

3. **Performance Optimization** ⭐
   - Overvej at bruge GPU hvis tilgængelig
   - Test performance på forskellige hardware typer
   - Dokumenter performance forskelle

4. **Deployment Considerations** ✅
   - EC2 serveren har muligvis ikke dedikeret GPU
   - CPU-baseret inference kan være langsommere
   - Overvej model størrelse og kompleksitet

### Hardware til EC2 Server:

**Hvad vi har:**
- EC2 serveren har sandsynligvis standard CPU (ingen dedikeret GPU)
- Python 3.12.3 og Docker installeret
- Nok memory til mindre modeller

**Anbefalinger:**
- Brug lightweight modeller der kan køre på CPU
- Overvej at bruge HuggingFace modeller der er optimeret til CPU
- Test model performance før deployment
- Dokumenter hardware limitations i rapporten

### Model Selection Tips:

1. **Lightweight Models:**
   - Brug mindre modeller (fx ResNet-18 i stedet for ResNet-152)
   - Overvej quantized modeller (8-bit, 4-bit)
   - Test model størrelse og inference tid

2. **CPU-Optimized Models:**
   - Nogle modeller er bedre optimeret til CPU
   - HuggingFace har mange CPU-friendly modeller
   - Overvej ONNX runtime for bedre CPU performance

3. **Memory Management:**
   - Monitor memory usage
   - Overvej batch size
   - Implementer proper cleanup

---

## 🧪 Exercise: Google Colab Hardware Testing

**Opgave:** Kør en AI model på forskellige typer hardware leveret af Google Colab.

**Steps:**

1. **Spin up Google Colab:**
   - Interactive playground (essentielt Jupyter Notebook)
   - Kør Python kode med forskellige typer hardware (CPU, GPU, TPU)
   - Nok gratis computing timer til at lege med

2. **Test AI Model:**
   - Kør image analysis modellen vi brugte i "Wrap AI Models with APIs"
   - Beregn den teoretiske størrelse af modellen (hint: kan opnås ved at beregne antallet af parametre i modellen)

3. **Test Forskellige Hardware:**
   - Skift runtime til forskellige typer hardware (CPU, GPU, TPU)
   - Genkør modellen på hver type

4. **Record og Sammenlign:**
   - Optegn tiden modellen har brug for at processe ét billede
   - Sammenlign tiden på tværs af forskellige typer hardware
   - Dokumenter resultaterne

**Forventede Resultater:**
- GPU vil typisk være hurtigere end CPU
- TPU kan være hurtigere end GPU for specifikke workloads
- CPU vil være langsommest men mest tilgængelig

---

## ✅ Checklist til Mini Projekt

### Hardware Considerations
- [ ] Hardware valgt (CPU/GPU/NPU)
- [ ] Model størrelse evalueret
- [ ] Memory requirements verificeret
- [ ] Performance testet på target hardware
- [ ] Limitations dokumenteret

### Model Selection
- [ ] Lightweight model valgt (hvis CPU)
- [ ] Model optimeret til target hardware
- [ ] Model størrelse og parametre dokumenteret
- [ ] Inference tid målt og dokumenteret

### Deployment
- [ ] Model kan køre på EC2 serveren
- [ ] Memory usage overvåget
- [ ] Performance acceptable
- [ ] Hardware limitations forklaret i rapporten

---

## 🔗 Ressourcer

### Von Neumann Architecture
- Von Neumann Architecture: https://en.wikipedia.org/wiki/Von_Neumann_architecture
- Computer Architecture Basics: https://www.tutorialspoint.com/computer_fundamentals/computer_architecture.htm

### GPU Computing
- NVIDIA CUDA: https://developer.nvidia.com/cuda-toolkit
- GPU vs CPU: https://www.nvidia.com/en-us/data-center/gpu-accelerated-applications/

### TPU
- Google TPU: https://cloud.google.com/tpu/docs
- TPU vs GPU: https://cloud.google.com/tpu/docs/tpus

### NPU
- Apple Neural Engine: https://www.apple.com/machine-learning/
- Qualcomm AI Engine: https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-ai-engine

### Model Optimization
- HuggingFace Models: https://huggingface.co/models
- ONNX Runtime: https://onnxruntime.ai/
- Model Quantization: https://huggingface.co/docs/transformers/quantization

### Google Colab
- Google Colab: https://colab.research.google.com/
- Colab GPU/TPU: https://colab.research.google.com/notebooks/gpu.ipynb

---

## 🎯 Konklusion

**Vigtige Takeaways:**

1. **Von Neumann Architecture:**
   - Størstedelen af computere bruger stadig denne 80-årige arkitektur
   - Modulært design gør det muligt at tilføje nye processing units

2. **CPU Limitations:**
   - Excellerer ved sequential processing
   - Ikke ideel til massive parallel computation
   - Memory bus bottleneck for AI workloads

3. **Specialized Hardware:**
   - **GPU:** Parallel processing, high-bandwidth memory
   - **TPU:** Højt specialiseret til AI, primært i data centers
   - **NPU:** Power-efficient, til edge devices

4. **For Mini Projekt:**
   - Overvej hardware limitations
   - Vælg appropriate modeller
   - Test performance
   - Dokumenter hardware valg og begrænsninger

