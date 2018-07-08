from dataclasses import dataclass


class People:
    list = []

    @dataclass()
    class Person:
        name: str
        age: int = None
        friends: list = None

        def __eq__(self, other):
            return self.name == other

    def __str__(self):
        return self.list.__str__()

    def __getitem__(self, item):
        return self.item

    def __getattr__(self, item):
        if item not in self.list:
            self.list.append(self.Person(item))
        for i in self.list:
            if item == i:
                return i


def test():
    people_list = People()
    bob = people_list.bob
    bob.age = 24
    print(people_list)



if __name__ == '__main__':
    test()
