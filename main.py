from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi cloudwarriors is cool!'

if __name__ == '__main__':
    app.run(debug=True, port=8000)