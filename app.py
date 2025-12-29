from flask import Flask, request, jsonify
from ai_sales_manager import ai_sales_reply
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "NV Shoppe AI Sales Manager is LIVE 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    reply = ai_sales_reply(user_msg)
    return jsonify({"reply": reply})

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    from twilio.twiml.messaging_response import MessagingResponse

    incoming = request.values.get("Body")
    response = ai_sales_reply(incoming)

    msg = MessagingResponse()
    msg.message(response)
    return str(msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

