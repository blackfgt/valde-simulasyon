FROM python:3.12-slim

# GÜVENLİK GÜNCELLEMESİ: İşletim sistemi paketlerini güncelle
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Geri kalan adımlar aynı...
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Root olmayan kullanıcı (Önceki konuştuğumuz gibi)
RUN useradd -m emniyet_kullanicisi
USER emniyet_kullanicisi

CMD ["python", "app.py"]