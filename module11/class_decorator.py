def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class DatabaseConnection:
    def __init__(self, url):
        self.url = url
        print(f"Connecting to {url}...")

    def __repr__(self):
        return f"DatabaseConnection({self.url!r})"


@singleton
class AppConfig:
    def __init__(self, env, debug=False):
        self.env = env
        self.debug = debug

    def __repr__(self):
        return f"AppConfig(env={self.env!r}, debug={self.debug})"


# "Connecting to..." prints only once — second call returns the same instance
db1 = DatabaseConnection("postgresql://localhost/mydb")
db2 = DatabaseConnection("postgresql://localhost/mydb")

print(db1 is db2)   # True — same object
print(db1)

cfg1 = AppConfig("production", debug=False)
cfg2 = AppConfig("production", debug=False)

print(cfg1 is cfg2)  # True
print(cfg1)
