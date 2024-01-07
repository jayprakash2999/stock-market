from unittest.mock import patch
from unittest import TestCase

from app import app
from fastapi.testclient import TestClient

from responses.company_details import company_details

client = TestClient(app)

url = '/company-detail/ABC'


class TestDetails(TestCase):

    def test_success(self):
        with patch('app.company_details') as mock_company_details:
            mock_company_details.return_value = company_details
            company_data = client.get(url)
            self.assertEqual(company_data.status_code, 200)

