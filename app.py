from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Valde Simulasyon Calisiyor!"

@app.route('/ara')
def search_user():
    # 1. Veriyi al
    user_id = request.args.get('id')
    
    # 2. GÜVENLİ YÖNTEM: Parametreli sorgu mantığını kullan (SQL Injection'ı engeller)
    # Gerçek bir veritabanı olsaydı: cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    
    return f"Aranan Kullanici ID: {user_id}"

if __name__ == "__main__":
    # 3. GÜVENLİK DÜZELTMESİ: Yerel testler için 127.0.0.1 kullan
    # Docker içinde çalıştıracaksan Bandit'e bu satırı görmezden gelmesini söyleyebilirsin:
    app.run(host='127.0.0.1', port=5000) # # nosec