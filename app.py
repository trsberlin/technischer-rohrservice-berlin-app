from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Technischer Rohrservice Berlin</title>
        <style>
            body{
                font-family: Arial;
                background:#111;
                color:white;
                text-align:center;
                padding:40px;
            }

            h1{
                color:#00c853;
                font-size:50px;
            }

            .button{
                display:inline-block;
                padding:15px 30px;
                margin:10px;
                background:#00c853;
                color:white;
                text-decoration:none;
                border-radius:10px;
                font-size:20px;
            }

            .card{
                background:#1e1e1e;
                padding:20px;
                margin:20px auto;
                border-radius:15px;
                max-width:700px;
            }
        </style>
    </head>

    <body>

        <h1>Technischer Rohrservice Berlin</h1>

        <p>24/7 Rohrreinigung & Notdienst in Berlin</p>

        <a class="button" href="tel:+49123456789">
            Jetzt anrufen
        </a>

        <a class="button" href="https://wa.me/49123456789">
            WhatsApp
        </a>

        <div class="card">
            <h2>Unsere Leistungen</h2>

            <p>✔ Rohrreinigung</p>
            <p>✔ Abflussreinigung</p>
            <p>✔ Notdienst</p>
            <p>✔ Hochdruckspülung</p>
        </div>

        <div class="card">
            <h2>Schnell vor Ort</h2>

            <p>Berlin & Umgebung</p>
            <p>Auch am Wochenende erreichbar</p>
        </div>

    </body>
    </html>
    """
