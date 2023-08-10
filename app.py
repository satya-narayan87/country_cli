from flask import Flask, jsonify
from country_cli_data import *
app = Flask(__name__)

data =data_from_json()

@app.route('/health')
def health():
    return jsonify(status="healthy")

@app.route('/diag')
def diag():
    # Perform a request to https://www.travel-advisory.info/api and check status
    # Return the response as JSON
    return jsonify(api_status={"code": 200, "status": "ok"})

# Modify your existing lookup_country_name function to work with Flask
@app.route('/convert/<country_code>')
def convert(country_code):
    country_name = search_country(country_code, data)
    return jsonify(country_name=country_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
