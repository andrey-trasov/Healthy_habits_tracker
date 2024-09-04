from datetime import timedelta

from django.db import models

from user.models import User

class Habit(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="название привычки"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="создатель привычки",
        blank=True,
        null=True,
    )
    place = models.CharField(
        max_length=100,
        verbose_name="место выполнения действия",
    )
    action = models.CharField(
        max_length=255,
        verbose_name="действие",
        blank=True,
        null=True,
    )
    first_time_to_do = models.DateTimeField(
        verbose_name="дата первого выполнения привычки"
    )
    next_time_to_do = models.DateTimeField(
        verbose_name="дата следующего выполнения привычки",
        blank=True,
        null=True,
    )
    reward = models.CharField(    #только для полезных привычек
        max_length=100,
        verbose_name="вознаграждение за выполнение привычки",
        blank=True,
        null=True,
    )
    relation_habit = models.ForeignKey(    #указываем приятную привычку для полезной привычки
        "tracker.Habit",
        on_delete=models.SET_NULL,
        verbose_name="связующая привычка",
        blank=True,
        null=True,
    )
    is_pleasant = models.BooleanField(    #  True для приятной привычки
        default=False,
        blank=True,
        null=True,
        verbose_name="приятность привычки"
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="периодичность в днях",
        blank=True,
        null=True,
    )
    duration = models.CharField(
        max_length=50,
        default=timedelta(minutes=2),
        verbose_name="время требующееся на выполнение действия",
        blank=True,
    )
    is_public = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="доступность другим пользователям"
    )
    is_active = models.BooleanField(
        default=True,
        blank=True,
        verbose_name="активность привычки(влияет на отправку уведомлений пользователю)"
    )

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"

    def __str__(self):
        return {self.name}
