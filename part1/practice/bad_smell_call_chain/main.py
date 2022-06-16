# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    @staticmethod
    def get_name():
        return 42


class Street:
    @staticmethod
    def get_room() -> Room:
        return Room()


class City:
    @staticmethod
    def get_street() -> Street:
        return Street()

    @staticmethod
    def population():
        return 100500


class Country:
    @staticmethod
    def get_city() -> City:
        return City()


class Planet:
    @staticmethod
    def get_contry() -> Country:
        return Country()


class Person:
    def __init__(self, room, population_cities):
        self.room = room
        self.population_cities = population_cities

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.population_cities


if __name__ == '__main__':
    person = Person(212, 100050)

    print(person.get_person_room())
    print(person.get_city_population())
