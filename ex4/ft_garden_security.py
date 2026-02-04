class SecurePlant:
    """
    Protects plant data using encapsulation and validation.
    """
    def __init__(self, name: str) -> None:
        """
        Initializes the plant with a name, height, and age.
        """
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")

    def get_height(self) -> int:
        """
        Returns the plant's height.
        """
        return self._height

    def get_age(self) -> int:
        """
        Returns the plant's age.
        """
        return self._age

    def set_height(self, value: int) -> None:
        """
        Updates the height with validation (non-negative values only).
        """
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """
        Updates the age with validation (non-negative values only).
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def display_status(self) -> None:
        """
        Displays the current state of the plant.
        """
        print(
            f"\nCurrent plant: {self.name} "
            f"({self._height}cm, {self._age} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")

    # Set valid values for height and age
    rose.set_height(25)
    rose.set_age(30)

    # Attempt to set an invalid height
    print("")
    rose.set_height(-5)

    # Display the plant's current status
    rose.display_status()
