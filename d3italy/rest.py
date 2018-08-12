from flask import Blueprint, jsonify
from flask_restful import Resource

from . import models
from  . import schemas


class City(Resource):
    def get(self, id):
        schema = schemas.CitySchema()
        item = models.City.query.filter_by(id=id).first()
        return schema.dump(item)


class CityName(Resource):
    def get(self, name):
        schema = schemas.CityNameSchema()
        item = models.City.query.filter_by(name=name).first()
        return schema.dump(item)


class Region(Resource):
    def get(self, id):
        schema = schemas.RegionSchema()
        item = models.Region.query.filter_by(id=id).first()
        return schema.dump(item)


class RegionName(Resource):
    def get(self, name):
        schema = schemas.RegionNameSchema()
        item = models.Region.query.filter_by(name=name).first()
        return schema.dump(item)