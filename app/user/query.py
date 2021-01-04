import graphene
from graphql import GraphQLError
from graphene_django_extras import DjangoObjectField, DjangoListObjectField
from django_graphene_permissions import permissions_checker
from .models import User, Token
from .permissions import IsAuthenticated
from .types import UserType,  UserListType, VerifyTokenOutputType


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
    user_list = DjangoListObjectField(
        UserListType, description="User List Query")
    verify_register_token = graphene.Field(
        VerifyTokenOutputType, token=graphene.String(required=True))

    @permissions_checker([IsAuthenticated])
    def resolve_users(self, info):
        return User.objects.all()

    @permissions_checker([IsAuthenticated])
    def resolve_me(self, info):
        return info.context.user

    def resolve_verify_register_token(self, info, token=None):
        if token is not None:
            user_token = Token.objects.filter(token=token).first()
            if user_token:
                return {
                    'email': user_token.new_user_email is None and user_token.user or user_token.new_user_email,
                    'is_valid': True
                }
            return {'email': None, 'is_valid': False}
        raise GraphQLError('invalid token')



