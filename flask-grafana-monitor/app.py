from flask import Flask, jsonify, request
from prometheus_client import start_http_server, Counter, generate_latest, REGISTRY
from prometheus_client.exposition import basic_auth_handler

# Create Flask app
app = Flask(__name__)

# Define Prometheus counters
http_requests_total = Counter(
    'http_requests_total', 
    'Total HTTP requests', 
    ['method', 'status']
)

# Endpoint for metrics
@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY)

# Basic endpoint for demo
@app.route('/hello', methods=['GET'])
def hello():
    http_requests_total.labels(method='GET', status='200').inc()
    return jsonify({"message": "Hello World!"})

# Simulate 4xx and 5xx errors
@app.route('/error/<int:error_code>', methods=['GET'])
def error(error_code):
    if error_code == 404:
        http_requests_total.labels(method='GET', status='404').inc()
        return "Not Found", 404
    elif error_code == 500:
        http_requests_total.labels(method='GET', status='500').inc()
        return "Internal Server Error", 500
    else:
        http_requests_total.labels(method='GET', status='200').inc()
        return "All good", 200

# Start the Prometheus client HTTP server to expose the metrics
if __name__ == "__main__":
    start_http_server(8000)  # Expose metrics on port 8000
    app.run(host='0.0.0.0', port=5000)  # Flask app runs on port 5000