#Max level: 10
#Each Level is a new move
#Increase power or stun bacteria
#Max attacks: 4

import time, sys, random

soapType = 0


def printf(format, *arg):
    print(format % arg)


def bacLevel(l):
    if l == 0:
        return random.randrange(1, 3)
    elif l == 1:
        return random.randrange(1, 4)
    elif l == 2:
        return random.randrange(2, 5)
    elif l == 3:
        return random.randrange(2, 6)
    elif l == 4:
        return random.randrange(3, 7)
    elif l == 5:
        return random.randrange(3, 8)
    elif l == 6:
        return random.randrange(4, 9)
    elif l == 7:
        return random.randrange(4, 10)
    elif l == 8:
        return random.randrange(5, 11)
    elif l == 9:
        return random.randrange(5, 12)
    elif l == 10:
        return random.randrange(6, 13)


def bacHealth(num):
    if num == 1:
        return 30
    elif num == 2:
        return 40
    elif num == 3:
        return 50
    elif num == 4:
        return 60
    elif num == 5:
        return 70
    elif num == 6:
        return 80
    elif num == 7:
        return 90
    elif num == 8:
        return 100
    elif num == 9:
        return 150
    elif num == 10:
        return 200


def bacDamage(num):
    if num == 1:
        return 10
    elif num == 2:
        return 15
    elif num == 3:
        return 20
    elif num == 4:
        return 25
    elif num == 5:
        return 30
    elif num == 6:
        return 35
    elif num == 7:
        return 40
    elif num == 8:
        return 45
    elif num == 9:
        return 60
    elif num == 10:
        return 70


def combat(health, damage, defense, attacks, aDamage, eHealth, eDamage, eDefense, bHealth, bDamage, bDefense):
    beHealth = False
    while health > 0 and bHealth > 0:
        print("\nIt's your turn!")
        time.sleep(1)
        print("\nYour Stats: " + "\n     Health: " + str(health) + "\n     Damage: " + str(damage) + "\n     Defense: " + str(defense))
        print("\nOpponent Stats: " + "\n     Health: " + str(bHealth) + "\n     Damage: " + str(bDamage) + "\n     Defense: " + str(bDefense))
        print("\nChoose an attack to perform. Here's a list of your attacks:")
        for i in range(len(attacks)):
            aChoice = int(input("\n (" + str(i + 1) + ") " + attacks[i] + "\n     Damage: " + str(aDamage[i]))) - 1

        if aChoice == 0 or aChoice == 1 or aChoice == 3:
            time.sleep(1)
            print("\nYou dealt " + str(aDamage[aChoice]) + " damage to the opponent.")
            if eHealth[aChoice] > 0:
                beHealth = True
            if eDamage[aChoice] > 0:
                time.sleep(1)
                print("\nYou also lower the opponent's damage by " + str(eDamage[aChoice]) + ".")
                bDamage -= eDamage[aChoice]
                if bDamage < 1:
                    bDamage = 1
            if eDefense[aChoice] > 0:
                time.sleep(1)
                print("\nYou also lower the opponent's defense by " + str(eDefense[aChoice]) + ".")
                bDefense -= eDefense[aChoice]

            bHealth -= aDamage[aChoice]

            if beHealth:
                time.sleep(1)
                print("You also lower the opponent's health by " + str(eHealth[aChoice]) + " by effects.")

                bHealth -= eHealth[aChoice] * (abs((bDefense * -1.0) + 100.0) / 100.0)

        else:
            print("\nInvalid Input.")
            continue

        if bHealth <= 0:
            continue

        time.sleep(1)
        print("\nIt's your opponent's turn!")
        time.sleep(1)
        print("\nYour opponent dealt " + str(bDamage) + " damage to you.")
        health -= bDamage

    if health <= 0:
        print("\nYou've been defeated by your opponent...")
        return False

    if bHealth <= 0:
        print("\nYou've defeated your opponent!")
        return True


def life(type):
    days = 0
    lives = 3
    level = 0
    maxXP = 10
    XP = 0
    bDefense = 0

    if type == 1:
        attacks = ["Sodium Dodecylbenzenesulfonate (Lowers Opponent's Damage by 5)"] #damage: 20
        aDamage = [20]
        eHealth = [0]
        eDamage = [5]
        eDefense = [0]
        health = 10
        damage = 1.6
        defense = 1.6
    elif type == 2:
        attacks = ["Lavender Oil (Lowers Opponent's Defense by 5)"] #damage: 10
        aDamage = [10]
        eHealth = [0]
        eDamage = [0]
        eDefense = [5]
        health = 20
        damage = 1.3
        defense = 1
    else:
        attacks = ["Anthocyanins (Poisons Opponent, Injuring by 5)"] #damage: 5
        aDamage = [5]
        eHealth = [5]
        eDamage = [0]
        eDefense = [0]
        health = 30
        damage = 1
        defense = 1.3
    while True:
        print("\nThe early morning rises for day " + str(days) + ", awaiting for you to clean the world.\nCurrent Stats: \nLevel: " + str(level) + "\nAttack List: ")
        for i in range(len(attacks)):
            print("\n - " + attacks[i])

        #setup all of the bacteria's properties
        bLevel = bacLevel(level)
        bHealth = bacHealth(bLevel)
        bDamage = bacDamage(bLevel)

        randNum = random.randrange(1, 7)
        if randNum == 1:
            print("\nA bacteria has appeared! It's a level " + str(bLevel) + " Staphylococcus epidermidis!")
        elif randNum == 2:
            print("\nA bacteria has appeared! It's a level " + str(bLevel) + " Methicillin-resistant Staphylococcus aureus!")
        elif randNum == 3:
            print("\nA bacteria has appeared! It's a level " + str(bLevel) + " Staphylococcus hominis!")
        elif randNum == 4:
            print("\nA bacteria has appeared! It's a level " + str(bLevel) + " Propionibacteria!")
        elif randNum == 5:
            print("\nA bacteria has appeared! It's a level " + str(bLevel) + " Corynebacterium!")
        else:
            print("\nA bacteria has appeared! It's a level " + str(bLevel) + " Streptococcus pyogenes!")

        if (combat(health, damage, defense, attacks, aDamage, eHealth, eDamage, eDefense, bHealth, bDamage, bDefense) == True):
            XP += bLevel * 2
            if XP >= maxXP:
                level += 1
                maxXP += 15
                health += 10
                damage += 0.3
                defense += 0.3
                #add new attacks, num less than or equal to 3


def store(type):
    boolean = False
    while boolean == False:
        randNum = random.randrange(1, 3)
        time.sleep(3)
        print("\nBarg' N-Mart has opened up and now you await for a customer to purchase you.")
        if randNum == 1:
            boolean = True
            time.sleep(3)
            print("\nA customer by the name of Jeff decides to walk in your aisle. He catches the"
                  "\nvibrant colors on your box from the corner of his eye. He's thinking about buying"
                  "\nyou. He takes several seconds and decides that he does want to buy soap. Jeff grabs"
                  "\nyour soap box, purchases you, and places you onto a soap dish near the bathroom"
                  "\nsink.")
        else:
            time.sleep(5)
            print("\nA full day passes and not yet one person decides to buy you. But there's always another day.")

    boolean = False

    life(type)


def soap():

    print("\nYou've been chosen to be manufactured as a bar of soap but they need a scent for you. Choose a bar of soap.")
    print("\n(1) Fresh Laundry (Low Health, High Attack, High Defense)"
          "\n(2) Lavender      (Normal Health, Normal Attack, Low Defense)"
          "\n(3) Mixed Berries (High Health, Low Attack, Normal Defense)")
    choice = int(raw_input())
    if choice == 1:
        choice = raw_input("\nYou've chosen Fresh Laundry. Are you sure about that? (Yes or No)")
        soapType = 1
    elif choice == 2:
        choice = raw_input("\nYou've chosen Lavender. Are you sure about that? (Yes or No)")
        soapType = 2
    elif choice == 3:
        choice = raw_input("\nYou've chosen Mixed Berries. Are you sure about that? (Yes or No)")
        soapType = 3
    else:
        print("\nInvalid input.")
        soap()

    if choice.lower() == "yes":
        time.sleep(1)
        print("\nGreat! Your job is to wait for a customer to buy you and be used as a soap bar."
            "\nNow the purpose of a soap bar or any sort of soap is very simple. Being a soap"
            "\nis some what difficult because when the human is washing its hands, it'll use"
            "\nyou inorder to kill any and all bacteria. By 'all' we mean 99.9%. Anyways,"
            "\ndepending on your soap scent, you have certain abilities to attack the bacteria."
            "\nAnd just like soaps, bacterias also vary which means some can be more difficult"
            "\nthan others so be aware of that. Your journey ends when you die to bacteria three"
            "\ntimes. Your owner may get the message that you've expired in usefulness,"
            "\ndiscarding you in the trash can, the worst thing that could happen to a soap bar."
            "\nWell, I think that's enough typing for now. Hope you enjoy your shelf life!")
        time.sleep(3) #make this 25
    elif choice.lower() == "no":
        soap()
    else:
        print("\nInvalid input.")
        soap()

    store(soapType)


def main():
    soap()

main()
