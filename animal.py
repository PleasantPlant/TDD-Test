class Animal:
    def __init__(self, animalType=str):
        self.type = animalType
        self.size = ""
        self.age = 0
        self.name = ""
        match self.type.lower():
            case "cat":
                self.name = "Seymour"
            case "dog":
                self.name = "Spot"

    def speak(self):
        match (self.type.lower(), self.size.lower()):
            case ("cat", "small"):
                return "meow"
            case ("cat", "medium"):
                return "MEOW!"
            case ("cat", "large"):
                return "MEOW!"
            case ("dog", "small"):
                return "bow wow"
            case ("dog", "medium"):
                return "Ruff ruff"
            case ("dog", _):
                return "arf arf"
            case _:
                return "how did you set invalid values?"

    def describe(self):
        if self.age < 10:
            return f"{self.name} is young"
        elif self.age >= 10:
            return f"{self.name} is old"
