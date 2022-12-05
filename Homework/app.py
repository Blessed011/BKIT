from flask import Flask
from lazy_fibonacci import fibonacci

app = Flask(__name__)
@app.route('/num/<number>')
def num(number):
    return str(list(fibonacci(int(number))))


if __name__ == "__main__":
    app.run()
