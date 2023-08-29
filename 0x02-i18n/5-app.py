#!/usr/bin/env python3
""" working on translation """
from flask_babel import Babel, request
from flask import Flask, render_template, g


class Config:
    """Defining the configuration attributes"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

# Using 'from_object' loading configuration settings
# + from the specified object, in this case from Config class
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    Determining the best match with our supported languages.
    """
    language = app.config["LANGUAGES"]
    if "locale" in request.args and request.args["locale"] in language:
        return request.args["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def hello():
    """Rendering hello world"""
    return render_template("5-index.html")


def get_user():
    """Returns a user dictionary or None if not found"""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (ValueError, TypeError, KeyError):
        return None


@app.before_request
def before_request():
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
