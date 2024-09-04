from rest_framework.serializers import ModelSerializer

from tracker.models import Habit
from tracker.validators import RewardValidator, CompleteTimeValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [RewardValidator(field1='relation_habit', field2='reward'), CompleteTimeValidator(field='duration')]