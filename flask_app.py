from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('layout.html',
        app_name = 'nuttyx',
        title = 'home',
        some_phrase = 'Hello')

if __name__ == "__main__":
    app.run()
