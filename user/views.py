from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Интпоинт для регистрации пользователя
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)  # открываем для анонимных пользователей

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)  # сохраняяем пользователя активным
        user.set_password(user.password)  # хэшируем пароль
        user.save()

# Правда чтобы не делать два запроса в базу данных (происходит на каждый save), можно было сделать так:
#
# def perform_create(self, serializer):
#     user = serializer.save(commit=False)
#     user.set_password(user.password)
#     user.save()
#
# Причем статус активности ставить не нужно - пользователь дефолтно создается активным
