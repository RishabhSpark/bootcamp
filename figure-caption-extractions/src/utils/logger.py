import logging
import os
# def get_logger(name: str = __name__, level: str = "info") -> logging.Logger:
#     logger = logging.getLogger(name)
#     if not logger.hasHandlers():
#         handler = logging.StreamHandler()
#         formatter = logging.Formatter(
#             '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
#         )
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)
#         log_level = getattr(logging, level.upper(), logging.INFO)
#         logger.setLevel(log_level)
#     return logger


def get_logger(name: str = __name__, level: str = "info", log_to_file: bool = False, log_file_path: str = "logs/app.log") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        # Console handler
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # File handler
        if log_to_file:
            os.makedirs(os.path.dirname(log_file_path), exist_ok=True)  # Ensure log dir exists
            file_handler = logging.FileHandler(log_file_path, mode='a')  # Append mode
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        log_level = getattr(logging, level.upper(), logging.INFO)
        logger.setLevel(log_level)
    return logger