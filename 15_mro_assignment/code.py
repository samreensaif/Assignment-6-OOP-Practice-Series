class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass  # No show() method, so it will use MRO

# Create an object of class D
obj = D()
obj.show()  # This will show the result based on MRO
