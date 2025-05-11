
class Logger:
  def __init__(self, message):
    self.message = message
    print(f"Object created: {self.message}")

  def __del__(self):
    print(f"Object destroyed: {self.message}")

obj1 = Logger("Message 1")
obj2 = Logger("Message 2")

del obj1
del obj2

# print(obj1.message) returns error
# print(obj2.message)
