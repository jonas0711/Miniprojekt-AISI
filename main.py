"""
FastAPI Server for CIFAR-10 Image Classification
Baseret på Modul 3: Wrap AI Models with APIs
"""

from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from pydantic import BaseModel
from typing import List, Optional
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet18
from PIL import Image
import base64
import io

# CIFAR-10 klasser (10 kategorier)
CIFAR10_CLASSES = [
    "airplane", "car", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]


class ImageClassifier:
    """Klasse til at håndtere CIFAR-10 image classification"""
    
    def __init__(self):
        self.model = None
        self.model_name = "ResNet-18 (CIFAR-10)"
    
    async def load_model(self):
        """Loader CIFAR-10 modellen"""
        if self.model is None:
            print(f"Loading model: {self.model_name}")
            # ResNet-18 modificeret til 10 klasser
            self.model = resnet18(pretrained=False)
            self.model.fc = torch.nn.Linear(self.model.fc.in_features, 10)
            self.model.eval()
            print("Model loaded successfully")
    
    async def classify_image(self, image: Image.Image) -> dict:
        """Klassificerer et billede"""
        if self.model is None:
            await self.load_model()
        
        # Preprocess image til 32x32
        transform = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        input_tensor = transform(image).unsqueeze(0)
        
        # Kør inference
        with torch.no_grad():
            outputs = self.model(input_tensor)
            predictions = torch.nn.functional.softmax(outputs[0], dim=0)
        
        # Top 5 predictions
        top5_probs, top5_indices = torch.topk(predictions, 5)
        results = []
        
        for prob, idx in zip(top5_probs, top5_indices):
            results.append({
                "label": CIFAR10_CLASSES[idx.item()],
                "confidence": round(prob.item(), 4)
            })
        
        return {
            "predictions": results,
            "model": self.model_name
        }


# Initialize classifier
classifier = ImageClassifier()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager - loader modellen ved startup"""
    await classifier.load_model()
    yield


app = FastAPI(
    title="CIFAR-10 Image Classification API",
    version="1.0.0",
    lifespan=lifespan
)


# Data Models
class ImageRequest(BaseModel):
    image: str  # base64 encoded image
    filename: Optional[str] = None


class ClassificationResponse(BaseModel):
    predictions: List[dict]
    model: str


class ModelInfo(BaseModel):
    name: str
    status: str
    num_labels: Optional[int] = None


def decode_base64_image(base64_string: str) -> Image.Image:
    """Dekoder base64 string til PIL Image"""
    try:
        if base64_string.startswith('data:image'):
            base64_string = base64_string.split(',')[1]
        image_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
        return image
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid base64 image: {str(e)}")


# Routes
@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to CIFAR-10 Image Classification API"}


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_status": "loaded" if classifier.model is not None else "not loaded"
    }


@app.get("/model/info", response_model=ModelInfo)
async def model_info():
    """Returnerer model information"""
    if classifier.model is None:
        return ModelInfo(
            name=classifier.model_name,
            status="not_loaded"
        )
    return ModelInfo(
        name=classifier.model_name,
        status="loaded",
        num_labels=10
    )


@app.post("/image_classify", response_model=ClassificationResponse)
async def classify_image(request: ImageRequest):
    """Klassificerer et base64 encoded billede"""
    try:
        image = decode_base64_image(request.image)
        result = await classifier.classify_image(image)
        return ClassificationResponse(**result)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
