from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "wow"
if __name__ == "__main__":
    app.run(host="localhost", port=int("8000"), debug=True)