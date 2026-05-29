import logging


class FileHandler(logging.FileHandler):
    def __init__(self, path):
        super().__init__(path, encoding="utf-8")
        self.setLevel(logging.INFO)


fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

file_handler = FileHandler("app.log")
file_handler.setFormatter(fmt)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(fmt)

# root logger must be at DEBUG so records reach handlers;
# each handler then applies its own level filter
logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, stream_handler])

logger = logging.getLogger(__name__)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
