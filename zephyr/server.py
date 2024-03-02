import sys
from flask import Flask, render_template
from libraries.compiler import compile

app = Flask(__name__, template_folder='./', static_folder='../app/')
DEV_PORT = 3000

DEBUG = '--debug' in sys.argv
print('DEBUG:', DEBUG)

@app.route('/')
def index():
    if DEBUG: # If in debug mode, compile the files before rendering the template
        compile()
    return render_template('.index.html')

def main():
    if not DEBUG: # If not in debug mode, compile the files before running the app
        compile()
    app.run(port=DEV_PORT, debug=DEBUG)


if __name__ == '__main__':
    main()
