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
        result = romanize(thai_text, engine="royin")
        return jsonify({"romanized": result})
    except Exception as e:
        return jsonify({"error": f"Lỗi xử lý: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
