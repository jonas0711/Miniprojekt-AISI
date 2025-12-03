# Dockerfile for CIFAR-10 Image Classification API
# Baseret på Modul 5: Packaging & Containerization

# Start med Python 3.11 slim image (mindre størrelse)
FROM python:3.11-slim

# Sæt working directory
WORKDIR /app

# Kopier requirements først (for bedre layer caching)
COPY requirements.txt .

# Installer dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Kopier applikationskode
COPY . .

# Expose port 8000
EXPOSE 8000

# Kør serveren
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

