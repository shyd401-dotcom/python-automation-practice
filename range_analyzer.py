number = int(input("Enter a number: "))

if number % 2 == 0:
    parity = "even"
else:
    parity = "odd"

if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

print(f"{number} is an {parity} {sign} number.")
            