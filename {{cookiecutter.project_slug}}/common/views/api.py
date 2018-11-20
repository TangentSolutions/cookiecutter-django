from typing import Dict
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class APIRootBaseView(APIView):
    """Base class for an API root view."""

    @staticmethod
    def get_routes(request: Request) -> Dict:
        """Generate a dict of routes for a given package."""

        raise NotImplementedError(
            f"method 'get_routes' not implemented for APIRootView"
        )

    def get(self, request: Request) -> Response:
        """Provides the routes available under the users module.

        Returns:
            A DRF response containing hyperlinks to the available routes.
        """

        return Response(self.get_routes(request))
