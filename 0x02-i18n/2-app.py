from flask_babel import Babel
from flask import Flask

class Config:
    ''' Defining the configuration attributes '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)

# Using 'from_object' loading configuration settings
# + from the specified object, in this case from Config class
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    Determining the best match with our supported languages.
    **** what is localselector? *****
    Flask-Babel relies on the locale_selector to determine which
    language to use for rendering content in your Flask application. 
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])
