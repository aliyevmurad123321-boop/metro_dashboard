from flask import Flask, render_template, jsonify
from data import get_sixliq_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def api_data():
    data = get_sixliq_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)