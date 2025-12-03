# Modul 2: Advanced APIs in the Era of AI - Opsummering

**Kursus:** AI Systems & Infrastructure  
**Formål:** Lær avancerede API patterns og teknikker der gør high-performance, real-time, og message-driven kommunikation mulig for moderne AI systemer

---

## 📚 TL;DR

Avancerede API patterns og teknikker muliggør high-performance, real-time, og message-driven kommunikation essentiel for moderne AI systemer—ligesom subscription services der leverer kontinuerlige opdateringer i stedet for at kræve individuelle requests.

---

## 🎯 Hovedbegreber

### Problem med Simple Request-Response

**Eksempel:**
- At sende et brev og vente på svar virker for lejlighedsvis kommunikation
- Men bliver upraktisk når du har brug for kontinuerlige opdateringer
- Ligesom at sende timevis request breve til en vejrservice i stedet for at modtage automatiske daglige forecasts

**Real-world Eksempel:**
- Når du sender en request til OpenAI/Anthropic's API, venter du et par sekunder for komplet response
- Men i ChatGPT/Claude's officielle apps, streames responserne kontinuerligt ord-for-ord
- Denne streaming behavior er også opnåelig gennem APIs!

---

## 🔧 Additional Fundamentals

### API Versioning

**Hvorfor?**
- APIs skal opdateres for at inkorporere nye features eller lave ændringer
- Særligt for AI services hvor nye features og opdateringer til AI modeller konstant introduceres
- Vi skal kunne introducere ændringer uden at bryde eksisterende interaktioner

**Definition:**
API versioning er praksis med at håndtere forskellige iterationer af APIs, hvilket tillader providers at introducere ændringer og nye features uden at bryde eksisterende interaktioner. Tænk på det som at opretholde backward compatibility—gamle systemer fortsætter med at virke mens nye features bliver tilgængelige i nyere versioner.

**Strategier:**

1. **URL Path Versioning** (Mest almindelig og anbefalet)
   - Embedder version information direkte i endpoint URL
   - Eksempel: `https://api.example.com/v1/generate` vs `https://api.example.com/v2/generate`
   - Brugt af både OpenAI og Anthropic
   - Umiddelbart synlig og let at forstå

2. **Header-based Versioning**
   - URLs forbliver uændrede
   - Version specificeres via HTTP headers:
     - `API-Version: 2.1`
     - `Accept: application/vnd.api+json;version=2`
   - Mere fleksibel men mindre transparent

3. **Query Parameter Versioning**
   - URL parametre som `?version=1.2` eller `?api_version=latest`
   - Simpel at implementere, men kan gøre URLs rodede
   - Passer ikke godt med REST standarden

4. **Model-specific Versioning** (Særligt relevant for AI services)
   - Forskellige model versioner (fx `gpt-3.5-turbo` vs `gpt-4o`) repræsenterer distinkte capabilities
   - Specificeres typisk med en key i request body

### Rate Limiting

**Hvorfor?**
- Avancerede AI modeller er beregningsmæssigt dyre
- Uden proper limits kan få tunge brugere overvælde hele servicen
- Vigtigt når man skal skalere applikationer
- Du har måske ikke mødt rate limiting i praksis da usage costs typisk rammer budget limits først

**Definition:**
Rate limiting er en strategi implementeret af API providers til at kontrollere antallet af requests processeret inden for en given tidsramme.

**Typer af Rate Limiting:**

1. **Request-based:**
   - X requests per minut/time
   - Almindeligt for mange APIs

2. **Token-based:**
   - Limit baseret på input/output tokens
   - Almindeligt for conversational AI services hvor processing power er direkte relateret til antallet af tokens brugt

3. **Concurrent requests:**
   - Maksimalt antal samtidige forbindelser
   - Oftere set i data storage services

4. **Resource-based:**
   - GPU tid eller compute units
   - Almindeligt for cloud computing services

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

**Reference:**
- OpenAI rate limiting: https://platform.openai.com/docs/guides/rate-limits
- Anthropic rate limiting: https://docs.anthropic.com/claude/reference/rate-limits

---

## 🚀 Advanced API Protocols

### Streaming Protocols

**Hvorfor?**
- Word-by-word streaming er opnåelig gennem APIs ved brug af streaming protokoller
- Widely supported i conversational AI APIs
- De fleste AI modeller til conversation er baseret på next token prediction (NTP) arkitektur
- Passer den naturlige måde mennesker læser tekst

**To prominente streaming protokoller:**
1. Server-Sent Events (SSE)
2. WebSocket

### Server-Sent Events (SSE)

**Hvad er det?**
- En client modtager en kontinuerlig stream af data fra en server
- Teknikken brugt af de fleste conversational AI services (chatbots) til at streame tekst ord-for-ord til brugere
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
    "User-Agent": "SomeAIApp/1.0",
    "anthropic-version": "2023-06-01"
}

json_body = {
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 2048,
    "temperature": 0.7,
    "stream": True,  # Enable streaming
    "messages": [
        {
            "role": "user",
            "content": "Explain the concept of APIs."
        }
    ]
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=json_body,
        timeout=30,
        stream=True  # Enable streaming in requests
    )
    
    response.raise_for_status()
    print("Streaming response:")
    
    for line in response.iter_lines():
        if line:
            line = line.decode('utf-8')
            if line.startswith('data: '):
                data = line[6:]  # Remove 'data: ' prefix
                if data == '[DONE]':
                    break
                try:
                    event_data = json.loads(data)
                    # Extract and print the content delta
                    if 'delta' in event_data and 'text' in event_data['delta']:
                        print(event_data['delta']['text'], end='', flush=True)
                except json.JSONDecodeError:
                    continue
    
    print("\nStreaming complete!")
    
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

**Nøgle forskelle fra regular POST:**
- `"stream": True` i request body for at enable streaming
- `"Accept": "text/event-stream"` header for at specificere SSE format
- `stream=True` parameter i `requests.post()` for at håndtere streaming responses
- `response.iter_lines()` for at processe kontinuerlig stream af data
- Parse SSE format hvor hver chunk starter med `data:`

**Extended Reading:**
- OpenAI streaming: https://platform.openai.com/docs/api-reference/streaming
- Anthropic streaming: https://docs.anthropic.com/claude/reference/messages-streaming

### WebSocket

**Hvad er det?**
- **Bidirektional streaming protokol** (til forskel fra SSE som kun er unidirektional)
- Eksempel: ChatGPT's voice mode hvor du kan tale med ChatGPT og afbryde det, ligesom at ringe til nogen i virkeligheden
- Dette er uopnåeligt med unidirektionale protokoller som SSE

**Forskelle fra SSE:**
- SSE er bygget på toppen af HTTP
- WebSocket er sin egen kommunikationsprotokol
- For to applikationer at etablere en WebSocket forbindelse:
  1. En applikation sender først en standard HTTP request med upgrade headers
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
    # Send a request to the API when the connection opens
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

ws = websocket.WebSocketApp(
    url,
    header=headers,
    on_open=on_open,
    on_message=on_message
)

ws.run_forever()
```

**Note:**
- Vi kan ikke længere bruge `requests` package da den er specifikt bygget til HTTP
- I stedet bruger vi `websocket` package

**WebRTC:**
- En anden real-time protokol der giver peer-to-peer forbindelser mellem applikationer
- Sammenlignet med WebSocket som er mere egnet til forbindelser mellem servers eller mellem en server og en client
- WebRTC excellerer ved at streame data mellem clients uden at stole på server arkitekturer
- Widely used i video calling og live streaming softwares

---

## 📨 Message-driven Protocols

**Problem:**
- Streaming protokoller excellerer ved at levere kontinuerlig data mellem applikationer—ligesom to mennesker kommunikerer gennem telefonopkald
- Men der er scenarier hvor data fra flere applikationer skal distribueres til flere andre applikationer
- Eksempel: Journalister producerer nyhedsbreve for en publisher, som så leverer dem til subscribers
- Direkte kommunikation mellem hver applikation ville være upraktisk i sådanne tilfælde

**Løsning:** Message-driven protokoller

### MQTT (Message Queuing Telemetry Transport)

**Hvad er det?**
- Publish-subscribe message protokol
- Designet til resource-constrained devices (lav-power computere, smart home devices)
- Opererer på publish-subscribe (pub-sub) pattern:
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

**Note:**
- Brug `paho-mqtt` library
- Brug en public broker som HiveMQ på `broker.hivemq.com`
- Både publishers og subscribers kan køres som multiple instances på multiple devices

### Apache Kafka

**Hvad er det?**
- Følger også pub-sub pattern til at levere beskeder
- **Mere end en protokol** - et omfattende computing system
- Kan håndtere store mængder beskeder med lav latency
- Brugt i mange large-scale IT infrastrukturer (Netflix, Uber) til streaming og processing real-time events

**Arkitektur:**
- **Producers** (ligesom MQTT's publishers)
- **Consumers** (ligesom MQTT's subscribers)
- **Brokers**
- Deres respektive roller er meget lig dem i MQTT

**Forskelle fra MQTT:**
- Kafka er et high-performance system
- Bygget på toppen af clustering arkitektur hvor flere computere arbejder sammen
- Undgår system overload og opretholder konsistent hastighed selv med beskeder produceret ved høje rates

**Implementering i Python:**

```python
# producer.py
import os
from kafka import KafkaProducer
import json
import time

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=f"{os.getenv('KAFKA_ADDRESS')}:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Produce messages
for i in range(10):
    message = {'number': i, 'message': f'Hello Kafka! Message {i}'}
    producer.send('demo/ai-systems', value=message)
    print(f'Produced: {message}')
    time.sleep(1)

# Ensure all messages are sent
producer.flush()
producer.close()
print("All messages sent successfully!")

# consumer.py
import os
from kafka import KafkaConsumer
import json

# Create a Kafka consumer
consumer = KafkaConsumer(
    'demo/ai-systems',
    bootstrap_servers=f"{os.getenv('KAFKA_ADDRESS')}:9092",
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='demo-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Waiting for messages...")

# Consume messages
for message in consumer:
    message_value = message.value
    print(f'Consumed: {message_value}')
```

**Note:**
- Implementering er lidt kompliceret
- Du skal typisk køre ZooKeeper (Apache's clustering management system) og Kafka nodes separat
- Kafka's Python library `kafka-python` giver kun interfaces til faktiske Kafka nodes
- Når de er sat op, er implementering af producers og consumers lignende til publishers og subscribers i MQTT

---

## 🤖 Model Context Protocol (MCP)

**Problem:**
- Nylige fremskridt i conversational AI modeller—large language models (LLMs)—har vist stor potentiale i at løse komplekse opgaver
- Deres udnyttelse er meget afhængig af omfattende information de får og diversiteten af handlinger de kan udføre
- Når du interagerer med LLMs gennem conversation APIs, kan du manuelt feede så meget information som muligt ind i conversation context og instruere LLMs til at fortælle dig hvad du skal gøre i naturligt sprog
- Men denne proces aligner ikke med API filosofien: den er hverken automatisk eller reproducerbar, hvilket betyder den ikke kan skalere til production-level applikationer

**Løsning:**
- MCP introduceret af Anthropic i 2024
- Har hurtigt blivet standarden for conversational AI modeller til at integrere med eksterne informationskilder og tools
- Bygget på JSON-RPC 2.0—samme fundament som andre protokoller vi har udforsket
- Giver en standardiseret tilgang der eliminerer behovet for custom integrationer mellem hvert AI system og ekstern service
- Mens lignende funktionalitet kunne opnås gennem hardcoded custom interaktioner ved brug af konventionelle API teknikker, stammer MCP's udbredte adoption fra dens development simplicity og standardiserede tilgang

**Arkitektur:**

1. **Hosts:**
   - AI applikationer brugere interagerer med direkte (fx Claude Code, IDEs)
   - Disse applikationer indeholder LLMs der har brug for adgang til eksterne capabilities

2. **Servers:**
   - Eksterne applikationer der eksponerer specifikke capabilities til AI modeller gennem standardiserede interfaces
   - Disse kan inkludere database connectors, file system access tools, eller API integrationer med tredjepart services

3. **Clients:**
   - Lever inden for host applikationer
   - Styrer forbindelser mellem hosts og servers
   - Hver client opretholder dedikeret one-to-one forbindelse med specifik server, lignende til hvordan vi så individuelle forbindelser i vores tidligere protokol eksempler

**Capabilities MCP servers kan levere:**

1. **Resources:**
   - Act like read-only data sources, lignende til HTTP GET endpoints
   - Giver kontekstuel information uden signifikant computation eller side effects
   - Eksempel: En file system resource der giver adgang til dokumentation, mens en database resource kunne tilbyde read-only adgang til customer data

2. **Tools:**
   - Executable funktioner AI modeller kan kalde for at udføre specifikke handlinger
   - I modsætning til resources, kan tools modificere state, performe computationer, eller interagere med eksterne services
   - Eksempler: Sende emails, oprette calendar events, eller køre data analysis scripts

3. **Prompts:**
   - Pre-definerede templates der hjælper AI systemer med at bruge resources og tools mest effektivt
   - Giver strukturerede måder at accomplish common tasks
   - Kan deles på tværs af forskellige AI applikationer

**Kommunikationsmetoder:**

1. **stdio (Standard Input/Output):**
   - For lokale integrationer når clients og servers kører på samme maskine

2. **HTTP med SSE:**
   - For remote connections
   - Leverer samme SSE protokol vi udforskede tidligere for streaming responses

**Implementering:**
- Implementering af MCP servers og clients med Python er relativt ligetil
- Eksempler af en weather server og en MCP client er givet i de officielle quick start tutorials

**Ressourcer:**
- Specifikation: https://modelcontextprotocol.io/specification/
- Dokumentation: https://modelcontextprotocol.io/docs/
- Awesome MCP servers:
  - https://github.com/punkpeye/awesome-mcp-servers
  - https://github.com/wong2/awesome-mcp-servers
- Public MCP servers fra store virksomheder: Zapier, Notion

**Diskussion:**
- Skal du altid bruge MCP for at forbinde LLMs med eksterne resources og tools? Måske ikke.
- Blog posts om dette emne:
  - https://lucumr.pocoo.org/2025/7/3/tools/
  - https://decodingml.substack.com/p/stop-building-ai-agents

---

## ⚡ High-Performance Data Pipelines

**Problem:**
- I production miljøer kan protokoller alene være utilstrækkelige til at processe massive datasets
- Dette kan potentielt skabe bottlenecks i AI systemer
- High-performance data pipelines adresserer denne udfordring ved at give processing power nødvendig for large-scale data operationer

**Vi har allerede udforsket:**
- Kafka (excellerer ved at levere high-throughput beskeder)

**Her udforsker vi to yderligere systemer fra Apache:**
- Hadoop (excellerer ved at analysere large-scale data med høj hastighed og performance)
- Spark (excellerer ved at analysere large-scale data med høj hastighed og performance)

### Apache Hadoop

**Hvad er det?**
- Framework til at lagre og processe store mængder data i et distribueret computing environment (clustering)
- I essens er det faktisk en collection af open-source software
- Key idea: Udnytte clustering arkitektur til at håndtere massive mængder data

**To core layers:**

1. **HDFS (Hadoop Distributed File System):**
   - Arkitektur til at lagre store mængder data i et cluster
   - Bryder store filer i mindre blocks (typisk 128 MB eller 256 MB)
   - Lagrer dem på tværs af flere maskiner
   - Hver block replikeres flere gange (typisk 3) for fault tolerance—en almindelig clustering praksis hvor et par node failures ikke kompromitterer data integritet
   - Ligesom at købe tre kopier af en DVD og lagre dem i dit hus og din vens hus så du ikke sandsynligvis mister dem

2. **MapReduce:**
   - Computation layer til effektivt at processe store mængder data i et cluster
   - Input data divideres i chunks og processeres i parallel
   - Hver worker processerer en chunk og producerer key-value pairs
   - Disse key-value pairs grupperes derefter for at generere finale resultater
   - Tænk på hvordan store IT virksomheder splitter et stort software projekt i flere moduler for hver medarbejder at arbejde på individuelt, derefter merger alles arbejde til det endelige produkt
   - En almindelig måde at interagere med Hadoop systemer med Python er at skrive MapReduce jobs

### Apache Spark

**Hvad er det?**
- Både Spark og Hadoop er designet til large-scale data workloads
- Men de har distinkte arkitektoniske tilgange og forskelle i detaljerede funktionaliteter

**Forskelle fra Hadoop:**

1. **Storage:**
   - I modsætning til HDFS i Hadoop, har Spark ikke sit eget native file system
   - Kan integreres med eksterne storage systemer inkluderende HDFS eller databases
   - Dette gør dens implementering og deployment mere fleksibel
   - Del af denne fleksibilitet kommer fra det faktum at Hadoop stoler på sin HDFS data arkitektur
   - Spark's storage efficiency opnås primært gennem at lagre intermediate data i memory i stedet for på disks, hvilket normalt er meget hurtigere

2. **Computation:**
   - Spark's computation arkitektur er også forskellig fra Hadoop
   - To key koncepter:
     - **RDDs (Resilient Distributed Datasets):**
       - I essens immutable collections af data der er distribueret på tværs af et cluster af maskiner
       - Ligesom hver job tildelt hver medarbejder der ikke konflikter med hinanden
     - **DAG (Directed Acyclic Graph) Scheduler:**
       - Spark's hjerne til at finde ud af hvordan man computerer resultaterne
       - Ligesom hvordan et management team finder ud af hvordan man splitter et stort projekt i flere jobs

**Interaktion med Python:**
- Spark har built-in APIs der understøtter flere programmeringssprog til at interagere med sit system
- Inkluderer Python med `pyspark` library

**Note:**
- Vi vil dykke dybere ned i hele software og hardware arkitekturen af Kafka, Hadoop, og Spark i senere moduler, efter vi har fået nogle fundamentale kendskaber til clustering
- Lige nu ville det være lidt overvældende

---

## 📋 Opsummering til Mini Projekt

### Vigtige Koncepter at Inkludere:

1. **API Versioning** ✅ (Påkrævet)
   - Brug URL path versioning (fx `/v1/`, `/v2/`)
   - Dokumenter versioning strategi i rapporten

2. **Rate Limiting** ✅ (Påkrævet/Anbefalet)
   - Implementer rate limiting for AI endpoints
   - Overvej token-based eller request-based limiting
   - Dokumenter strategi

3. **REST Principper** ✅ (Påkrævet)
   - Design endpoints der følger REST
   - Proper HTTP metoder (GET, POST, PUT, DELETE)

4. **Streaming Support** ⭐ (Optional men anbefalet)
   - Implementer SSE for streaming responses
   - Særligt relevant hvis du har conversational AI endpoints
   - Giver bedre user experience

5. **Error Handling** ✅ (Påkrævet)
   - Proper error responses
   - Status codes
   - Informative fejlbeskeder

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

- **Brug FastAPI** (som vi har lært i kurset)
- **Implementer versioning fra start** - lettere end at tilføje senere
- **Overvej rate limiting fra start** - vigtigt for production
- **Test streaming** hvis relevant - giver bedre UX
- **Dokumenter alle design valg** - vigtigt for rapporten
- **Brug proper error handling** - vigtigt for robusthed

### Streaming Implementation Tips:

1. **SSE for FastAPI:**
   ```python
   from fastapi.responses import StreamingResponse
   
   @app.post("/v1/conversation")
   async def conversation_stream(request: ConversationRequest):
       async def generate():
           # Your streaming logic here
           for chunk in stream_response():
               yield f"data: {json.dumps(chunk)}\n\n"
       return StreamingResponse(generate(), media_type="text/event-stream")
   ```

2. **Client Side:**
   - Brug `EventSource` i JavaScript eller `requests` med `stream=True` i Python
   - Parse SSE format korrekt
   - Håndter connection termination signals

---

## ✅ Checklist til Mini Projekt

### API Design
- [ ] API versioning implementeret (fx `/v1/`, `/v2/`)
- [ ] REST principper følges
- [ ] Proper HTTP metoder brugt
- [ ] Error handling og proper status codes
- [ ] Dokumentation af design valg

### Rate Limiting
- [ ] Rate limiting implementeret for AI endpoints
- [ ] Strategi valgt (request-based, token-based, etc.)
- [ ] Algoritme valgt (fixed window, sliding window, token bucket)
- [ ] Dokumenteret i rapporten

### Streaming (Optional)
- [ ] Streaming support implementeret (hvis relevant)
- [ ] SSE eller WebSocket valgt
- [ ] Testet og fungerer korrekt
- [ ] Client kan håndtere streaming responses

### Testing
- [ ] Alle endpoints testet
- [ ] Error cases håndteret
- [ ] Rate limiting testet
- [ ] Streaming testet (hvis implementeret)

---

## 🔗 Ressourcer

### Streaming
- OpenAI Streaming: https://platform.openai.com/docs/api-reference/streaming
- Anthropic Streaming: https://docs.anthropic.com/claude/reference/messages-streaming

### Rate Limiting
- OpenAI Rate Limits: https://platform.openai.com/docs/guides/rate-limits
- Anthropic Rate Limits: https://docs.anthropic.com/claude/reference/rate-limits

### MCP
- MCP Spec: https://modelcontextprotocol.io/specification/
- MCP Docs: https://modelcontextprotocol.io/docs/
- Awesome MCP Servers: https://github.com/punkpeye/awesome-mcp-servers

### Libraries
- FastAPI: https://fastapi.tiangolo.com/
- paho-mqtt: https://pypi.org/project/paho-mqtt/
- kafka-python: https://kafka-python.readthedocs.io/
- websocket: https://pypi.org/project/websocket-client/

---

## 🎯 Exercise: Streaming Chatbot Enhancement

**Opgave:** Upgrade chatbot programmet fra API Fundamentals til at demonstrere avancerede API koncepter dækket i dette modul.

**Krav:**
1. **SSE Implementation:**
   - Brug Server-Sent Events som demonstreret i Server-Sent Events sektionen
   - Modtag responses ord-for-ord i stedet for at vente på komplet responses

2. **Stream Processing:**
   - Parse streaming response format
   - Håndter kontinuerlig data flow passende
   - Inkluder proper handling af connection termination signals

**Tips:**
- Start med at implementere basic SSE support
- Test med en AI API der understøtter streaming (OpenAI, Anthropic)
- Sørg for at håndtere edge cases (connection drops, timeouts, etc.)

