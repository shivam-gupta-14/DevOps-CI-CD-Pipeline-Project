from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello! This is Shivam's DevOps Project</h1><p>Deployed via CI/CD Pipeline on AWS!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)