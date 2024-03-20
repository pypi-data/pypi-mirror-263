"""Genera un log en el sistema"""
import json

from django.db.transaction import non_atomic_requests

from exedoc_extranet.models import LogSistema
import logging


# noinspection PyBroadException
@non_atomic_requests
def set_log_sistema(
    view: str, 
    method: str, 
    function: str, 
    log: str, 
    params: dict = None, 
    type_log: str = 'ERROR', 
    trace: str = None, 
    stack: str = None
):
    """Genera un log en el sistema"""
    logger = logging.getLogger('seim.log.sistema')
    try:
        json_params = json.dumps(params, indent=4, sort_keys=True, default=str)
    except Exception as exception:
        logger.debug(vars(exception))
        json_params = None
    
    if type_log is LogSistema.DEBUG:
        logger.debug(f"{view}.{function}.{method} -> {log}", extra={'params': json_params})
    elif type_log is LogSistema.INFO:
        logger.info(f"{view}.{function}.{method} -> {log}", extra={'params': json_params})
    elif type_log is LogSistema.WARNING:
        logger.warning(f"{view}.{function}.{method} -> {log}", extra={'params': json_params})
    elif type_log is LogSistema.ERROR:
        logger.error(
            f"{view}.{function}.{method} -> {log}", 
            extra={'params': json_params, 'trace': trace, 'stack': stack}
        )

    try:
        LogSistema.objects.create(
            view=view,
            method=method,
            function=function,
            log=log,
            params=json.loads(json_params),
            usuario_ingreso_id=LogSistema.UsuarioLogin,
            usuario_ingreso_token="",
            tipo_registro=type_log,
            trace=trace,
            stack=stack
        )
    except Exception as exception:
        pass

