
class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine

    def start_engine(self):
        return f"The {self.type_of_engine} engine is now running."

class Car:
    def __init__(self, model, engine: Engine):
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def start(self):
        return f"{self.model} is starting. {self.engine.start_engine()}"

# Example usage:
engine1 = Engine("V8")
car1 = Car("Mustang", engine1)

print(car1.start())  # Output: Mustang is starting. The V8 engine is now running.
