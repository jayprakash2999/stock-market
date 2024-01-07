from unittest.mock import patch
from unittest import TestCase

from app import app
from fastapi.testclient import TestClient
from responses.related_symbols import related_symbols

client = TestClient(app)

url = '/related_symbols/AB'


class TestDetails(TestCase):

    def test_success(self):
        with patch('app.get_related_symbols') as mock_get_related_symbols:
            mock_get_related_symbols.return_value = related_symbols
            related_symbols_data = client.get(url)
            self.assertEqual(related_symbols_data.status_code, 200)