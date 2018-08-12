import os
import unittest

from .. import create_app, db

TEST_DB = '/tmp/d3italy-test.db'

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['DEBUG'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + TEST_DB
        self.app.config['SQLALCHEMY_ECHO'] = False
        with self.app.app_context():
            db.drop_all()
            db.create_all()


    # def tearDown(self):
    #     pass

class ModelTests(BasicTests):
    def test_model(self):
        from d3italy import models
        region = models.Region(name='test_region')
        city = models.City(name='test_city', region=region)
        with self.app.app_context():
            db.session.add(region, city)
            db.session.commit()
            city_q = models.City.query.filter_by(id=1).first()
            self.assertEquals(city_q.name, 'test_city')
            self.assertEquals(city_q.region.name, 'test_region')


class APITests(BasicTests):
    def test_api(self):
        from d3italy import models
        region = models.Region(name='test_region')
        city = models.City(name='test_city', region=region)
        with self.app.app_context():
            db.session.add(region, city)
            db.session.commit()

        client = self.app.test_client()
        resp = client.get('/api/city/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json['name'], 'test_city')


if __name__ == "__main__":
    unittest.main()