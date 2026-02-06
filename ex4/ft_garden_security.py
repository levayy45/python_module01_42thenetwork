class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def display_status(self) -> None:
        print(
            f"\nCurrent plant: {self.name} "
            f"({self._height}cm, {self._age} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")

    rose.set_height(25)
    rose.set_age(30)

    print("")
    rose.set_height(-5)

    rose.display_status()
