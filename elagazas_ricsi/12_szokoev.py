ev=int(input("év: "))

print(ev % 4 == 0 and (ev % 100 != 0 or ev % 400 == 0) and "Szökőév!!" or "Nem szökik!")