from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8653698830:AAG7_Wpnbc6pStgf3xhk6sfThZ7vfrQ9z9o"
CRYPTOBOT_API = "580459:AAAndC0pOAgJtEKxbKvSiXxFmPZWTRjv0VA"
CHANNEL_ID = "@xalorbqq"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and data.get('status') == 'paid':
        user_id = data.get('payload')
        amount = data.get('amount')
        if user_id:
            send_message(int(user_id), f"✅ Оплачено {amount} USDT")
            send_message(CHANNEL_ID, f"💸 Новая оплата: {amount} USDT")
    return "OK"

@app.route('/')
def home():
    return "✅ Webhook работает!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
