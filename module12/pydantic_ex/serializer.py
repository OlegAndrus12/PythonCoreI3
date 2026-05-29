from pydantic import BaseModel, field_serializer
from datetime import date, datetime


# field_serializer lets you control how a field is serialized
# without changing how it is stored or validated

class Event(BaseModel):
    name: str
    date: date
    price_usd: float

    @field_serializer("date")
    def serialize_date(self, value):
        return value.strftime("%d %b %Y")  # e.g. "01 Jan 2024"

    @field_serializer("price_usd")
    def serialize_price(self, value):
        return f"${value:,.2f}"


e = Event(name="PyCon", date="2024-05-15", price_usd=299.0)
print(e.model_dump())        # date and price are custom-formatted strings
print(e.model_dump_json())

# The raw Python attribute is still a date / float
print(type(e.date))          # <class 'datetime.date'>
print(type(e.price_usd))     # <class 'float'>


# mode='plain' replaces default serialization entirely (used above by default)
# mode='wrap'  gives you the default serializer to call or skip
class Log(BaseModel):
    created_at: datetime

    @field_serializer("created_at", mode="wrap")
    def as_iso(self, value, handler):
        # call default, then uppercase it (contrived example)
        return handler(value).replace("T", " ")

log = Log(created_at="2024-03-10T14:30:00")
print(log.model_dump())
