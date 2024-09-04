from datetime import timedelta

from rest_framework.serializers import ValidationError


class RewardValidator:
   def __init__(self, field1, field2):
       self.field1 = field1
       self.field2 = field2


   def __call__(self, value):
       relation_habit = dict(value).get(self.field1)
       reward = dict(value).get(self.field2)
       if relation_habit and reward:
            raise ValidationError("Одновеременное заполнение полей 'Вознаграждение' и 'Связанная привычка' запрещена!")

class CompleteTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field) > timedelta(seconds=120):
            raise ValidationError("Время выполнения привычки не может быть больше 2-х минут!")

