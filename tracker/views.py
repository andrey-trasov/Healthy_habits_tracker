from django.shortcuts import render

from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from tracker.models import Habit
from tracker.paginators import CustomPagination
from tracker.permissions import IsOwner
from tracker.serializers import HabitSerializer


class HabitCreateApiView(CreateAPIView):   #Создание привычки.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HabitListApiView(ListAPIView):   #Список привычек текущего пользователя с пагинацией.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class PublicHabitListApiView(ListAPIView):   #Список публичных привычек.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # pagination_class = CustomPagination

    def get_queryset(self):
        return self.queryset.filter(is_public=True)

class HabitRetrieveApiView(RetrieveAPIView):   #детальный просмотр привычки
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)

class HabitUpdateApiView(UpdateAPIView):   #Редактирование привычки.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)

class HabitDestroyApiView(DestroyAPIView):   #Удаление привычки.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)