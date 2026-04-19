FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# BURADA KULLANICI TANIMLAMADIK -> VARSAYILAN ROOT! (TEHLİKE)
CMD ["python", "app.py"]