from typing import Dict

import requests


class GooglePlacesClient:
    """Requests wrapper on certain APIs available through Google."""

    GEOCODE_API = "https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    RGEOCODE_API = "https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={API_KEY}"
    PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={API_KEY}"

    def __init__(self, API_KEY: str) -> None:
        self.API_KEY = API_KEY

    def _build_url(self, base_url: str, **kwargs) -> str:
        """Build the specified url."""

        return base_url.format(API_KEY=self.API_KEY, **kwargs)

    def _make_request(self, url: str) -> Dict:
        """Helper function to make the request to the API."""

        response = requests.get(url)
        response.raise_for_status()

        return response.json()

    def geocode(self, address: str) -> Dict:
        """Geocode the provided address using the Google Places API."""

        url = self._build_url(GooglePlacesClient.GEOCODE_API, address=address)
        return self._make_request(url=url)

    def rgeocode(self, lat: float, lon: float) -> Dict:
        """Reverse geocode the provided latitude and longitude using the Google Places API."""

        url = self._build_url(GooglePlacesClient.RGEOCODE_API, lat=lat, lon=lon)
        return self._make_request(url=url)

    def places(self, query: str) -> Dict:
        """Search for places using the Google Places API."""

        url = self._build_url(GooglePlacesClient.PLACES_API_URL, query=query)
        return self._make_request(url=url)
