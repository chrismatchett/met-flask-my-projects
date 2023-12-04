from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    from . import notes
    app.register_blueprint(notes.bp)

    return app