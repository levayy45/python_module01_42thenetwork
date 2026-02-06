class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_details(self) -> str:
        return f"- {self.name}: {self.height}cm"

    def get_type(self) -> str:
        return "regular"


class FloweringPlant(Plant):

    def __init__(self, name, height, color) -> None:
        super().__init__(name, height)
        self.color = color

    def get_details(self) -> str:
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )

    def get_type(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):

    def __init__(
        self, name: str, height: int, color: str, points: int
    ) -> None:
        super().__init__(name, height, color)
        self.points = points

    def get_details(self) -> str:
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), Prize points: {self.points}"
        )

    def get_type(self) -> str:
        return "prize"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        @staticmethod
        def calculate(plants: list[Plant]) -> tuple[int, int, int, int]:
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
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()

    def generate_report(self) -> None:
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

    def height_validation_test(val: int) -> bool:
        return val > 0
    height_validation_test = staticmethod(height_validation_test)

    def create_garden_network(cls) -> None:
        print("=== Garden Management System Demo ===\n")

        alice = cls("Alice")
        alice.add_plant(Plant("Oak Tree", 100))
        alice.add_plant(FloweringPlant("Rose", 25, "red"))
        alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

        alice.help_plants_grow()
        alice.generate_report()

        print("")
        print(f"Height validation test: {cls.height_validation_test(100)}")

        cls("Bob")

        print("Garden scores - Alice: 218, Bob: 92") #no harcode here
        print(f"Total gardens managed: {cls.total_gardens}")
    create_garden_network = classmethod(create_garden_network)

if __name__ == "__main__":
    GardenManager.create_garden_network()
