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
    locale = request.args.get("locale")
    # Let us first check if the preffered language from URL
    # + is match in the supported languages(fr, en)
    if locale in app.config["LANGUAGES"]:
        return locale

    # Get locale from user settings (if available) and check if
    # the 'locale' exist in the user setting
    if g.user and "locale" in g.user:
        user_locale = g.user["locale"]
        # Then check if the locale key in the user setting matches
        # + with one of the supported languges
        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    locale = request.headers.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def hello():
    """Rendering hello world"""
    return render_template("7-index.html")


def get_user():
    """Returns a user dictionary or None if not found"""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (ValueError, TypeError, KeyError):
        return None


@app.before_request
def before_request():
    """This function stores user information to the global variable"""
    g.user = get_user()


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the best-matching time zone.
    """
    # Find timezone parameter in URL parameters
    timezone_param = request.args.get('timezone')
    if timezone_param:
        try:
            pytz.timezone(timezone_param)
            return timezone_param
        except pytz.UnknownTimeZoneError:
            pass

    # Find time zone from user settings (if available)
    if g.user and 'timezone' in g.user:
        user_timezone = g.user['timezone']
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.UnknownTimeZoneError:
            pass

    # Default to UTC
    return 'UTC'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
