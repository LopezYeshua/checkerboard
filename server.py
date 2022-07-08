from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    num1 = 8
    num2 = 8
    return render_template('index.html', num1 = num1, num2 = num2)

@app.route('/<int:num2>')
def tallerBoard(num2):
    num1 = 8
    return render_template("index.html", num1=num1, num2=num2)

@app.route('/<int:num2>/<int:num1>')
def biggerBoard(num2, num1):
    return render_template("index.html", num2 = num2, num1 = num1)


if __name__ == '__main__':
    app.run(debug=True)