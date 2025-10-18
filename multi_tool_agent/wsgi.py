# wsgi.py
from flask import Flask, request, jsonify
from multi_tool_agent.agent import ask

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200

@app.route("/ask", methods=["POST"])
def ask_endpoint():
    payload = request.get_json(force=True)
    prompt = payload.get("prompt")
    if not prompt:
        return jsonify({"error": "missing prompt"}), 400
    try:
        result = ask(prompt)
        # ensure result is JSON-serializable (ADK returned object may be complex)
        return jsonify({"result": str(result)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
