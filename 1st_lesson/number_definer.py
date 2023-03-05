number = float(input())
last_number = ''
if number == 0:
    last_number = "zero"
elif number > 0:
    last_number = "positive"
    if 0 < number < 1:
        last_number = "small positive"
    elif number > 1_000_000:
        last_number = "large positive"
elif number < 0:
    last_number = "negative"
    if -1 < number < 0:
        last_number = "small negative"
    elif number < -1_000_000:
        last_number = "large negative"
print(last_number)