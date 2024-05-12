class A:
    a=9
class B(A):
    b=8
class C(B):
    pass

print(C.mro())