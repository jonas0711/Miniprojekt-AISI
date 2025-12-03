"""
Klientprogram til CIFAR-10 Image Classification API
Baseret på Modul 1 & 2: Interact with AI Systems

Dette program kan kalde API serveren og teste endpoints
"""

import requests
import base64
import json
import sys
from pathlib import Path


# API server URL
# Standard: EC2 serveren på 51.21.200.191:8000
# Eller lokal test: http://127.0.0.1:8000
API_BASE_URL = "http://51.21.200.191:8000"


def encode_image_to_base64(image_path: str) -> str:
    """
    Encoder et billede til base64 string
    
    Args:
        image_path: Sti til billedfilen
        
    Returns:
        Base64 encoded string
    """
    print(f"DEBUG: Encoding image: {image_path}")
    
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_string = base64.b64encode(image_data).decode('utf-8')
            print(f"DEBUG: Image encoded successfully. Size: {len(base64_string)} characters")
            return base64_string
    except Exception as e:
        print(f"ERROR: Failed to encode image: {str(e)}")
        raise


def check_health():
    """
    Tjekker om API serveren kører korrekt
    GET /health endpoint
    """
    print("\n=== Testing Health Endpoint ===")
    print(f"DEBUG: Calling GET {API_BASE_URL}/health")
    
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=10)
        response.raise_for_status()
        
        print(f"DEBUG: Response status: {response.status_code}")
        print(f"DEBUG: Response: {response.json()}")
        
        data = response.json()
        print(f"\n✅ Server Status: {data.get('status')}")
        print(f"✅ Model Status: {data.get('model_status')}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: Health check failed: {str(e)}")
        return False


def get_model_info():
    """
    Henter information om modellen
    GET /model/info endpoint
    """
    print("\n=== Testing Model Info Endpoint ===")
    print(f"DEBUG: Calling GET {API_BASE_URL}/model/info")
    
    try:
        response = requests.get(f"{API_BASE_URL}/model/info", timeout=10)
        response.raise_for_status()
        
        print(f"DEBUG: Response status: {response.status_code}")
        
        data = response.json()
        print(f"\n✅ Model Name: {data.get('name')}")
        print(f"✅ Status: {data.get('status')}")
        print(f"✅ Number of Classes: {data.get('num_labels')}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: Model info failed: {str(e)}")
        return False


def classify_image(image_path: str):
    """
    Klassificerer et billede ved hjælp af API serveren
    POST /image_classify endpoint
    
    Args:
        image_path: Sti til billedfilen at klassificere
    """
    print("\n=== Testing Image Classification Endpoint ===")
    print(f"DEBUG: Classifying image: {image_path}")
    
    # Encoder billede til base64
    base64_image = encode_image_to_base64(image_path)
    
    # Opret request body
    request_body = {
        "image": base64_image,
        "filename": Path(image_path).name
    }
    
    print(f"DEBUG: Calling POST {API_BASE_URL}/image_classify")
    print(f"DEBUG: Request body size: {len(json.dumps(request_body))} characters")
    
    try:
        # Send POST request
        response = requests.post(
            f"{API_BASE_URL}/image_classify",
            json=request_body,
            headers={"Content-Type": "application/json"},
            timeout=30  # Image classification kan tage lidt tid
        )
        
        response.raise_for_status()
        
        print(f"DEBUG: Response status: {response.status_code}")
        
        data = response.json()
        
        print(f"\n✅ Classification Results:")
        print(f"   Model: {data.get('model')}")
        print(f"   Top Prediction: {data.get('top_prediction')}")
        print(f"   Confidence: {data.get('confidence')}")
        print(f"\n   All Predictions:")
        
        for i, pred in enumerate(data.get('predictions', []), 1):
            print(f"   {i}. {pred['label']}: {pred['confidence']}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: Classification failed: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   Response: {e.response.text}")
        return False


def main():
    """
    Hovedfunktion - tester alle endpoints
    """
    print("=" * 50)
    print("CIFAR-10 API Client")
    print("=" * 50)
    print(f"API Server: {API_BASE_URL}")
    
    # Test health endpoint
    if not check_health():
        print("\n❌ Server is not responding. Please check:")
        print("   1. Is the server running?")
        print("   2. Is the URL correct?")
        print("   3. Can you reach the server?")
        sys.exit(1)
    
    # Test model info endpoint
    get_model_info()
    
    # Test image classification
    # Hvis der er givet et billede som argument, brug det
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        if not Path(image_path).exists():
            print(f"\n❌ ERROR: Image file not found: {image_path}")
            sys.exit(1)
        classify_image(image_path)
    else:
        print("\n⚠️  No image provided for classification")
        print("   Usage: python client.py <image_path>")
        print("   Example: python client.py test_image.jpg")
    
    print("\n" + "=" * 50)
    print("Testing complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()

