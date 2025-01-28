from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hommie paish'

@app.route('/greet')
def greet():
    return 'Hello, World!'

@app.route('/greet/<name>')
def greet_name(name):
    return f'Hello, {name}! 😏'


if __name__ == '__main__':
    app.run(debug=True)
