import sys
from flask import Flask, render_template
from libraries.compiler import compile

app = Flask(__name__, template_folder="./", static_folder="../app/")

DEBUG = "--debug" in sys.argv
print("DEBUG:", DEBUG)


@app.route("/")
def index():
    if DEBUG:  # If in debug mode, compile the files before rendering the template
        compile()
    return render_template(".index.html")


def main():
    if not DEBUG: # If not in debug mode, compile the files before running the app
        compile()
        port = 80
    else: # If in debug mode, set the port to 8080
        port = 8080

    app.run(port=port, debug=DEBUG)


if __name__ == "__main__":
    main()
