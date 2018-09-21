a = 50
b = 20

while b > 0:
    tmp = a
    a = b
    b = tmp%b
print(a)


## The Python way
print()
while b > 0:
    a, b = b, a%b
print(f"Doing it in Python's way, we still get ==>{a:5}")
