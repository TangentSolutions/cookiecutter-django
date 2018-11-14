from rest_framework import serializers
from django.contrib.auth import get_user_model
from common.rest_framework.fields import LuhnField


# Custom user model
User = get_user_model()


class UsernameAvailabilitySerializer(serializers.Serializer):
    """Serializer class for the check username availability custom action."""

    username = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    """Django user model serializer."""

    url = serializers.HyperlinkedIdentityField("accounts-api:user-detail")
    id_number = LuhnField(min_length=13, required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "id_number",
            "email",
            "url",
        )
