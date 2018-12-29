import random
for i in range(0,100):
    print(i)
n = random.randint(1, 99)
monster = int(raw_input("choose from 1 to 99 to kill this monster: "))
while n != "guess":
    print
    if monster < n:
        print ("you damaged the monster low health" )
        monster = int(raw_input("kill me or i will kill you: "))
    elif monster > n:
        print (" you damaged the monster very high health")
        monster = int(raw_input("kill me or i will kill you: "))
    else:
        print ("you killed the monster")
        break
    print


