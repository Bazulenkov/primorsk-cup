import datetime as dt

from django.contrib.auth import get_user_model

User = get_user_model()


def year(request):
    """
    Добавляет переменную с текущим годом.
    """
    year_now = dt.datetime.now().date().year
    return {"year": year_now}


def participants_count(request):
    """Выводит общее кол-во участников."""
    count = User.objects.all().count()
    return {"participants_count": count}
