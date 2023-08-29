#!/usr/bin/env python3
""" Instantiating Babel """
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Defining the configuration attributes"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

# Using 'from_object' loading configuration settings
# + from the specified object, in this case from Config class
app.config.from_object(Config)

"""
*****why app.config?******
app.cofig refers to the configuration dictionary associated with
your Flask application. It's where you store configuration
settings that affect how your application behaves.
"""

# Instantiate the Babel object
babel = Babel(app)

@app.route("/", strict_slashes=False)
def hello():
    """Rendering hello world"""
    return render_template("0-index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
