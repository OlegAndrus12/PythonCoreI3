from pydantic import BaseModel, ConfigDict


# model_copy returns a new instance with selected fields overridden
# it's the safe way to do partial updates without mutating the original

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    age: int
    address: Address

u1 = User(name="Alice", age=30, address=Address(city="Kyiv", country="Ukraine"))

# shallow copy — nested objects are shared by reference
u2 = u1.model_copy(update={"age": 31})
print(u1)
print(u2)
print(u1 is u2)             # False — different top-level instances
print(u1.address is u2.address)  # True — same nested Address object

# deep copy — nested objects are also duplicated
u3 = u1.model_copy(update={"address": u1.address.model_copy(update={"city": "Lviv"})})
print(u3)
print(u1.address.city)      # Kyiv — original unchanged


# frozen=True makes instances immutable (like a dataclass frozen=True)
class Point(BaseModel):
    model_config = ConfigDict(frozen=True)

    x: float
    y: float

p = Point(x=1.0, y=2.0)

try:
    p.x = 99  # raises ValidationError
except Exception as e:
    print(e)

# to "change" a frozen model, create a new one via model_copy
p2 = p.model_copy(update={"x": 99})
print(p2)
print(p)   # original unchanged
