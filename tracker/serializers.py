from rest_framework.serializers import ModelSerializer

from tracker.models import Habit
from tracker.validators import RewardValidator, CompleteTimeValidator, ChecRrelation_habitValidator, \
    ChecPleasantValidator, ChecPeriodicityValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [RewardValidator(field1='relation_habit', field2='reward'),
                      CompleteTimeValidator(field='duration'),
                      ChecRrelation_habitValidator(field="relation_habit"),
                      ChecPleasantValidator(field1='is_pleasant', field2='reward', field3='relation_habit'),
                      ChecPeriodicityValidator(field='periodicity'),
                      ]

