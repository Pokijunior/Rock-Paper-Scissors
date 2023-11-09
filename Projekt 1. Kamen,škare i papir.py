from random import randint
gamemode=["kamen","skare","papir"]
computer=gamemode[randint(0,2)]
player=False
bc=0
bp=0
rod=input("Koji ste rod? M/Z: ")
ime=input("Unesite svoje ime: ")
while player==False:
    player=input("Odaberite: kamen,skare,papir " )
    print("")
    if player==computer:
        print("Odabrali ste isti znak.")
    elif player=="kamen":
        if computer=="papir":
            print("Izgubio si,",computer,"pobjeduje",player)
            bc+=1
        else:
            if rod.upper()=="M":
                print("Pobjedio si,",player,"pobjeduje",computer)
            if rod.upper()=="Z":
                print("Pobjedila si,",player,"pobjeduje",computer)
            bp+=1
    elif player=="skare":
        if computer=="kamen":
            if rod.upper()=="M":
                print("Izgubio si,",player,"pobjeduje",computer)
            if rod.upper()=="Z":
                print("Izgubila si,",player,"pobjeduje",computer)
            bc+=1
        else:
            if rod.upper()=="M":
                print("Pobjedio si,",player,"pobjeduje",computer)
            if rod.upper()=="Z":
                print("Pobjedila si,",player,"pobjeduje",computer)
            bp+=1
    elif player=="papir":
        if computer=="skare":
            if rod.upper()=="M":
                print("Izgubio si,",player,"pobjeduje",computer)
            if rod.upper()=="Z":
                print("Izgubila si,",player,"pobjeduje",computer)
            bc+=1
        else:
            if rod.upper()=="M":
                print("Pobjedio si,",player,"pobjeduje",computer)
            if rod.upper()=="Z":
                print("Pobjedila si,",player,"pobjeduje",computer)
            bp+=1
    else:
        ("Krivi unos.")
    if bc==3:
        print("Kompjuter je pobjedio!")
        break
    if bp==3:
        print(ime+" je pobjedio!")
        break
    if bc>bp:
        print("Kompjuter vodi sa",bc," naprema",bp)
    elif bp>bc:
        if rod.upper()=="M":
            print("Gospodin",ime,"vodi sa",bp,"naprema",bc)
        if rod.upper()=="Z":
            print("Gospodica",ime,"vodi sa",bp,"naprema",bc)
            
    else:
        print("Izjednaceno")
    player=False
    computer=gamemode[randint(0,2)]

