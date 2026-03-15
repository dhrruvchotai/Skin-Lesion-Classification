<div align="center">

# Skin Lesion Classifier
### Part of the **MedicalGPT** Family of Models

![MedicalGPT](https://img.shields.io/badge/MedicalGPT-Family-red?style=for-the-badge&logo=health&logoColor=white)
![Model](https://img.shields.io/badge/Model-EfficientNet--B0-blue?style=for-the-badge)
![Dataset](https://img.shields.io/badge/Dataset-ISIC%202019-green?style=for-the-badge)
![Classes](https://img.shields.io/badge/Classes-8-orange?style=for-the-badge)
![Framework](https://img.shields.io/badge/Framework-PyTorch-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white)

*AI-powered dermatological analysis for early skin lesion detection*

---

</div>

## 🏥 About MedicalGPT

This model is part of the **MedicalGPT** family — a suite of specialized AI models designed to assist in clinical and diagnostic workflows. MedicalGPT models are built with the goal of making medical-grade AI accessible, interpretable, and deployable in real-world healthcare applications.

> ⚠️ **Disclaimer:** This model is intended for **research and assistive purposes only**. It is not a substitute for professional medical diagnosis. Always consult a qualified dermatologist for clinical decisions.

---

## 🔬 Model Overview

| Property | Details |
|---|---|
| **Architecture** | EfficientNet-B0 (fine-tuned) |
| **Task** | Multi-class Skin Lesion Classification |
| **Dataset** | ISIC 2019 Skin Lesion Images |
| **Classes** | 8 |
| **Input Size** | 224 × 224 px |
| **Framework** | PyTorch 2.x |
| **Best Val Accuracy** | 0.7375 (73.75%) |
| **Model Family** | MedicalGPT |

---

## 🏷️ Supported Classes

| Index | Abbreviation | Full Name |
|---|---|---|
| 0 | AK | Actinic Keratosis |
| 1 | BCC | Basal Cell Carcinoma |
| 2 | BKL | Benign Keratosis |
| 3 | DF | Dermatofibroma |
| 4 | NV | Melanocytic Nevus |
| 5 | MEL | Melanoma |
| 6 | SCC | Squamous Cell Carcinoma |
| 7 | VASC | Vascular Lesion |

---

## ⚙️ Model Architecture & Training

- **Base Model:** EfficientNet-B0 pretrained on ImageNet
- **Fine-tuning Strategy:** Partial fine-tuning — feature blocks 6, 7, 8 + classifier unfrozen
- **Class Imbalance Handling:** Inverse frequency class weighting in CrossEntropyLoss
- **Optimizer:** Adam with differential learning rates (backbone: 1e-4, classifier: 1e-3)
- **Scheduler:** CosineAnnealingLR over 30 epochs
- **Early Stopping:** Patience of 5 epochs on validation accuracy
- **Best model checkpoint** saved automatically during training

### Preprocessing Pipeline
```
Resize (260×260) → CenterCrop (224×224) → ToTensor → Normalize
mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
```

---

## 🚀 API Usage

### Endpoint
```
POST /predict
```

### Python
```python
import requests

url = "https://YOUR_USERNAME-skin-lesion-classifier.hf.space/predict"

with open("skin_image.jpg", "rb") as f:
    response = requests.post(url, files={"file": f})

print(response.json())
```

### JavaScript / Frontend
```javascript
const formData = new FormData();
formData.append("file", imageFile);

const response = await fetch(
  "https://YOUR_USERNAME-skin-lesion-classifier.hf.space/predict",
  { method: "POST", body: formData }
);

const result = await response.json();
console.log(result);
```

### Sample Response
```json
{
  "prediction": "Melanoma (MEL)",
  "confidence": 0.8731,
  "all_classes": [
    { "label": "Melanoma (MEL)",              "confidence": 0.8731 },
    { "label": "Basal Cell Carcinoma (BCC)",  "confidence": 0.0621 },
    { "label": "Actinic Keratosis (AK)",      "confidence": 0.0312 },
    { "label": "Melanocytic Nevus (NV)",      "confidence": 0.0198 },
    { "label": "Benign Keratosis (BKL)",      "confidence": 0.0087 },
    { "label": "Dermatofibroma (DF)",         "confidence": 0.0031 },
    { "label": "Squamous Cell Carcinoma (SCC)", "confidence": 0.0013 },
    { "label": "Vascular Lesion (VASC)",      "confidence": 0.0007 }
  ]
}
```

---

## 📊 Performance

| Metric | Score |
|---|---|
| Recall (Macro) | 0.6876 |
| Recall (Micro) | 0.7375 |
| Recall (Weighted) | 0.7375 |
| **Best Validation Accuracy** | **0.7375 (73.75%)** |

### Per-Class Recall
| Class | Recall |
|---|---|
| Actinic Keratosis (AK) | 0.6667 |
| Basal Cell Carcinoma (BCC) | 0.7757 |
| Benign Keratosis (BKL) | 0.5865 |
| Dermatofibroma (DF) | 0.6842 |
| Melanocytic Nevus (NV) | 0.6141 |
| Melanoma (MEL) | 0.8169 |
| Squamous Cell Carcinoma (SCC) | 0.5368 |
| Vascular Lesion (VASC) | 0.8200 |

---

## 🧪 Dataset

- **Source:** [ISIC 2019 - Skin Lesion Images for Classification](https://www.kaggle.com/datasets/salviohexia/isic-2019-skin-lesion-images-for-classification)
- **Total Samples:** ~25,331 images
- **Split:** 80% training / 20% validation

### Class Distribution
| Class | Samples |
|---|---|
| Melanoma (MEL) | 12,875 |
| Melanocytic Nevus (NV) | 4,522 |
| Basal Cell Carcinoma (BCC) | 3,323 |
| Benign Keratosis (BKL) | 2,624 |
| Actinic Keratosis (AK) | 867 |
| Squamous Cell Carcinoma (SCC) | 628 |
| Vascular Lesion (VASC) | 253 |
| Dermatofibroma (DF) | 239 |

---

## 🛠️ Deployment

This model is deployed using **Docker** on Hugging Face Spaces with a **FastAPI** backend.

```
Docker → FastAPI → EfficientNet-B0 → REST API
```

---

## 🧬 MedicalGPT Model Family

This is one model in the growing **MedicalGPT** ecosystem. The vision is to build a fully integrated AI platform where all specialist models work together, unified by a central Medical Chatbot that patients and doctors can talk to directly.

| Model | Domain | Status |
|---|---|---|
| 🔬 Skin Lesion Classifier | Dermatology | ✅ Live |
| 💬 MedicalGPT Chatbot | General Medical Queries & Patient Support | 🔜 Coming Soon |
| 📄 Medical OCR | Medicine & Report Reader | 🔜 Coming Soon |
| 🫁 Chest X-Ray Analyzer | Radiology | 🔜 Coming Soon |
| 👁️ Retinal Scan Classifier | Ophthalmology | 🔜 Coming Soon |

### 🤖 MedicalGPT Chatbot (Coming Soon)
A conversational AI assistant that will serve as the **central hub** of the MedicalGPT platform. Patients can ask general medical questions, describe symptoms, and get guidance — while the chatbot intelligently routes to the right specialist model (e.g. skin lesion classifier) when needed. All diagnostic results from every model feed back into the chatbot for a unified patient experience.

### 📄 Medical OCR (Coming Soon)
An OCR-powered module designed specifically for healthcare documents. It will be able to read and extract information from prescription slips, medicine labels, lab reports, and discharge summaries — making it easy for patients to understand their own medical documents without needing a doctor present.

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

Built with ❤️ as part of the **MedicalGPT** initiative

*Advancing AI for Healthcare*

</div>
