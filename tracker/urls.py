from django.urls import path

from tracker.apps import TrackerConfig
from tracker.views import HabitCreateApiView, HabitListApiView, PublicHabitListApiView, HabitRetrieveApiView, \
    HabitUpdateApiView, HabitDestroyApiView

app_name = TrackerConfig.name

urlpatterns = [
    path("habit/", HabitListApiView.as_view(), name="habit"),
    path("habit_public/", PublicHabitListApiView.as_view(), name="habit_public"),
    path("habit_create/", HabitCreateApiView.as_view(), name="habit_create"),
    path("habit/<int:pk>/", HabitRetrieveApiView.as_view(), name="habit_detail"),
    path("habit_update/<int:pk>/", HabitUpdateApiView.as_view(), name="habit_update"),
    path("habit_delete/<int:pk>/", HabitDestroyApiView.as_view(), name="habit_delete"),
]
