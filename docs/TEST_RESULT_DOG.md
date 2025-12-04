# Test Resultat: Classification af dog.jpg

**Dato:** 4. december 2025
**Server:** 51.21.200.191 (EC2)
**Klient:** client.py (Lokal maskine)

## Test Setup
Vi testede API'en ved at downloade et billede af en hund og sende det gennem vores klientprogram til serveren.

**Billede:** [dog.jpg](https://raw.githubusercontent.com/pytorch/hub/master/images/dog.jpg)
**Kommando:**
```bash
python client.py dog.jpg
```

## Resultat (Output)

```text
API Server: http://51.21.200.191:8000
Server Status: healthy
Model Status: loaded
Model: ResNet-18 (CIFAR-10)
Status: loaded
Classes: 10

Classification Results:
Model: ResNet-18 (CIFAR-10)

Top Predictions:
1. dog: 0.2011  (20.11%)
2. bird: 0.1491 (14.91%)
3. ship: 0.1273 (12.73%)
4. cat: 0.1174  (11.74%)
5. airplane: 0.083 (8.30%)
```

## Konklusion
- **Status:** ✅ Success
- **Korrekthed:** Modellen klassificerede korrekt billedet som en **hund** (dog) med højeste sandsynlighed.
- **Funktionalitet:** Dette bekræfter at hele pipelinen virker:
    1.  Klient encoder billede til Base64.
    2.  Sender request over internettet til EC2.
    3.  Docker container modtager request.
    4.  FastAPI decoder og pre-processer billedet.
    5.  PyTorch modellen kører inference.
    6.  Resultatet sendes retur til klienten.
