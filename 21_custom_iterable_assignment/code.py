
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stops the iteration when countdown reaches 0
        self.current -= 1
        return self.current + 1  # Returns the current countdown value

# Example usage:
countdown = Countdown(5)

# Using for loop to iterate over the Countdown object
for num in countdown:
    print(num)
