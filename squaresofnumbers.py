lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in lst:
    print(num)
    print(num*num)
    print()

print("That's the whole list now...")


## Doing it the Python way

for num2 in range(0,11):
    print(num2)
    print(num2*num2)
    print()
print("Again, that's the whole list using the range() function...")

### Doing it the Python way with the f-strings witout and with f:formatting...
print("Compare the formatted outputs...")
for num3 in range(0,11):
    print(f"{num3} {num3 * num3}")

##Compare the layout now...
for num3 in range(0,11):
    print(f"{num3:2} {num3 * num3:4}")

print()
## Print range by wrapping in a list
print(range(20))
print(list(range(20)))
