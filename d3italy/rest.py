from flask import Blueprint, jsonify
from flask_restful import Resource, reqparse
from webargs.flaskparser import use_args

from . import models
from  . import schemas


class CityId(Resource):
    def get(self, id):
        schema = schemas.CitySchema()
        item = models.City.query.filter_by(id=id).first()
        return schema.dump(item)


class City(Resource):
    @use_args(schemas.CitySchema())
    def get(self, args):
        schema = schemas.CitySchema()
        item = models.City.query.filter_by(**args).all()
        return schema.dump(item, many=True)


class RegionId(Resource):
    def get(self, id):
        schema = schemas.RegionSchema()
        item = models.Region.query.filter_by(id=id).first()
        return schema.dump(item)


class Region(Resource):
    @use_args(schemas.RegionSchema())
    def get(self, args):
        schema = schemas.RegionSchema()
        item = models.Region.query.filter_by(**args).all()
        return schema.dump(item, many=True)