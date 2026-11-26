# Bool Type Conversios
a = 1
print(a,type(a))
b = bool(a)
print(b,type(b))

A = 30
print(A,type(A))
B = bool(A)
print(B,type(B))

# float --> bool
a1 = 5.2
print(a1,type(a1))
b1 = bool(a1)
print(b1,type(b1))

# complex --> bool
A1 = 2+3j
print(A1,type(A1))
B1 = bool(A1)
print(B1,type(B1))

# str with int,float,complex values --> bool
c = "1"
print(c,type(c))
d = bool(c)
print(d,type(d))

# str with float --> bool
c1 = "3.2"
print(c1,type(c1))
d1 = bool(c1)
print(d1,type(d1))

# str with complex --> bool
C = 4+3j
print(C,type(C))
D = bool(C)
print(D,type(D))

n = "bag"
print(n,type(n))
N = bool(n)
print(N,type(N))