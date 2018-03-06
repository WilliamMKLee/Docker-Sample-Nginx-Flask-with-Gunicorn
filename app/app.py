from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', host=os.environ['HOSTNAME'])

# this only for testing purpose
# should using nginx or something to serve static file
#@app.route('/static/<path:path>')
#def send_static(path):
#    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
