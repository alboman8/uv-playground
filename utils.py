import logging

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


class ColorFormatter(logging.Formatter):
    COLORS = {logging.INFO: GREEN, logging.ERROR: RED}

    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelno, RESET)
        return f"{color}{super().format(record)}{RESET}"


def get_logger(name: str) -> logging.Logger:
    handler = logging.StreamHandler()
    handler.setFormatter(ColorFormatter("%(levelname)s:%(name)s:%(message)s"))
    logging.basicConfig(level=logging.INFO, handlers=[handler])
    return logging.getLogger(name)
