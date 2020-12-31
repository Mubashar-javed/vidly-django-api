from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        new_user = User.objects.filter(username=user).first()
        token['_id'] = new_user.pk
        token['name'] = new_user.username
        token['email'] = new_user.email
        token['isAdmin'] = new_user.is_superuser
        return token
