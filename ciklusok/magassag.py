import random

ennyi=int(input("Ennyi ember: "))

for i in range(ennyi):
    print(str(i+1)+". ember magassága "+str(random.randrange(100,220))+" cm")