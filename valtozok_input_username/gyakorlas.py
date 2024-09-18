#1.
elso_szam,masodik_szam = 10, 3.0

# Itt több változót deklarálok egy sorban.
osszeg,kulonbseg,szorzat,hanyados,maradek=elso_szam+masodik_szam,elso_szam-masodik_szam,elso_szam*masodik_szam,elso_szam/masodik_szam,elso_szam%masodik_szam

print(elso_szam, " és ", masodik_szam, " összege: ", osszeg)
print(elso_szam, " és ", masodik_szam, " különbsége: ", kulonbseg)
print(elso_szam, " és ", masodik_szam, " szorzata: ", szorzat)
print(elso_szam, " és ", masodik_szam, " hányadosa: ", hanyados)
print(elso_szam, " és ", masodik_szam, " maradéka: ", maradek)

# 2-3.

# l!sta="..."
# ^ Ez nem fog működni, mert speciális karaktereket nem lehet használni.

# try="..."
# ^ Ez nem fog működni, mert python kulcsszavakat nem lehet változónévnek megadni.

arlista="Alma\t200Ft\nSzilva\t650Ft\nDió\t999Ft"
print(arlista)

# 4.
# Kör kerülete, területe 
# kerület: 2 * r * Pi
# terület: r^2 * Pi
r = 20
PI = 3.142

print("A kör kerülete:", (2*r*PI),"\nA kör területe:", (r**2*PI))