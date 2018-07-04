from dataclasses import dataclass


@dataclass()
class Person:
    name: str
    age: int
    objects: list
    active: bool = True


bob = Person(name="Bob", age=35, objects=[])
print(bob)
