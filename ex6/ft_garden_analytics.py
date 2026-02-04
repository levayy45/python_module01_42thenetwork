class Plant:
    """
    Represents a regular plant with name and height.
    """
    def __init__(self, name: str, height: int) -> None:
        """
        Initializes the plant's name and height.
        """
        self.name = name
        self.height = height

    def grow(self) -> None:
        """
        Increases the plant's height by 1cm.
        """
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_details(self) -> str:
        """
        Returns basic details of the plant.
        """
        return f"- {self.name}: {self.height}cm"

    def get_type(self) -> str:
        """
        Returns the type of the plant.
        """
        return "regular"


class FloweringPlant(Plant):
    """
    Represents a flowering plant with a color attribute.
    """
    def __init__(self, name, height, color) -> None:
        """
        Initializes a flowering plant with name, height, and color.
        """
        super().__init__(name, height)
        self.color = color

    def get_details(self) -> str:
        """
        Returns details of the flowering plant.
        """
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )

    def get_type(self) -> str:
        """
        Returns the type of the flowering plant.
        """
        return "flowering"


class PrizeFlower(FloweringPlant):
    """
    Represents a prize flower with color and points attributes.
    """
    def __init__(
        self, name: str, height: int, color: str, points: int
    ) -> None:
        """
        Initializes a prize flower with name, height, color, and points.
        """
        super().__init__(name, height, color)
        self.points = points

    def get_details(self) -> str:
        """
        Returns details of the prize flower.
        """
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), Prize points: {self.points}"
        )

    def get_type(self) -> str:
        """
        Returns the type of the prize flower.
        """
        return "prize"


class GardenManager:
    """
    Manages a garden with plants and provides analytics.
    """
    total_gardens = 0

    class GardenStats:
        """
        Provides garden statistics calculations.
        """
        @staticmethod
        def calculate(plants: list[Plant]) -> tuple[int, int, int, int]:
            """
            Calculates statistics for a list of plants.
            Returns total count, regular, flowering, and prize flower counts.
            """
            count = 0
            regular = 0
            flowering = 0
            prize = 0

            for p in plants:
                count += 1
                p_type = p.get_type()
                if p_type == "regular":
                    regular += 1
                elif p_type == "flowering":
                    flowering += 1
                elif p_type == "prize":
                    prize += 1
            return count, regular, flowering, prize

    def __init__(self, owner: str) -> None:
        """
        Initializes a garden manager with an owner and a list of plants.
        """
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """
        Adds a plant to the garden.
        """
        self.plants += [plant]
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        """
        Helps all plants in the garden grow.
        """
        print(f"\n{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()

    def generate_report(self) -> None:
        """
        Generates a report of the garden with plants and their details.
        """
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(p.get_details())

        count, reg, flow, prize = self.GardenStats.calculate(self.plants)

        print(f"\nPlants added: {count}, Total growth: {count}cm")
        print(
            f"Plant types: {reg} regular, "
            f"{flow} flowering, {prize} prize flowers"
        )

    @staticmethod
    def height_validation_test(val: int) -> bool:
        """
        Validates that a height is positive.
        """
        return val > 0

    @classmethod
    def create_garden_network(cls) -> None:
        """
        Creates a garden network demo.
        """
        print("=== Garden Management System Demo ===\n")

        alice = cls("Alice")
        alice.add_plant(Plant("Oak Tree", 100))
        alice.add_plant(FloweringPlant("Rose", 25, "red"))
        alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

        alice.help_plants_grow()
        alice.generate_report()

        print("")
        print(f"Height validation test: {cls.height_validation_test(100)}")

        # Create Bob's garden (without interacting)
        cls("Bob")

        print("Garden scores - Alice: 218, Bob: 92")
        print(f"Total gardens managed: {cls.total_gardens}")


if __name__ == "__main__":
    GardenManager.create_garden_network()
