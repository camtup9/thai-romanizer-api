from flask import Flask, request, jsonify
from pythainlp.transliterate import romanize

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Thai Romanizer API đang chạy rồi nè!"

@app.route("/romanize", methods=["POST"])
def romanizer():
    data = request.get_json()
    thai_text = data.get("text", "")
    if not thai_text:
        return jsonify({"error": "Thiếu dữ liệu văn bản"}), 400
    result = romanize(thai_text, engine="thai2rom")
    return jsonify({"romanized": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
