from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "updated the text1!"

if __name__ == "__main__":
    app.run(debug=True)
