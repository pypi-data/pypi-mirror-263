from exedoc_extranet.config.settings import LOG_SEIM_LEVEL
import logging

class SeimLogSistema:
    
    def __init__(self, view, method, function):
        self.view: str = view
        self.method: str = method
        self.function: str = function
        self.old_function: str = function
        self.params: dict = {}
        self.log: str = 'OK'
        self.type_log: str = 'ERROR'
        self.trace: str = ''
        self.stack: str = ''
        self.logger: logging.Logger = logging.getLogger('seim.log.sistema')
        self.logger.debug(f"**INICIO - {function}** -> \n{view}.{function}({method})")
            

    def set_function_name(self, new_name):
        self.logger.debug(f'Call {new_name} from {self.function}')
        self.old_function = self.function
        self.function = new_name

    def reset_function_name(self):
        self.logger.debug(f"return to {self.old_function} from {self.function}")
        self.function = self.old_function

    def to_dict(self) -> dict:
        return {
            'view': self.view,
            'method': self.method,
            'function': self.function,
            'log': self.log,
            'params': self.params,
            'type_log': self.type_log,
            'trace': self.trace,
            'stack': self.stack
        }
    
    def add_params(self, atributo, valor):
        self.logger.debug(f"{self.view}.{self.function}.{atributo}->{valor}")
        self.params.update(
            {
                atributo: valor
            }
        )
        return self
    
    def set_log_message(self, valor):
        self.log = valor
        return self
    
    def set_type_log(self, valor):
        from exedoc_extranet.models import LogSistema
        if valor not in LogSistema.TIPOS:
            valor = LogSistema.ERROR
        self.type_log = valor
        return self
    
    def set_traceback(self, trace, stack):
        self.logger.debug(f"{self.view}.{self.function}.trace->{trace}")
        self.logger.debug(f"{self.view}.{self.function}.stack->{stack}")
        self.trace = trace
        self.stack = stack
        return self
    
    def warning(self, log):
        from exedoc_extranet.models import LogSistema
        self.__save_with_log_and_type(LogSistema.WARNING, log)
    
    def debug(self, log):
        from exedoc_extranet.models import LogSistema
        if LOG_SEIM_LEVEL == 'DEBUG':
            self.__save_with_log_and_type(LogSistema.DEBUG, log)
    
    def error(self, log):
        from exedoc_extranet.models import LogSistema
        self.__save_with_log_and_type(LogSistema.ERROR, log)
    
    def info(self, log):
        from exedoc_extranet.models import LogSistema
        self.__save_with_log_and_type(LogSistema.INFO, log)
    
    def __save_with_log_and_type(self, type_log, log):
        self.type_log = type_log
        self.log = log
        self.save()
    
    def save(self):
        from exedoc_extranet.services import set_log_sistema
        set_log_sistema(
            view=self.view, 
            method=self.method, 
            function=self.function, 
            log=self.log, 
            params=self.params, 
            type_log=self.type_log, 
            trace=self.trace, 
            stack=self.stack
        )
