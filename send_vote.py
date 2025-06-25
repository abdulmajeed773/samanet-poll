from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/send_vote", methods=["POST"])
def receive_vote():
    data = request.json
    poll_id = data.get("poll_id")
    answer = data.get("answer")
    client_ip = request.remote_addr

    if not poll_id or not answer:
        return jsonify({"error": "البيانات ناقصة"}), 400

    # طباعة التصويت في سجل Render (أو اربطه مع بوت لاحقاً)
    print(f"🗳️ تصويت جديد | السؤال: {poll_id} | الإجابة: {answer} | IP: {client_ip}")

    return jsonify({"message": "✅ تم استلام التصويت"}), 200

if __name__ == "__main__":
    app.run()