n = int(input())
heroes = {}
for i in range(n):
    data = input().split()
    heroes[data[0]] = {'HP': int(data[1]), 'MP': int(data[2])}

command = input()
while command != "End":
    current_command = command.split(" - ")
    hero_name = current_command[1]
    if current_command[0] == "CastSpell":
        hero_name = current_command[1]
        MP_needed = int(current_command[2])
        spell_name = current_command[3]
        if heroes[hero_name]['MP'] >= MP_needed:
            heroes[hero_name]['MP'] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif current_command[0] == "TakeDamage":
        hero_name = current_command[1]
        damage = int(current_command[2])
        attacker = current_command[3]
        heroes[hero_name]['HP'] -= damage
        if heroes[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif current_command[0] == "Recharge":
        hero_name = current_command[1]
        amount = int(current_command[2])
        if heroes[hero_name]['MP'] + amount >= 200:

            print(f"{hero_name} recharged for {(200 - heroes[hero_name]['MP'])} MP!")
            heroes[hero_name]['MP'] = 200
        else:
            heroes[hero_name]['MP'] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif current_command[0] == "Heal":
        hero_name = current_command[1]
        amount = int(current_command[2])
        if heroes[hero_name]['HP'] + amount >= 100:

            print(f"{hero_name} healed for {100 - heroes[hero_name]['HP']} HP!")
            heroes[hero_name]['HP'] = 100
        else:
            heroes[hero_name]['HP'] += amount
            print(f"{hero_name} healed for {amount} HP!")

    command = input()
for hero in heroes:
    print(f"{hero}")
    print(f"HP: {heroes[hero]['HP']}")
    print(f"MP: {heroes[hero]['MP']}")
