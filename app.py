from flask import Flask, render_template, request
from scraper import fetch_case_details
from utils.logger import log_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    data = request.form
    result = fetch_case_details(data['case_type'], data['case_number'], data['year'])
    log_query(data, result.get('raw_html', ''))

    if result['error']:
        return render_template('index.html', result=None, error=result['error'])

    return render_template('index.html', result=result, error=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

