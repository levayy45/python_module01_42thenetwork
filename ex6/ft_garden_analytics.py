class Plant:
    def __init__(
        self,
        name: str,
        height: int,
        color: str = "",
        prize: int = 0
    ) -> None:
        self.name: str = name
        self.height: int = height
        self.color: str = color
        self.prize: int = prize

    def grow(self) -> None:
        self.height += 1
        GardenManager.total_growth += 1
        print(f"{self.name} grew 1cm")

    def print_info(self) -> None:
        print(f"- {self.name}: {self.height}cm", end="")


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize: int = 0
    ) -> None:
        super().__init__(name, height, color, prize)
        self.is_bloom: bool = True

    def is_blooming(self) -> str:
        if self.is_bloom:
            return "(blooming)"
        else:
            return ""

    def print_info(self) -> None:
        super().print_info()
        print(f", {self.color} flowers {self.is_blooming()}", end="")


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize: int
    ) -> None:
        super().__init__(name, height, color, prize)

    def get_prize(self) -> int:
        return abs(self.prize)

    def print_info(self) -> None:
        super().print_info()
        print(f", Prize points: {self.get_prize()}", end="")


class GardenManager:
    total_growth: int = 0
    total_plants: int = 0
    total_gardens: int = 0
    gardens: dict[str, list[Plant]] = {}

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> str:
        if self.owner not in GardenManager.gardens:
            GardenManager.gardens[self.owner] = []
        GardenManager.gardens[self.owner].append(plant)
        GardenManager.total_plants += 1
        return f"Added {plant.name} to {self.owner}'s garden"

    def create_garden_network(cls) -> int:
        return cls.total_gardens
    create_garden_network = classmethod(create_garden_network)

    class GardenStats:
        def calculate_plant_types() -> tuple[int, int, int]:
            regular: int = 0
            flowering: int = 0
            prize: int = 0

            for owner in GardenManager.gardens:
                for plant in GardenManager.gardens[owner]:
                    if plant.prize != 0:
                        prize += 1
                    elif plant.color != "":
                        flowering += 1
                    else:
                        regular += 1

            return regular, flowering, prize
        calculate_plant_types = staticmethod(calculate_plant_types)

        def validate_heights() -> bool:
            for owner in GardenManager.gardens:
                for plant in GardenManager.gardens[owner]:
                    if plant.height < 0:
                        return False
            return True
        validate_heights = staticmethod(validate_heights)

        def get_garden_score(owner: str) -> int:
            total_score: int = 0
            if owner in GardenManager.gardens:
                for plant in GardenManager.gardens[owner]:
                    total_score += plant.height
                    if plant.color != "":
                        total_score += 15
                    total_score += plant.prize
            return total_score
        get_garden_score = staticmethod(get_garden_score)

        def get_statistics() -> None:
            regular, flowering, prize = (
                GardenManager.GardenStats.calculate_plant_types()
            )
            is_valid: bool = GardenManager.GardenStats.validate_heights()

            print(
                f"\nPlants added: {GardenManager.total_plants}, ",
                end=""
            )
            print(f"Total growth: {GardenManager.total_growth}cm")
            print("Plant types: ", end="")
            print(f"{regular} regular, ", end="")
            print(f"{flowering} flowering, ", end="")
            print(f"{prize} prize flowers")
            print("\nHeight validation test: ", end="")
            print(f"{is_valid}")
        get_statistics = staticmethod(get_statistics)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager_1 = GardenManager("Alice")
    oak_tree = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    print(manager_1.add_plant(oak_tree))
    print(manager_1.add_plant(rose))
    print(manager_1.add_plant(sunflower))

    print(f"\n{manager_1.owner} is helping all plants grow...")
    oak_tree.grow()
    rose.grow()
    sunflower.grow()

    print(f"\n=== {manager_1.owner}'s Garden Report ===")
    print("Plants in garden:")
    oak_tree.print_info()
    print()
    rose.print_info()
    print()
    sunflower.print_info()
    print()
    GardenManager.GardenStats.get_statistics()

    manager_2 = GardenManager("Bob")
    sunflower_2 = FloweringPlant("Sunflower", 77, "yellow")
    manager_2.add_plant(sunflower_2)

    print(f"Garden scores - {manager_1.owner}: ", end="")
    score_1 = manager_1.GardenStats.get_garden_score(manager_1.owner)
    print(f"{score_1}", end="")
    print(f", {manager_2.owner}: ", end="")
    score_2 = manager_2.GardenStats.get_garden_score(manager_2.owner)
    print(f"{score_2}")
    print(
        f"Total gardens managed: "
        f"{GardenManager.create_garden_network()}"
    )
