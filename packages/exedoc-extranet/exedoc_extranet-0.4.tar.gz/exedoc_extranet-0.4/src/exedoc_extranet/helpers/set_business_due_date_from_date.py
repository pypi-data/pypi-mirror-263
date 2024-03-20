from datetime import timedelta, datetime
from typing import Optional
from exedoc_extranet.config import settings
from exedoc_extranet.models import TiemposProyecto

from . import get_business_due_date_from_date

def set_business_due_date_from_date(initial_date: datetime, offset: int, type_offset: str) -> Optional[datetime]:
    """Set the business day from a date by a given number"""
    if initial_date is None:
        return None
    last_offset = 0
    in_bussday: int = int(settings.INICIO_HORAS_HABILES)
    out_bussday: int = int(settings.TERMINO_HORAS_HABILES)
    business_hours: int = 24

    if type_offset == TiemposProyecto.MINUTOS:
        initial_date = initial_date + timedelta(minutes=offset)

    elif type_offset == TiemposProyecto.HORAS_CORRIDAS:
        initial_date = initial_date + timedelta(hours=offset)

    elif type_offset == TiemposProyecto.HORAS_HABILES:
        # Se calculan los días hábiles de las horas solicitadas
        days = int(offset / business_hours)
        # Se calcula el remanente de horas que pudieran quedar del cálculo anterior
        hours = 0 if days == offset / business_hours else offset - int(days * business_hours)
        # Si el día origen es viernes, se agregan 2 días
        if initial_date.isoweekday() == 5:
            days += 2
        # Se agregan los días calculados
        initial_date = initial_date + timedelta(days=days)
        # Se fija la hora en el inicio del día hábil
        initial_date = initial_date.replace(hour=out_bussday, minute=0, second=0, microsecond=0)
        # Se suma el remanente de horas calculado
        initial_date = initial_date + timedelta(hours=hours)

    elif type_offset == TiemposProyecto.DIAS_CORRIDOS:
        initial_date = initial_date + timedelta(days=offset)

    elif type_offset == TiemposProyecto.DIAS_HABILES:
        last_offset = offset
        if initial_date.hour < in_bussday:
            initial_date = initial_date.replace(hour=in_bussday, minute=0, second=0, microsecond=0)
        elif initial_date.hour > out_bussday:
            last_offset += 1

    return get_business_due_date_from_date(initial_date, last_offset)