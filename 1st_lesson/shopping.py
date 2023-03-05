buddget = int(input())
command = input()
money = 0
is_enought = True
while command != "End":
    price = int(command)
    money += price
    if money > buddget:
        is_enought = False
        print("You went in overdraft!")
        break
    command = input()
if is_enought:
    print("You bought everything needed.")
