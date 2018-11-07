from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

import accounts.serializers
import accounts.permissions


# Custom user model
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """Read only viewset for the user model.
    
    Write operations are provided through custom actions.
    """

    queryset = User.objects.all()
    serializer_class = accounts.serializers.UserSerializer
    permission_classes = (IsAdminUser,)

    @action(
        detail=False,
        methods=['GET'],
        url_name='me',
        url_path='me',
        permission_classes=(
            IsAuthenticated & accounts.permissions.RequestUserIsInstanceUser,
        ),
    )
    def me(self, request: Request) -> Response:
        """Return the user instance for the request user.

        Returns:
            A single user instance belonging to the request user.
        """

        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['POST'],
        url_name='check-username-availability',
        url_path='check-username-availability',
        serializer_class=accounts.serializers.UsernameAvailabilitySerializer,
        permission_classes=(AllowAny,),
    )
    def check_availability(self, request: Request) -> Response:
        """Check if the requested username is available.
        
        Returns:
            A DRF response containing the username and a boolean indicating
            whether it is available or not.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        response = {
            'username': username,
            'available': User.objects.filter(username=username).exists() is False,
        }

        return Response(response)
