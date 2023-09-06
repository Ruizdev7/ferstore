import os
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()


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

    from ferstore_app.models import tbl_customer
    from ferstore_app.models import tbl_type_id
    from ferstore_app.models import tbl_auto_perceived_gender

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping("test_config")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
