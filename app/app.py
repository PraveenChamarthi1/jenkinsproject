from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! Welcome to GCP and Hi!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)