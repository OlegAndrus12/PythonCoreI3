employees = [
        {
      "id": 1,
      "first_name": "Ezequiel",
      "last_name": "Jiri",
      "age": 28,
      "job_title": "Research Nurse",
      "email": "ejiri0@constantcontact.com",
      "gender": "Bigender",
      "shirt_size": "XL",
      "favorite_color": "#fa173b",
      "iso_code": "PH",
      "years_of_experience": 10,
      "annual_salary": 184958.79
    },
    {
      "id": 2,
      "first_name": "Kara",
      "last_name": "Benkin",
      "age": 63,
      "job_title": "Junior Executive",
      "email": "kbenkin1@toplist.cz",
      "gender": "Genderfluid",
      "shirt_size": "XL",
      "favorite_color": "#9b8185",
      "iso_code": "YE",
      "years_of_experience": 4,
      "annual_salary": 197442.13
    },
]


class Employee:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"[{self.user_id}] {self.name} <{self.email}>"

    def __repr__(self):
        return f"Employee({self.name!r}, id={self.user_id})"


class Department:
    def __init__(self, name):
        self.name = name
        self._employees = []
        self._index = 0

    def add(self, employee):
        self._employees.append(employee)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._employees):
            raise StopIteration
        employee = self._employees[self._index]
        self._index += 1
        return employee

    def __len__(self):
        return len(self._employees)

    def __str__(self):
        return f"Department '{self.name}' ({len(self)} employees)"


engineering_dep = Department("Engineering")

for emp in employees:
    engineering_dep.add(
        Employee(
            user_id=emp["id"],
            name=emp["first_name"] + emp["last_name"],
            email=emp["email"],
        )
    )

for employee in engineering_dep:
    print(f"  {employee}")
