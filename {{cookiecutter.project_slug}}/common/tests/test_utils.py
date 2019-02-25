from unittest.mock import patch
from common.utils import GooglePlacesClient


class TestGooglePlacesClient:
    """Test suite for GooglePlacesClient"""

    def test_geocode(self):
        """Test the geocode function by mocking out the actual request."""

        client = GooglePlacesClient("")
        with patch("requests.get") as mock:
            mock.return_value.json.return_value = {"status": "ok"}
            response = client.geocode(address="testing")
            assert response == {"status": "ok"}

    def test_rgeocode(self):
        """Test the rgeocode function by mocking out the actual request."""

        client = GooglePlacesClient("")
        with patch("requests.get") as mock:
            mock.return_value.json.return_value = {"status": "ok"}
            response = client.rgeocode(lat=-28, lon=26)
            assert response == {"status": "ok"}

    def test_places(self):
        """Test the places function by mocking out the actual request."""

        client = GooglePlacesClient("")
        with patch("requests.get") as mock:
            mock.return_value.json.return_value = {"status": "ok"}
            response = client.places(query="testing")
            assert response == {"status": "ok"}
