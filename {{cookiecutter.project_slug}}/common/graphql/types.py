import graphene


class PermissionsDict(graphene.ObjectType):
    read = graphene.Boolean(required=True)
    write = graphene.Boolean(required=True)
