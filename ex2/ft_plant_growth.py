class Plant:
    """
    Represents a plant that can grow and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a plant with its name, height, and ages.
        """
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self, growth_amount: int) -> None:
        """
        Increases the plant's height by the specified amount.
        """
        self.height += growth_amount

    def age(self, days: int) -> None:
        """
        Increases the plant's age by the specified number of days.
        """
        self.plant_age += days

    def get_info(self) -> str:
        """
        Returns information about the plant's current state.
        """
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


if __name__ == "__main__":
    # Create the plant
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(rose.get_info())

    # Simulate a week of growth
    weekly_growth: int = 6
    for day in range(1, 7):
        if day == 6:
            rose.grow(weekly_growth)
            rose.age(6)

    # Day 7: Display the updated state of the plant
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{weekly_growth}cm")
