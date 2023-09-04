import os
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()


SWAGGER_URL = "/api_documentation"
API_URL = "http://127.0.0.1:5000/static/swagger/swagger.json"

SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "ferstore_app"}
)


def create_app(test_config=None):
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder="../dist",
        static_url_path="",
    )

    app.config.from_object("config.DevelopmentConfig")
    app.config["JWT_SECRET_KEY"] = "super-secret"
    db.init_app(app)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from ferstore_app.models import tbl_employee

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping("test_config")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from ferstore_app.views.api_documentation import blueprint_api_documentation

    app.register_blueprint(blueprint_api_documentation, url_prefix="")

    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    from ferstore_app.resources.resource_authorization import (
        blueprint_api_authorization_employee,
    )

    return app
