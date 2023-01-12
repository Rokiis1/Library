from flask import Flask, render_template
import uvicorn

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="0.0.0.0")
