from pydantic import BaseModel, computed_field
from datetime import date


# computed_field exposes a @property in model_dump / model_dump_json / JSON schema

class Person(BaseModel):
    first_name: str
    last_name: str
    birth_date: date

    @computed_field
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @computed_field
    @property
    def age(self):
        today = date.today()
        delta = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            delta -= 1
        return delta


p = Person(first_name="Isaac", last_name="Newton", birth_date="1643-01-04")
print(p.full_name)
print(p.age)

# computed fields appear in model_dump and model_dump_json
print(p.model_dump())
print(p.model_dump_json(indent=2))

# and in the JSON schema
from pprint import pprint
pprint(Person.model_json_schema())
