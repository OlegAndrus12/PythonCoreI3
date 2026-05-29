from pydantic import BaseModel, model_validator, ValidationError
from datetime import date


# mode='before' runs before field-level validation, receives raw input dict
# mode='after'  runs after all fields are already validated instances

class DateRange(BaseModel):
    start: date
    end: date

    @model_validator(mode="after")
    def check_end_after_start(self):
        if self.end <= self.start:
            raise ValueError("end must be after start")
        return self

try:
    DateRange(start="2024-01-10", end="2024-01-05")
except ValidationError as e:
    print(e)

dr = DateRange(start="2024-01-01", end="2024-12-31")
print(dr)


# mode='before' — normalize raw data before Pydantic parses it
class User(BaseModel):
    name: str
    email: str

    @model_validator(mode="before")
    @classmethod
    def strip_whitespace(cls, data):
        # data is a raw dict here
        return {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}


u = User(name="  Alice  ", email="  alice@example.com  ")
print(repr(u.name))   # 'Alice'
print(repr(u.email))  # 'alice@example.com'


# cross-field dependency: password confirmation
class SignupForm(BaseModel):
    username: str
    password: str
    password_confirm: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.password_confirm:
            raise ValueError("passwords do not match")
        return self

try:
    SignupForm(username="bob", password="secret", password_confirm="wrong")
except ValidationError as e:
    print(e)

form = SignupForm(username="bob", password="secret", password_confirm="secret")
print(form)
