"""
Klientprogram til CIFAR-10 Image Classification API
Baseret på Modul 1 & 2: Interact with AI Systems
"""

import requests
import base64
import sys
from pathlib import Path

# API server URL
API_BASE_URL = "http://51.21.200.191:8000"


def encode_image_to_base64(image_path: str) -> str:
    """Encoder et billede til base64 string"""
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        return base64.b64encode(image_data).decode('utf-8')


def check_health():
    """Tjekker om API serveren kører korrekt"""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"Server Status: {data.get('status')}")
        print(f"Model Status: {data.get('model_status')}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {str(e)}")
        return False


def get_model_info():
    """Henter information om modellen"""
    try:
        response = requests.get(f"{API_BASE_URL}/model/info", timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"Model: {data.get('name')}")
        print(f"Status: {data.get('status')}")
        print(f"Classes: {data.get('num_labels')}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {str(e)}")
        return False


def classify_image(image_path: str):
    """Klassificerer et billede"""
    base64_image = encode_image_to_base64(image_path)
    
    request_body = {
        "image": base64_image,
        "filename": Path(image_path).name
    }
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/image_classify",
            json=request_body,
            timeout=30
        )
        response.raise_for_status()
        
        data = response.json()
        print(f"\nClassification Results:")
        print(f"Model: {data.get('model')}")
        print(f"\nTop Predictions:")
        
        for i, pred in enumerate(data.get('predictions', []), 1):
            print(f"{i}. {pred['label']}: {pred['confidence']}")
        
        return True
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {str(e)}")
        return False


def main():
    """Hovedfunktion"""
    print(f"API Server: {API_BASE_URL}")
    
    if not check_health():
        print("Server is not responding")
        sys.exit(1)
    
    get_model_info()
    
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        if not Path(image_path).exists():
            print(f"ERROR: Image file not found: {image_path}")
            sys.exit(1)
        classify_image(image_path)
    else:
        print("Usage: python client.py <image_path>")


if __name__ == "__main__":
    main()
