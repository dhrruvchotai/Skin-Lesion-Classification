FROM python:3.12-slim

#create a folder called /app inside the container
WORKDIR /app

# Copy requirements.txt into the container first
COPY requirements.txt .

# Install all Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy your remaining files into the container
COPY app.py .
COPY model.pth .

# Open port 7860 (because to deploy on hugging face it needs exactly this prot soo)
EXPOSE 7860


CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]