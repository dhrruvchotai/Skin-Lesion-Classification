from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import torch
import torch.nn as nn
from torchvision.models import efficientnet_b0
from torchvision import transforms
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CLASS_LABELS = [
    "Actinic Keratosis (AK)",
    "Basal Cell Carcinoma (BCC)",
    "Benign Keratosis (BKL)",
    "Dermatofibroma (DF)",
    "Melanoma (MEL)",
    "Melanocytic Nevus (NV)",
    "Squamous Cell Carcinoma (SCC)",
    "Vascular Lesion (VASC)",
]

model = efficientnet_b0(weights=None)
model.classifier[1] = nn.Linear(model.classifier[1].in_features, 8)
model.load_state_dict(torch.load("model.pth", map_location="cpu"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((260, 260)),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

@app.get("/")
def root():
    return {"message": "Skin Lesion Classifier API is running!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read uploaded image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # Run inference
    #add the new dimension (for batch size) using unsqueeze
    tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(tensor)
        probs = torch.softmax(outputs, dim=1)[0]

    # Build response
    results = [
        {"label": CLASS_LABELS[i], "confidence": round(float(probs[i]), 4)}
        for i in range(8)
    ]
    results.sort(key=lambda x: x["confidence"], reverse=True)

    return {
        "prediction": results[0]["label"],
        "confidence": results[0]["confidence"],
        "all_classes": results
    }