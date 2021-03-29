"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

# Models
from users.models import User

# Serializers
from users.serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer
from users.utils import Util


class UserViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    filter_backends = (SearchFilter,)
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    search_fields = (
        'name',
        'gender',
        'username',
        'email',
    )

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data

        email_body = f'Hi {user.name}. Welcome to Be TECH CAPITAL!'

        data_mail = {'email_to': user.email, 'email_subject': 'I want to work in beTech Capital!',
                     'email_body': email_body}
        data_whatsapp = {'phone': user.phone, 'message': email_body}
        Util.send_email(data_mail)
        Util.send_whatsapp(data_whatsapp)

        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = User.objects.get_queryset()
        return queryset
