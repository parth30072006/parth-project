from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/products')
def products():
    return 'this is product!'
if __name__ == '__main__':
    app.run(debug=True)