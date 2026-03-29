from flask import Flask

from .routes import default_pages_blueprint


def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
    )

    app.register_blueprint(default_pages_blueprint)

    return app


app = create_app()
