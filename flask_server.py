from flask import Flask, request

app = Flask(__name__)
latest_message = ""

@app.route('/message', methods=['POST'])
def receive_message():
    global latest_message
    latest_message = request.json.get("text", "")
    print(f"📥 Received message: {latest_message}")
    return "✅ Message saved", 200

@app.route('/message.txt', methods=['GET'])
def get_message():
    return latest_message or "⚠️ لا توجد رسالة حالياً", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)