# MRO (Method Resolution Order) — the order Python searches for a method
# in multiple inheritance. Python uses C3 linearization (left-to-right, depth-first).
#
#         object
#        /      \
#   LogMixin  AuthMixin
#        \      /
#        APIView

class LogMixin:
    def log(self, message):
        print(f"[LOG] {self.__class__.__name__}: {message}")


class AuthMixin:
    def check_auth(self, token):
        return token == "secret"


class APIView(LogMixin, AuthMixin):
    def handle(self, token, data):
        if not self.check_auth(token):
            self.log("Unauthorized request")
            return {"error": "Unauthorized"}
        self.log("Request processed")
        return {"data": data}


print(APIView.__mro__)

view = APIView()
print(view.handle("secret", {"id": 1}))
print(view.handle("wrong", {}))