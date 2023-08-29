#!/usr/bin/env python3
''' working on translation '''
from flask_babel import Babel, request
from flask import Flask, render_template


class Config:
    """Defining the configuration attributes"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determining the best match with our supported languages.
    **** what is localselector? *****
    Flask-Babel relies on the locale_selector to determine which
    language to use for rendering content in your Flask application.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def hello():
    """Rendering hello world"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
