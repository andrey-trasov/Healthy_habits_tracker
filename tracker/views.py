from django.shortcuts import render

from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)

from tracker.models import Habit
from tracker.serializers import HabitSerializer


class HabitCreateApiView(CreateAPIView):   #Создание привычки.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HabitListApiView(ListAPIView):   #Список привычек текущего пользователя с пагинацией.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class PublicHabitListApiView(ListAPIView):   #Список публичных привычек.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        return self.queryset.filter(is_public=True)

class HabitRetrieveApiView(RetrieveAPIView):   #детальный просмотр привычки
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class HabitUpdateApiView(UpdateAPIView):   #Редактирование привычки.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class HabitDestroyApiView(DestroyAPIView):   #Удаление привычки.
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer