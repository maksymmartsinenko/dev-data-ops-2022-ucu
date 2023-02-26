from flask import Flask, request
from pymongo import MongoClient
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
        <html>
        <body>
            <form method='POST' action='/submit'>
                <input type='text' name='data' />
                <button type='submit'>Submit</button>
            </form>
        </body>
        </html>
    """

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.get("data")
    client = MongoClient(os.environ["MONGO_URI"])
    db = client["mydatabase"]
    collection = db["responses"]
    collection.insert_one({"data": data})
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 80)))
