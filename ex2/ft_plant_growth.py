class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.plant_age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    cactus = Plant("Cactus", 15, 20)
    plants = [rose, cactus]
    initial_height = [rose.height, cactus.height]
    print("=== Day 1 ===")

    for plant in plants:
        plant.get_info()
        for _ in range(6):
            plant.grow()
            plant.age()

    i = 0
    print("=== Day 7 ===")
    for plant in plants:
        plant.get_info()
        final_height = plant.height
        growth = final_height - initial_height[i]
        i += 1
    print(f"Growth this week: +{growth}cm")
