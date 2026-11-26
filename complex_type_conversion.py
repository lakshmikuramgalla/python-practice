#Complex Possible Type Conversions

# int --> complex
a = 5
print(a,type(a))
b = complex(a)
print(b,type(b))

# float --> complex
a1 = 10.5
print(a1,type(a1))
b1 = complex(a1)
print(b1,type(b1))

# bool --> complex
A = False
print(A,type(A))
B = complex(A)
print(B,type(B))

# str with int --> complex
A1 = "7"
print(A1,type(A1))
B1 = complex(A1)
print(B1,type(B1))

# str with float --> complex
c= "7.6"
print(c,type(c))
d = complex(c)
print(d,type(d))

# str with complex --> complex
c1 = "2+4J"
print(c1,type(c1))
d1 = complex(c1)
print(d1,type(d1))