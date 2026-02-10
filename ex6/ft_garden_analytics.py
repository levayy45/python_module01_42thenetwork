class Plant():
    def __init__(
            self, name: str, height: int, color: str = "", prize: int = 0
            ) -> None:
        self.name = name
        self.height = height
        self.color = color
        self.prize = prize

    def grow(self) -> None:
        self.height += 1
        GardenManager.totale_growth += 1
        print(f"{self.name} grew 1cm")

    def print_info(self) -> None:
        print(f"- {self.name}: {self.height}cm", end="")


class FloweringPlant(Plant):

    def __init__(
            self, name: str, height: int, color: str, prize: int = 0
            ) -> None:
        super().__init__(name, height, color, prize)
        self.is_bloom = True

    def is_blooming(self) -> str:
        if self.is_bloom is True:
            return "(blomming)"
        else:
            return ""

    def print_info(self) -> None:
        super().print_info()
        print(f", {self.color} flowers {self.is_blooming()}", end="")


class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color, prize)

    def getprize(self) -> int:
        if self.prize > 0:
            return self.prize
        else:
            return self.prize * -1

    def print_info(self) -> None:
        super().print_info()
        print(f", Prize points: {self.getprize()}", end="")


class GardenManager:

    totale_growth: int = 0
    totale_plants: int = 0
    totale_garden: int = 0
    d_gardens = {}

    def __init__(self, owner: str) -> None:
        self.owner = owner
        GardenManager.totale_garden += 1

    def add_plant(self, plant: Plant) -> str:
        self.GardenStats(self.owner, plant)
        return f"Added {plant.name} to {self.owner}'s garden"

    def create_garden_network(cls: type["GardenManager"]) -> int:
        return GardenManager.totale_garden
    create_garden_network = classmethod(create_garden_network)

    class GardenStats:
        regular = 0
        flowring = 0
        prize = 0
        is_valid_test = True

        def __init__(self, owner: str, plant: Plant) -> None:
            self.owner = owner
            self.plant = plant
            if self.owner not in GardenManager.d_gardens:
                GardenManager.d_gardens[self.owner] = []
            GardenManager.d_gardens[self.owner] += [self.plant]
            GardenManager.totale_plants += 1

        def calculate_plant_types() -> None:
            for owner in GardenManager.d_gardens:
                for plant in GardenManager.d_gardens[owner]:
                    if plant.prize != 0:
                        GardenManager.GardenStats.prize += 1
                    elif plant.color != "":
                        GardenManager.GardenStats.flowring += 1
                    else:
                        GardenManager.GardenStats.regular += 1
        calculate_plant_types = staticmethod(calculate_plant_types)

        def is_validate_height() -> None:
            for owner in GardenManager.d_gardens:
                for plant in GardenManager.d_gardens[owner]:
                    if plant.height < 0:
                        GardenManager.GardenStats.is_valid_test = False
        is_validate_height = staticmethod(is_validate_height)

        def get_garden_score(owner: str) -> int:
            total_score = 0
            if owner in GardenManager.d_gardens:
                for plant in GardenManager.d_gardens[owner]:
                    total_score += plant.height
                    if plant.color != "":
                        total_score += 15
                    total_score += plant.prize
            return total_score
        get_garden_score = staticmethod(get_garden_score)

        def get_statistic() -> None:
            GardenManager.GardenStats.calculate_plant_types()
            GardenManager.GardenStats.is_validate_height()
            print(f"\nPlants added: {GardenManager.totale_plants}, ", end="")
            print(f"Total growth: {GardenManager.totale_growth}cm")
            print("Plant types: ", end="")
            print(
                f"{GardenManager.GardenStats.regular} regular, ", end=""
                )
            print(f"{GardenManager.GardenStats.flowring} flowering, ", end="")
            print(f"{GardenManager.GardenStats.prize} prize flowers")
            print("\nHeight validation test: ", end="")
            print(f"{GardenManager.GardenStats.is_valid_test}")
        get_statistic = staticmethod(get_statistic)


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
    GardenManager.GardenStats.get_statistic()

    manager_2 = GardenManager("Bob")
    sunflower_2 = FloweringPlant("Sunflower", 77, "yellow")
    manager_2.add_plant(sunflower_2)

    print(f"Garden scores - {manager_1.owner}: ", end="")
    print(f"{manager_1.GardenStats.get_garden_score(manager_1.owner)}", end="")
    print(f", {manager_2.owner}: ", end="")
    print(f"{manager_2.GardenStats.get_garden_score(manager_2.owner)}")
    print(f"Total gardens managed: {GardenManager.create_garden_network()}")