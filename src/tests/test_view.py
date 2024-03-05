import unittest
from app import create_app, db
from app.models.items import Item
from config import Config
from datetime import datetime


# again for the sake of simplicity
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class SearchViewTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

        item = Item(
            title="Test Item", url="http://example.com", date_added=datetime.now()
        )
        db.session.add(item)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_search_title(self):
        response = self.client.get("/search?title=Test")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Test Item" in str(data))

    def test_search_url(self):
        response = self.client.get("/search?url=example.com")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue("http://example.com" in str(data))

    def test_date_range_search(self):
        response = self.client.get("/search?date_start=2021-01-01&date_end=2021-12-31")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
