from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello,This is Gnits.welcome to devops lab"

if __name__ == "__main__":
    app.run(debug=True)