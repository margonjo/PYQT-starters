from animal_class import *

class Cow(Animal):
    """A cow"""

    def __init__(self,name):
        super().__init__(1,3,6,name)
        self._type = "Cow"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "Poor" and water > self._water_need:
                self._weight += self._growth_rate * 1.25
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()
def main():
    cow_animal = Cow()
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())
    

if __name__ == "__main__":
    main()
