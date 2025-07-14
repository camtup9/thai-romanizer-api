from flask import Flask, request, jsonify
from pythainlp.transliterate import romanize

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Thai Romanizer API đang chạy rồi nè!"

@app.route("/romanize", methods=["POST"])
def romanizer():
    try:
        data = request.get_json(force=True)
        thai_text = data.get("text", "")
        if not thai_text:
            return jsonify({"error": "Thiếu dữ liệu văn bản"}), 400
        result = romanize(thai_text, engine="thai2rom")
        return jsonify({"romanized": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
