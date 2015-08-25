from animal_class import *

class Sheep(Animal):
    """A sheep"""

    def __init__(self,name):
        super().__init__(1,3,6,name)
        self._type = "Sheep"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "Poor" and water > self._water_need:
                self._weight += self._growth_rate * 1.25
            elif self._status == "Prime" and water > self._water_need:
                self._weight += self._growth_rate / 2
            else:
                self._weight += self._growth_rate 
        self._days_growing += 1
        self._update_status()
def main():
    sheep_animal = Sheep("Bob")
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()
