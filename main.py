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
        if not data or "text" not in data:
            return jsonify({"error": "Thiếu dữ liệu văn bản"}), 400
        thai_text = data["text"].strip()
        result = romanize(thai_text, engine="thai2rom")
        return jsonify({"romanized": result})
    except Exception as e:
        return jsonify({"error": "Lỗi xử lý: " + str(e)}), 500
