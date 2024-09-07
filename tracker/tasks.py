from datetime import datetime
from datetime import timedelta

import requests
from pytz import timezone
from celery import shared_task
from myproject import settings
from tracker.models import Habit


@shared_task
def sending_notifications():

    time_zone = timezone(settings.TIME_ZONE)
    current_date = datetime.now(time_zone)
    habits = Habit.objects.filter(is_active=True)
    for habit in habits:
        if habit.next_time_to_do <= current_date:
            habit.next_time_to_do = current_date + timedelta(days=habit.periodicity)
            habit.save()

            params = {
                "text": f"Пришло время выполнить {habit.action}",
                "chat_id": habit.owner.telegram_chat_id,
            }
            requests.get(
                f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage",
                params=params,
            )
