honap=int(input("Mely hónap: "))

if honap <= 3:
    print(honap, "tavasz")
elif honap <=6:
    print(honap, "nyár")
elif honap <=9:
    print(honap, "ősz")
else:
    print(honap, "tél")