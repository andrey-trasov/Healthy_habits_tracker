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
            raise ValidationError(
                "Одновеременное заполнение полей 'Вознаграждение' и 'Связанная привычка' запрещена!"
            )


class CompleteTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field) > timedelta(seconds=120):
            raise ValidationError(
                "Время выполнения привычки не может быть больше 2-х минут!"
            )


class ChecRrelation_habitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        relation_habit = dict(value).get(self.field)
        if relation_habit:
            if not relation_habit.is_pleasant:
                raise ValidationError(
                    "В связанные привычки могут попадать только привычки с признаком приятной привычки!"
                )


class ChecPleasantValidator:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        is_pleasant = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        relation_habit = dict(value).get(self.field3)
        if is_pleasant:
            if reward or relation_habit:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки!"
                )


class ChecPeriodicityValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field) > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней!")
