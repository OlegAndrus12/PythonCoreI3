class BaseLogger:
    def log(self, message):
        print(f"[LOG] {message}")


class FileLogger(BaseLogger):
    def __init__(self, path):
        self.path = path

    def log(self, message):
        print(f"[FILE:{self.path}] {message}")


class SilentLogger(BaseLogger):
    def log(self, message):
        pass  # suppresses all output


loggers = [BaseLogger(), FileLogger("/var/log/app.log"), SilentLogger()]
for logger in loggers:
    logger.log("server started")
