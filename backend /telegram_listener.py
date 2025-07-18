from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/notify", methods=["POST"])
def notify():
    msg = request.json.get("message")
    with open("static/notice.json", "w") as f:
        json.dump({"message": msg}, f)
    return {"status": "sent"}

# شغّل السيرفر بالداخل: flask run
