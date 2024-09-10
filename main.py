class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to_floor(self, new_floor):
        if new_floor != int(new_floor) or not (1 <= new_floor <= self.number_of_floors):
            print("Такого этажа не существует")
        else:
            print(new_floor)


d1 = House('d1', 1000)
d2 = House('d2', 10)

d1.go_to_floor(999)
d2.go_to_floor(99)