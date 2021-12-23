from flask import Flask
from datetime import datetime
BREAK LINT
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

app = Flask(__name__)

@app.route("/")

def index():
    return f"Simple Flask Webapp for Devops Capstone by Patrick Mallon. Time: {now}"
            
app.run(host="0.0.0.0", port=8000, debug=True)