class Car:
  brand = "Porche"

  def start(self):
    print(f"The {self.brand} car has started")


# Object creation
my_car = Car()

# Accessing public variable
print(my_car.brand)

# Accessing public method
my_car.start()
