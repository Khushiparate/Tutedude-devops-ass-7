from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Note: 'backend-service' is the DNS name in Kubernetes
        response = requests.get("http://backend-service")
        return f"Frontend: Connected to Backend! Message: {response.text}"
    except Exception as e:
        return f"Frontend: Could not connect to Backend. Error: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
