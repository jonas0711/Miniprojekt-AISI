# Modul 1: Interact with AI Systems - Opsummering

**Kursus:** AI Systems & Infrastructure  
**Formål:** Forstå standardiserede interaktioner mellem applikationer og avancerede API teknikker

---

## 📚 TL;DR

Lær hvorfor standardiserede interaktioner mellem applikationer er essentielle for at gøre AI modeller praktiske i virkelige scenarier. Gå fra simple funktionskald til robuste kommunikationsmetoder der virker på tværs af forskellige programmeringssprog og distributerede systemer.

---

## 🎯 Hovedbegreber

### Hvorfor Standardiserede Interaktioner?

**Problem:**
- AI modeller er ofte skrevet i Python, men ikke alle applikationer er
- Det er upraktisk at få software skrevet i Rust til at kalde en Python funktion
- Verdenen kan ikke være ét kæmpe Python projekt hvor applikationer kalder hinanden direkte

**Løsning:**
- Standardiserede og strømlinede metoder til at lade AI modeller interagere med omverdenen
- Fokus på eksisterende AI modeller/systemer og lokalt kørte AI modeller
- Deployment behandles i senere faser

---

## 🔧 Additional Fundamentals

### API Versioning

**Hvorfor?**
- APIs skal opdateres for at inkorporere nye features
- AI services introducerer konstant nye features og opdateringer til AI modeller
- Vi skal kunne introducere ændringer uden at bryde eksisterende interaktioner

**Strategier:**

1. **URL Path Versioning** (Mest almindelig)
   - Eksempel: `https://api.example.com/v1/generate` vs `https://api.example.com/v2/generate`
   - Brugt af OpenAI og Anthropic
   - Umiddelbart synlig og let at forstå

2. **Header-based Versioning**
   - URLs forbliver uændrede
   - Version specificeres via HTTP headers: `API-Version: 2.1` eller `Accept: application/vnd.api+json;version=2`
   - Mere fleksibel men mindre transparent

3. **Query Parameter Versioning**
   - Eksempel: `?version=1.2` eller `?api_version=latest`
   - Simpel at implementere, men kan gøre URLs rodede
   - Passer ikke godt med REST standarden

4. **Model-specific Versioning** (Særligt relevant for AI services)
   - Forskellige model versioner (fx `gpt-3.5-turbo` vs `gpt-4o`) repræsenterer forskellige capabilities
   - Specificeres typisk med en key i request body

### Rate Limiting

**Hvorfor?**
- Avancerede AI modeller er beregningsmæssigt dyre
- Uden proper limits kan få tunge brugere overvælde hele servicen
- Vigtigt når man skal skalere applikationer

**Typer af Rate Limiting:**

1. **Request-based:** X requests per minut/time
2. **Token-based:** Limit baseret på input/output tokens (almindeligt for conversational AI services)
3. **Concurrent requests:** Maksimalt antal samtidige forbindelser
4. **Resource-based:** GPU tid eller compute units (almindeligt for cloud computing services)

**Algoritmer:**

1. **Fixed Window:**
   - Fast limit inden for specifikke tidsrammer (fx 100 requests per minut, reset hvert minut)
   - Let at implementere, men kan forårsage trafik spikes ved window boundaries

2. **Sliding Window:**
   - Beregner kontinuerligt usage baseret på nylig aktivitet
   - Giver glattere request distribution og forhindrer burst abuse

3. **Token Bucket:**
   - Tillader requests kun når tokens er tilgængelige i en virtuel "bucket"
   - Tokens genopfyldes med en fast rate
   - Tillader korte bursts mens den opretholder overall rate control

---

## 🚀 Advanced API Protocols

### Streaming Protocols

**Problem:** Nogle gange har vi brug for kontinuerlige opdateringer i stedet for at vente på komplet response.

**Eksempel:** Når du sender en request til OpenAI/Anthropic's API, venter du et par sekunder for komplet response. Men i ChatGPT/Claude's officielle apps, streames responserne kontinuerligt ord-for-ord.

### Server-Sent Events (SSE)

**Hvad er det?**
- En client modtager en kontinuerlig stream af data fra en server
- Teknikken brugt af de fleste conversational AI services (chatbots) til at streame tekst ord-for-ord
- Letvægt og let at adoptere da det er baseret på HTTP protokollen
- **Kun unidirektional kommunikation** (server → client)

**Hvordan virker det?**
1. Receiver applikation åbner en forbindelse til sender applikation
2. Sender svarer og holder forbindelsen åben
3. Sender sender nye data gennem forbindelsen
4. Receiver modtager automatisk dataene

**Implementering i Python:**

```python
import os
import requests
import json

url = "https://api.anthropic.com/v1/messages"
headers = {
    "x-api-key": os.getenv("API_KEY"),
    "Content-Type": "application/json",
    "Accept": "text/event-stream",  # Accept SSE format
    "anthropic-version": "2023-06-01"
}

json_body = {
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 2048,
    "stream": True,  # Enable streaming
    "messages": [{"role": "user", "content": "Explain APIs."}]
}

response = requests.post(url, headers=headers, json=json_body, stream=True)

for line in response.iter_lines():
    if line:
        line = line.decode('utf-8')
        if line.startswith('data: '):
            data = line[6:]  # Remove 'data: ' prefix
            if data == '[DONE]':
                break
            try:
                event_data = json.loads(data)
                if 'delta' in event_data and 'text' in event_data['delta']:
                    print(event_data['delta']['text'], end='', flush=True)
            except json.JSONDecodeError:
                continue
```

**Nøgle forskelle fra regular POST:**
- `"stream": True` i request body
- `"Accept": "text/event-stream"` header
- `stream=True` parameter i `requests.post()`
- `response.iter_lines()` til at processe kontinuerlig stream
- Parse SSE format hvor hver chunk starter med `data:`

### WebSocket

**Hvad er det?**
- **Bidirektional streaming protokol** (til forskel fra SSE som kun er unidirektional)
- Eksempel: ChatGPT's voice mode hvor du kan tale med ChatGPT og afbryde det
- WebSocket er sin egen kommunikationsprotokol (ikke baseret på HTTP)

**Hvordan virker det?**
1. En applikation sender en standard HTTP request med upgrade headers
2. Den anden applikation accepterer upgrade og opretholder forbindelsen gennem WebSocket lifecycle

**Implementering i Python:**

```python
import os
import json
import websocket

OPENAI_API_KEY = os.getenv("API_KEY")
url = "wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-12-17"

headers = [
    "Authorization: Bearer " + OPENAI_API_KEY,
    "OpenAI-Beta: realtime=v1"
]

def on_open(ws):
    print("Connected to server.")
    payload = {
        "type": "response.create",
        "response": {
            "modalities": ["text"],
            "instructions": "Say hello!"
        }
    }
    ws.send(json.dumps(payload))

def on_message(ws, message):
    data = json.loads(message)
    print("Received event:", json.dumps(data, indent=2))

ws = websocket.WebSocketApp(url, header=headers, on_open=on_open, on_message=on_message)
ws.run_forever()
```

**WebRTC:**
- En anden real-time protokol der giver peer-to-peer forbindelser
- Bedre til streaming data mellem clients uden at stole på server arkitekturer
- Brugt i video calling og live streaming software

---

## 📨 Message-driven Protocols

**Problem:** Nogle gange skal data fra flere applikationer distribueres til flere andre applikationer. Direkte kommunikation mellem hver applikation ville være upraktisk.

**Eksempel:** Journalister producerer nyhedsbreve for en publisher, som så leverer dem til subscribers.

### MQTT (Message Queuing Telemetry Transport)

**Hvad er det?**
- Publish-subscribe message protokol
- Designet til resource-constrained devices (lav-power computere, smart home devices)
- Opererer på pub-sub pattern:
  - **Publishers** sender beskeder på specifikke topics uden at vide hvem der modtager dem
  - **Subscribers** udtrykker interesse ved at subscribe til specifikke topics
- Kræver **brokers** - devices/applikationer der modtager beskeder fra publishers og leverer dem til subscribers

**Anvendelser:**
- IoT (Internet of Things) kommunikation
- AI systemer hvor pub-sub pattern er nødvendigt

**Implementering i Python:**

```python
# publisher.py
import paho.mqtt.client as mqtt

broker = 'broker.hivemq.com'
port = 1883
topic = 'demo/ai-systems'

client = mqtt.Client()
client.connect(broker, port)
client.publish(topic, 'This is a very important message!')
client.disconnect()

# subscriber.py
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Received: {message.payload.decode()} on topic {message.topic}")

broker = 'broker.hivemq.com'
port = 1883
topic = 'demo/ai-systems'

client = mqtt.Client()
client.connect(broker, port)
client.subscribe(topic)
client.on_message = on_message
client.loop_forever()
```

### Apache Kafka

**Hvad er det?**
- Følger også pub-sub pattern
- Mere end en protokol - et omfattende computing system
- Kan håndtere store mængder beskeder med lav latency
- Brugt i mange large-scale IT infrastrukturer (Netflix, Uber)

**Arkitektur:**
- **Producers** (ligesom MQTT's publishers)
- **Consumers** (ligesom MQTT's subscribers)
- **Brokers**
- Bygget på clustering arkitektur for at undgå system overload

**Implementering i Python:**

```python
# producer.py
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=f"{os.getenv('KAFKA_ADDRESS')}:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(10):
    message = {'number': i, 'message': f'Hello Kafka! Message {i}'}
    producer.send('demo/ai-systems', value=message)
    time.sleep(1)

producer.flush()
producer.close()

# consumer.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'demo/ai-systems',
    bootstrap_servers=f"{os.getenv('KAFKA_ADDRESS')}:9092",
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='demo-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print(f'Consumed: {message.value}')
```

---

## 🤖 Model Context Protocol (MCP)

**Problem:**
- LLMs er meget afhængige af omfattende information og diverse handlinger de kan udføre
- Manuelt at feede information ind i conversation context og instruere LLMs er ikke automatisk eller reproducerbart
- Kan ikke skalere til production-level applikationer

**Løsning:**
- MCP introduceret af Anthropic i 2024
- Standard for conversational AI modeller til at integrere med eksterne informationskilder og tools
- Bygget på JSON-RPC 2.0
- Eliminerer behovet for custom integrationer mellem hvert AI system og ekstern service

**Arkitektur:**

1. **Hosts:**
   - AI applikationer brugere interagerer med direkte (fx Claude Code, IDEs)
   - Indeholder LLMs der har brug for adgang til eksterne capabilities

2. **Servers:**
   - Eksterne applikationer der eksponerer specifikke capabilities til AI modeller
   - Eksempler: database connectors, file system access tools, API integrationer med tredjepart services

3. **Clients:**
   - Lever inden for host applikationer
   - Styrer forbindelser mellem hosts og servers
   - Hver client opretholder dedikeret one-to-one forbindelse med specifik server

**Capabilities MCP servers kan levere:**

1. **Resources:**
   - Read-only data sources (ligesom HTTP GET endpoints)
   - Giver kontekstuel information uden signifikant computation eller side effects
   - Eksempel: file system resource der giver adgang til dokumentation

2. **Tools:**
   - Executable funktioner AI modeller kan kalde
   - Kan modificere state, performe computationer, eller interagere med eksterne services
   - Eksempel: sende emails, oprette calendar events, køre data analysis scripts

3. **Prompts:**
   - Pre-definerede templates der hjælper AI systemer med at bruge resources og tools mest effektivt
   - Giver strukturerede måder at accomplish common tasks
   - Kan deles på tværs af forskellige AI applikationer

**Kommunikationsmetoder:**

1. **stdio (Standard Input/Output):**
   - For lokale integrationer når clients og servers kører på samme maskine

2. **HTTP med SSE:**
   - For remote connections
   - Leverer samme SSE protokol vi har udforsket tidligere

**Ressourcer:**
- Specifikation: https://modelcontextprotocol.io/specification/
- Dokumentation: https://modelcontextprotocol.io/docs/
- Awesome MCP servers: https://github.com/punkpeye/awesome-mcp-servers

---

## ⚡ High-Performance Data Pipelines

**Problem:** I production miljøer kan protokoller alene være utilstrækkelige til at processe massive datasets, hvilket kan skabe bottlenecks i AI systemer.

**Løsning:** High-performance data pipelines der giver processing power nødvendig for large-scale data operationer.

### Apache Hadoop

**Hvad er det?**
- Framework til at lagre og processe store mængder data i et distribueret computing environment (clustering)
- Collection af open-source software med key idea om at udnytte clustering arkitektur

**To core layers:**

1. **HDFS (Hadoop Distributed File System):**
   - Arkitektur til at lagre store mængder data i et cluster
   - Bryder store filer i mindre blocks (typisk 128 MB eller 256 MB)
   - Lagrer dem på tværs af flere maskiner
   - Hver block replikeres flere gange (typisk 3) for fault tolerance

2. **MapReduce:**
   - Computation layer til effektivt at processe store mængder data i et cluster
   - Input data divideres i chunks og processeres i parallel
   - Hver worker processerer en chunk og producerer key-value pairs
   - Key-value pairs grupperes for at generere finale resultater

**Interaktion med Python:**
- Skriv MapReduce jobs

### Apache Spark

**Forskelle fra Hadoop:**
- Spark har ikke sin egen native file system
- Kan integreres med eksterne storage systemer (HDFS, databases)
- Storage efficiency opnås primært gennem at lagre intermediate data i memory i stedet for på disks (meget hurtigere)

**Arkitektur:**

1. **RDDs (Resilient Distributed Datasets):**
   - Immutable collections af data distribueret på tværs af et cluster af maskiner
   - Ligesom jobs tildelt hver medarbejder der ikke konflikter med hinanden

2. **DAG (Directed Acyclic Graph) Scheduler:**
   - Spark's hjerne til at finde ud af hvordan man computerer resultaterne
   - Ligesom et management team der finder ud af hvordan man splitter et stort projekt i flere jobs

**Interaktion med Python:**
- `pyspark` library

---

## 📋 Opsummering til Mini Projekt

### Vigtige Koncepter at Inkludere:

1. **API Versioning** ✅
   - Brug URL path versioning (fx `/v1/`, `/v2/`)
   - Dokumenter versioning strategi

2. **Rate Limiting** ✅
   - Implementer rate limiting for AI endpoints
   - Overvej token-based eller request-based limiting
   - Dokumenter strategi

3. **REST Principper** ✅
   - Design endpoints der følger REST
   - Proper HTTP metoder (GET, POST, PUT, DELETE)

4. **Streaming (Optional men anbefalet)** ⭐
   - Implementer SSE for streaming responses
   - Særligt relevant hvis du har conversational AI endpoints

5. **Error Handling** ✅
   - Proper error responses
   - Status codes

### Eksempel API Struktur:

```
/api/v1/
  ├── /models          # GET - List available models
  ├── /image_classify  # POST - Image classification
  ├── /conversation    # POST - LLM conversation (med streaming support)
  └── /health          # GET - Health check

/api/v2/
  └── /image_classify  # POST - Improved image classification
```

### Implementering Tips:

- Brug FastAPI (som vi har lært)
- Implementer versioning fra start
- Overvej rate limiting fra start
- Test streaming hvis relevant
- Dokumenter alle design valg

---

## 🔗 Ressourcer

- OpenAI Streaming: https://platform.openai.com/docs/api-reference/streaming
- Anthropic Streaming: https://docs.anthropic.com/claude/reference/messages-streaming
- MCP Spec: https://modelcontextprotocol.io/specification/
- MCP Docs: https://modelcontextprotocol.io/docs/

---

## ✅ Checklist til Mini Projekt

- [ ] API versioning implementeret (fx `/v1/`, `/v2/`)
- [ ] Rate limiting implementeret for AI endpoints
- [ ] REST principper følges
- [ ] Error handling og proper status codes
- [ ] Streaming support (hvis relevant)
- [ ] Dokumentation af design valg
- [ ] Test af alle endpoints

