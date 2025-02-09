class A:
    def method(self):
        print("This method belongs to class A")
    pass

class B(A):
    def method(self):
       print("This method belongs to class B")
    pass

class C(A):
    def method(self):
        print("This method belongs to class C")
    pass

class D(B,C):
    def method(self):
        print("This method belongs to class D")
    pass

d = D()
d.method()