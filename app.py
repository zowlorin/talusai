from searcher import EmbeddedSearcher

from flask import Flask, request, jsonify
from markupsafe import escape

SAMPLES_PATH = "static/items/"
model = EmbeddedSearcher(SAMPLES_PATH)

app = Flask(__name__, static_folder='static')

@app.route("/api/search")
def search():
    query = request.args.get("query", type=str)
    start = request.args.get("start", 0, type=int)
    count = request.args.get("count", 5, type=int)

    if query is None: return jsonify({ "code": 1 })

    items = model.query(query, start, count)
    formatted = [{ "path": path, "confidence": confidence } for path, confidence in items]
    return jsonify(formatted)

if __name__ == "__main__":
    app.run(port=3001)