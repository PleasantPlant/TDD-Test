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
        match self.type.lower():
            case "cat":
                if self.size.lower() == "small":
                    return "meow"
                else:
                    return "Meow!"
            case "dog":
                match self.size.lower():
                    case "small":
                        return "bow wow"
                    case "medium":
                        return "Ruff ruff"
                    case "large":
                        return "arf arf"
                    case _:
                        return "how did you set an invalid size?"
            case _:
                return "how did you set an invalid type?"

    def describe(self):
        if self.age <= 10:
            return f"{self.name} is young"
        elif self.age > 10:
            return f"{self.name} is old"
