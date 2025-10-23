from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return f"<h1>Main Page</h1>"

@app.route('/multiply/<int:x1>/<int:x2>/<int:x3>/<int:x4>')
def multiply(x1, x2, x3, x4):
    return f"<h1>Multiplication equals to: {x1 * x2 * x3 * x4}</h1>"

@app.route('/json')
def json():
    return jsonify({'hello': 'world'})

@app.route('/goto_json')
def goto_json():
    return redirect(url_for("json"))

@app.route('/hello/<name>')
def hello(name):
    return f"<h1>Hello {name}!</h1>"

@app.errorhandler(404)
def page_not_found(e):
    return f"<h1>Kai axla, mand ra ginda</h1>"

if __name__ == '__main__':
    app.run(debug=True)