class Plant:
    """
    Represents a plant with a name, height, and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes the plant's attributes.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """
        Returns plant information as a formatted string.
        """
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    # Create a list of plants
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    # Display all created plants
    print("=== Plant Factory Output ===")
    for i in range(5):
        print(plants[i].get_info())

    print("\nTotal plants created: 5")
