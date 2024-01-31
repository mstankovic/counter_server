from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

counter = 0

@app.route('/')
def index():
    return render_template('index.html', counter=counter)

@app.route('/get', methods=['GET'])
def get_counter():
    return jsonify({'counter': counter})

@app.route('/add', methods=['POST'])
def update_counter():
    global counter
    counter += 1
    return jsonify({'counter': counter})

if __name__ == '__main__':
    # Use Gunicorn to serve the Flask app
    app.run()
