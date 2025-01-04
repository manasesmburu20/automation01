from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Updated now by me again twice!thrice"

if __name__ == "__main__":
    app.run(debug=True)
