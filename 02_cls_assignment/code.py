
class Counter:
  count = 0

  def __init__(self):
    Counter.count += 1

  @classmethod
  def display_count(cls):
    print(f"Total objects created: {cls.count}")

counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

Counter.display_count()
