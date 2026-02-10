class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.height}cm, {self.age} days, {self.color} color"
        )
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )
        shade = self.trunk_diameter + 28
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: int, age: int,
            harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_benefits(self) -> None:
        print(
            f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 15, 12, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    maple = Tree("Maple", 450, 1500, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 60, "autumn", "vitamin A")

    rose.bloom()
    print("")
    oak.produce_shade()
    print("")
    tomato.show_benefits()
