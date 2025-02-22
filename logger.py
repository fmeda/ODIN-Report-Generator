import logging

logger = logging.getLogger("odin_report_generator")
logger.setLevel(logging.INFO)

# Handler para logs no console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Função para registrar erros
def log_error(message):
    logger.error(message)

# Função para registrar informações
def log_info(message):
    logger.info(message)
