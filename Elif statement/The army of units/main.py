armyUnits = int(input())

if armyUnits < 1:
    print("no army")
elif armyUnits >= 1 and armyUnits <= 9:
    print("few")
elif armyUnits > 9 and armyUnits <= 49:
    print("pack")
elif armyUnits > 49 and armyUnits <= 499:
    print("horde")
elif armyUnits > 499 and armyUnits <= 999:
    print("swarm")
else:
    print("legion")