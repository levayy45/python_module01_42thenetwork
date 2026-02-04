#!/usr/bin/python3

def display_plant_info(name: str, height: int, age: int) -> None:
    """
    Prints the plant's name, height, and age.
    """
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("=== End of Program ===")


if __name__ == "__main__":
    # Plant details
    name: str = "Rose"
    height: int = 25
    age: int = 30
    # Display plant information
    display_plant_info(name, height, age)
