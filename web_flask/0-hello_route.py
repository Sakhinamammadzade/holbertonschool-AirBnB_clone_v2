from flask import Flask, request
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "HBNB!")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    app.run(debug=True)
