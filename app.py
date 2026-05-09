from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Technischer Rohrservice Berlin</h1>
    <p>24/7 Rohrreinigung & Notdienst in Berlin</p>
    <button>Jetzt anrufen</button>
    """
