from models.animal import Animal


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


if __name__ == "__main__":
    my_dog = Dog("Buddy")
    print(f"{my_dog.name} says {my_dog.speak()}")
