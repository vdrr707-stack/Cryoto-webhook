from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "8653698830:AAG7_Wpnbc6pStgf3xhk6sfThZ7vfrQ9z9o"
CRYPTOBOT_API = "580459:AAAndC0pOAgJtEKxbKvSiXxFmPZWTRjv0VA"
CHANNEL_ID = "@xalorbqq"

def send_message(chat_id, text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown"
        })
    except Exception as e:
        print(f"Ошибка отправки: {e}")

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return "✅ Webhook endpoint работает. Отправьте POST-запрос."
    
    data = request.json
    print(f"Получен вебхук: {data}")
    
    if data and data.get('status') == 'paid':
        user_id = data.get('payload')
        amount = data.get('amount')
        
        if user_id:
            send_message(int(user_id), f"✅ *Оплата получена!*\n💰 Сумма: {amount} USDT")
            send_message(CHANNEL_ID, f"💸 *НОВАЯ ОПЛАТА*\n👤 ID: {user_id}\n💰 {amount} USDT")
    
    return jsonify({"ok": True}), 200

@app.route('/')
def home():
    return "✅ Webhook работает! Используйте /webhook"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
