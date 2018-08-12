import click
import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()
ma = Marshmallow()

from .models import *


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_envvar('APP_CONFIG')
        # SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile(os.environ['APP_CONFIG'], silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    ma.init_app(app)


    from . import italy
    app.register_blueprint(italy.bp)
    app.add_url_rule('/', endpoint='index')

    from . import rest
    api = Api(app)
    api.add_resource(rest.City, '/api/city/name/<string:name>')
    api.add_resource(rest.CityId, '/api/city/id/<int:id>')
    api.add_resource(rest.Region, '/api/region/name/<string:name>')
    api.add_resource(rest.RegionId, '/api/region/id/<int:id>')

    @app.cli.command()
    def init_db():
        '''Initializes database.'''
        db.drop_all()
        db.create_all()
        db.session.commit()

    @app.cli.command()
    def populate_db():
        '''Populates the database with default data.'''
        from . import models
        region = models.Region(name='test_region')
        city = models.City(name='test_city', region=region)
        db.session.add(region, city)
        db.session.commit()

    return app
