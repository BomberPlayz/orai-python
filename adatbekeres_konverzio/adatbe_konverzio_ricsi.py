# 1. Kiíratás
print('Sándor','József','Benedek', sep="\n")
# 2. Felhasználó üdvözlése
username = input("Üdv! Kérlek add meg a neved: ")
print("Szép napot kívánunk, "+username+"! Remélem szép napod van!")
# 3. Kassza
x,y,z=int(input("szaz?? "))*100,int(input("ketszaz?? "))*200,int(input("otszaz?? "))*500;print("Kassza tartalma: "+str(x+y+z))
# 4. Számológép egészekkel
x,y=int(input("első:")),int(input("második:"));print("Összeadás:",x+y,"kivonás:",x-y,"szorzás:",x*y,"osztás:",x/y,"maradékos:",x%y)
# 5. ^ csak valós számokkal
x,y=float(input("első:")),float(input("második:"));print("Összeadás:",x+y,"kivonás:",x-y,"szorzás:",x*y,"osztás:",x/y,"maradékos:",x%y)
# 6. hatványok
a=float(input("Minek a hatványát: "));b=float(input("Másik szám:"));print("Négyzete:",a**2,"Köb:",a**3,"Saját:",a**b)
# 7. téglalap
w,h=float(input("X: ")),float(input("Y: "))
print("Kerület:",w*2+h*2,"Terület",w*h)
# 8. életkor
jelen_ev,szuletesi_ev=2024,int(input("Születési éved: "))
print("Ennyi éves vagy:",jelen_ev-szuletesi_ev)
# 9. Átlag
szamok=[]
for i in range(3):
    szamok.append(float(input(str(i+1)+". szám: ")))
atlag = 0
for szam in szamok:
    atlag+=szam
atlag/=len(szamok)
print("A számok átlaga: "+str(atlag))
# 10. autó
nev,max_sebesseg,orszag=input("Az autó neve: "),input("Az autó végsebessége: "),input("Az autó gyártási országa: ")
print("A(z)",nev,"egy remek gépkocsi, egy elképesztő",max_sebesseg,"km/h végsebességgel. A járművet",orszag,"-ban gyártják.")