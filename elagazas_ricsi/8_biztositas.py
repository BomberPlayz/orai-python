hengerur,eletkor=int(input("Adja meg a hengerűrtartalmát: ")),int(input("Vezető életkora: "))
dij=(hengerur > 2000 and 10000 or hengerur > 1000 and 7000 or 5000)*(eletkor>35 and 0.8 or 1)
print("Bizosítás díja:",dij)