from searcher import EmbeddedSearcher

from flask import Flask
from markupsafe import escape

SAMPLES_PATH = "static/items/"
model = EmbeddedSearcher(SAMPLES_PATH)

app = Flask(__name__, static_folder='static')

@app.route("/")
def root():
    return "<p>Hello, World!</p>"

# SAMPLES_PATH = "samples/"

# if __name__ == "__main__":
#     model = EmbeddedSearcher(SAMPLES_PATH)

#     while True:
#         query = input("Query: ")

#         items = model.query(query,5)
#         for num, file, confidence in items:
#             print(f"{num} {file}: {confidence}")