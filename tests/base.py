# tests/base.py


from flask.ext.testing import TestCase

from tcmgmt import app, db
from tcmgmt.models import User


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('tcmgmt.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        user = User(email="ad@min.com", password="admin_user")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
