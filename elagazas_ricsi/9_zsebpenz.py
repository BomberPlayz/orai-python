penz=3500
print("VÁLASZTÉK:")
print("Zserbó - 800Ft")
print("epertorta - 950Ft")
print("kókuszkocka - 790Ft")

suti_1,suti_1_szam = int(input("Első süti ára: ")),int(input("Első süti darabszáma: "))
suti_2,suti_2_szam = int(input("Második süti ára: ")),int(input("Második süti darabszáma: "))

koltes = suti_1*suti_1_szam+suti_2*suti_2_szam
print(koltes > penz and "Nincs annyi pénze!" or ("Költés: "+str(koltes)+". Maradt ennyi: "+str(penz-koltes)))
