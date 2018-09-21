import datetime

today = datetime.datetime.today()
dayofweek = today.weekday()

print("Let's check if it's Tuesday today...")
## Day of week begins from Monday == 0... Sunday == 6
if dayofweek == 1:
    print("It's Tuesday!")
elif dayofweek == 0:
    print("It's not Tuesday.")
    print("Luckily, it will be Tuesday tomorrow...")
else:
    print("Unfortunately, it's not Tuesday.")

print("Thanks for checking whether it's Tuesday of not!")
