from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

import graphene


# Custom user model
User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User


class QueryType(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()


schema = graphene.Schema(query=QueryType, auto_camelcase=False)
