class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Some sound"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


if __name__ == "__main__":
    my_dog = Dog("Buddy")
    print(f"{my_dog.name} says {my_dog.speak()}")
