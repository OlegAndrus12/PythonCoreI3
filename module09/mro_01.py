# super() follows MRO — each class calls the next in the chain

class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        super().greet()
        print("B")

class C(A):
    def greet(self):
        super().greet()
        print("C")

class D(B, C):
    def greet(self):
        super().greet()
        print("D")

print(D.__mro__)
D().greet()   # A → C → B → D  (MRO order, each super() continues the chain)
