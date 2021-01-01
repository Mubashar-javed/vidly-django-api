from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        new_user = User.objects.get(username=user)
        token['_id'] = token['user_id']
        token['name'] = new_user.username
        token['email'] = new_user.email
        token['isAdmin'] = new_user.is_superuser
        return token
