# Códigos de exemplo de como fazer a utilização do logger.

from loguru import logger

#  Os códigos estão por níveis. (Decrescente)

logger.debug("Um aviso para um dev (ou eu mesmo) no futuro.")   # Só irei ver quando eu estiver debugando.
logger.info("Informação do fluxo de código.")   # Print do Python.
logger.warning("Algo no futuro irá parar de funcionar.")    # Warning (A vida é muito curta para ler warning),
logger.error("Aconteceu uma falha")     # Uma falha inesperada, algo que deu errado.
logger.critical("Aconteceu uma falha que aborta o código.")     # Aborta todo código, esse é para olhar o vermelho e tirar alguns minutos para descansar(chorar).