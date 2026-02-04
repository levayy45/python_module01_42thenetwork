class Plant:
    """
    Represents a plant with a name, height, and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a plant object.
        """
        self.name = name
        self.height = height
        self.age = age


def print_plant() -> None:
    """
    Displays a registry of plants.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    # Display plant information
    print("=== Garden Plant Registry ===")
    for i in range(3):
        plant = plants[i]
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    print_plant()
