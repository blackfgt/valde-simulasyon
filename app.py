from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Valde Simulasyon Calisiyor!"

@app.route('/ara')
def search_user():
    user_id = request.args.get('id')
    return f"Aranan Kullanici ID: {user_id}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)