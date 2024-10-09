passwd="titok"
ok=False
while not ok:
    ok=input("Jelszó: ")==passwd
    if ok:
        print("Jó!")
    else:
        print("Rossz!")