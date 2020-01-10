from attacks import Attack


def askUser():
    print("==========================================")
    print("\n Please select an attack type:")
    print("\n 1. UDP Flood")
    print("\n 2. Ping of death")
    print("\n=========================================")
    try:
        valid = [1,2]
        answer = int(input("Choice [1-2]: "))
        if answer not in valid:
            print("Please enter a valid number.")
            askUser()
        else:
            if answer == 1:
                host = input('Host: ')
                port = int(input('Post: '))

                att = Attack('udpflood', host, port)
                isUp = att.checkTargetAlive()
                print(isUp)
                if isUp:
                    att.attack()
                else:
                    print("Could not check if target is up.")
                    keepGoing = input("Do you still want to attack target? (y/n)")
                    if keepGoing == 'y' or keepGoing == 'Y':
                        att.attack()
                    elif answer == 'n' or answer == 'N':
                        askUser()
                    else:
                        pass
            else:
                pass

    finally:
        print("Done.")

askUser()