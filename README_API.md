# CIFAR-10 Image Classification API

Simpel FastAPI server til at klassificere billeder i 10 kategorier.

## Endpoints

### 1. GET `/` - Root
Returnerer velkomstbesked og liste af endpoints.

### 2. GET `/health` - Health Check
Tjekker om serveren kører korrekt.
```bash
curl http://localhost:8000/health
```

### 3. GET `/model/info` - Model Information
Returnerer information om CIFAR-10 modellen.
```bash
curl http://localhost:8000/model/info
```

### 4. POST `/image_classify` - Image Classification (AI Funktionalitet)
Klassificerer et billede. Modtager base64 encoded image i JSON.

**Request body:**
```json
{
  "image": "base64_encoded_image_string",
  "filename": "optional_filename.jpg"
}
```

**Response:**
```json
{
  "predictions": [
    {"label": "airplane", "confidence": 0.8542},
    {"label": "ship", "confidence": 0.1234},
    ...
  ],
  "model": "ResNet-18 (CIFAR-10)",
  "top_prediction": "airplane",
  "confidence": 0.8542
}
```

### 5. POST `/image_classify/upload` - File Upload
Alternativ endpoint der modtager file upload i stedet for base64.

```bash
curl -X POST -F "file=@image.jpg" http://localhost:8000/image_classify/upload
```

## Kør serveren lokalt

```bash
# Installer dependencies
pip install -r requirements.txt

# Kør serveren
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Serveren kører på: `http://127.0.0.1:8000`

## CIFAR-10 Klasser

1. airplane
2. car
3. bird
4. cat
5. deer
6. dog
7. frog
8. horse
9. ship
10. truck

## Noter

- Modellen er en simpel ResNet-18 model modificeret til CIFAR-10 (10 klasser)
- Billeder bliver automatisk resized til 32x32 pixels
- Modellen loades ved server startup for bedre performance

