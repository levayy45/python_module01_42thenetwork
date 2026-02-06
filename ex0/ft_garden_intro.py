#!/usr/bin/python3

def display_plant_info(name: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    name: str = "Rose"
    height: int = 25
    age: int = 30
    display_plant_info(name, height, age)
