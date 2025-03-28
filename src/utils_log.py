# Principal objetivo dessa camada é: ALterar configurações de logging. Exemplo: Posso alterar qual logging irá aparecer no meu terminal, Posso alterar qual logging eu irei salvar do meu fluxo de código.

from loguru import logger
from sys import stderr
from functools import wraps

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="INFO"
)

def log_decorator(func):  # Recebe uma função e decora ela.
    @wraps(func)        # Essa linha de código nos garante que, a função recebida não perca suas características originais.
    def wrapper(*args, **kwargs):       # **Args e **Kwargs, aqui ela recebe todos argumentos (parâmetros) que o usúario passa na função recebida.
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)      # Aqui executamos a função que foi recebida normalmente.
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:      # Se caso der alguma excessão (falha), nos jogará essa informação
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada
    return wrapper