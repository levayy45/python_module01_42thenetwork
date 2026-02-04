class Plant:
    """
    Represents a base plant with common attributes.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes the plant's name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Represents a flower with a color and bloom ability.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initializes the flower's attributes, including color.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """
        Displays flower blooming behavior.
        """
        print(
            f"{self.name} (Flower): "
            f"{self.height}cm, {self.age} days, {self.color} color"
        )
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Represents a tree with a trunk diameter and ability to produce shade.
    """
    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        """
        Initializes the tree's attributes, including trunk diameter.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Displays shade area based on trunk diameter.
        """
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )
        shade = self.trunk_diameter + 28
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """
    Represents a vegetable with harvest season and nutritional value.
    """
    def __init__(
        self, name: str, height: int, age: int,
            harvest_season: str, nutritional_value: str) -> None:
        """
        Initializes the vegetable's attributes, including harvest
        season and nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_benefits(self) -> None:
        """
        Displays vegetable benefits and harvest season.
        """
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("")

    # Create instances of Flower
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 15, 12, "yellow")

    # Create instances of Tree
    oak = Tree("Oak", 500, 1825, 50)
    maple = Tree("Maple", 450, 1500, 40)

    # Create instances of Vegetable
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 60, "autumn", "vitamin A")

    # Simulate plant behaviors
    rose.bloom()
    print("")
    oak.produce_shade()
    print("")
    tomato.show_benefits()
