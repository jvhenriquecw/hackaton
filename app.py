from flask import Flask
app = Flask(__name__)

@app.route('/')
def ola():
    return 'ola'

if __name__ == '__main__':
    app(debug=True)