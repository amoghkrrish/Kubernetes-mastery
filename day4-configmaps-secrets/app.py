import os
from flask import Flask
app = Flask(__name__)

welcome = os.environ.get("welcome_message","Default_Hello")
api_key = os.environ.get("API_KEY","no-key")

@app.route("/")
def home():
    return f"<h1>{welcome}</h1><p>API Key: {api_key}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
