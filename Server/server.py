from flask import Flask
app = Flask(__name__)
@app.get("/")
def home():
    return "hello from flask"
app.run(debug=True)