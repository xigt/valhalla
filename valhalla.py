
import json

from flask import Flask, render_template

import sleipnir

app = Flask(__name__)
app.register_blueprint(sleipnir.v1)

with open('config.json') as f:
    settings = json.loads(f.read())

@app.route('/')
def index():
    return render_template('index.html', settings=settings)

if __name__ == '__main__':
    app.run()

