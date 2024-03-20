from datetime import datetime
from typing import Optional

import numpy
from pytz import timezone

from models.feriado import Feriado
from config import settings

cl = timezone(settings.TIME_ZONE)
utc = timezone('UTC')


def get_business_due_date_from_today(offset: int, tzinfo=utc) -> datetime:
    """Get the business day from today by a given number"""
    offset = 0 if offset is None else offset
    today = datetime.now(cl).astimezone(tzinfo)
    return get_business_due_date_from_date(today, offset, tzinfo)


def get_business_due_date_from_date(today: Optional[datetime], offset: int, tzinfo=utc) -> Optional[datetime]:
    """Get the business day from a date by a given number"""
    if today is None:
        return None
    last_year = int(datetime.now(cl).strftime('%Y')) - 1
    next_year = int(datetime.now(cl).strftime('%Y')) + 1
    holidays = Feriado.objects.filter(fecha__year__gte=last_year, fecha__year__lte=next_year)
    holidays = [holiday.fecha.strftime('%Y-%m-%d') for holiday in holidays]
    due_date = numpy.busday_offset(today.date(), offset, holidays=holidays, weekmask='Mon Tue Wed Thu Fri', roll='forward').astype(datetime)
    return datetime(int(due_date.strftime('%Y')),
                    int(due_date.strftime('%m')),
                    int(due_date.strftime('%d')),
                    today.hour,
                    today.minute,
                    tzinfo=today.tzinfo).astimezone(tzinfo)
