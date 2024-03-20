from datetime import timedelta, datetime

from django.db import models
from pytz import timezone

from exedoc_extranet.config import settings


def date_to_str_local(fecha: models.DateTimeField or datetime, strftime='%Y-%m-%dT%H:%M:%SZ') -> str:
    """De vuelve las horas UTC en zona horaria de chile"""
    if fecha is None or isinstance(fecha, int):
        return ""
    local_timezone = timezone(settings.TIME_ZONE)
    loc_dt = fecha.astimezone(local_timezone)
    return loc_dt.strftime(strftime)


def date_to_long_str_local(fecha: models.DateTimeField or datetime) -> str:
    """Devuelve la fecha con formato expandido chile sin hora"""
    if fecha is None:
        return ""
    _months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    cl = timezone(settings.TIME_ZONE)
    loc_dt = fecha.astimezone(cl)
    return f"{loc_dt.day} de {_months[loc_dt.month - 1]} de {loc_dt.year}"


def date_to_str_utc(fecha: models.DateTimeField or datetime) -> str:
    """Devuelve fecha con hora local a forma UTC"""
    if fecha is None:
        return ""
    loc_dt = fecha.astimezone(timezone('UTC'))
    return loc_dt.strftime('%Y-%m-%dT%H:%M:%S%z')


def now_to_isodate() -> str:
    """FORMATO ISO 8601 FECHA"""
    local_timezone = timezone(settings.TIME_ZONE)
    fecha = datetime.now().replace(microsecond=0)
    fecha_corrida = fecha.astimezone(local_timezone) + timedelta(minutes=5)
    return fecha_corrida.isoformat()
