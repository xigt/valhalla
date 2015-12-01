
from flask import Flask, render_template

import sleipnir

app = Flask(__name__)
app.register_blueprint(sleipnir.blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

