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

#1adat,     Ez nem fog működni, mert a változó neve nem tartalmazhat vesszőt
#If         Ez működni fog, mert a python változók megkülönböztetik a kis és nagybetűket
#La Pos     Ez nem fog működni, mert a változó neve nem tartalmazhat szóközöket
#ellen?     Ez nem fog működni, mert a változó neve nem tartalmazhat kérdőjelet
#l!sta      Ez nem fog működni, mert a változó neve nem tartalmazhat felkiáltójelet
#(alma)     Ez nem fog működni, mert a változó neve nem tartalmazhat zárójeleket
#try        Ez nem fog működni, mert a változó neve nem tartalmazhat python kulcsszavakat
#Kö_rte     Ez nem fog működni, mert a változó neve nem tartalmazhat ékezetes betűket
#+adat      Ez nem fog működni, mert a változó neve nem tartalmazhat speciális karaktereket mint +, -, *, /
#_print #   Ez nem fog működni, mert a változó neve nem tartalmazhat kettőskeresztet, mert a többi része akkor megjegyzésnek lesz tekintve.
#_, _       Ez nem fog működni, mert a változó neve nem tartalmazhat vesszőt vagy szóközt. Ez azonban elfogadható, ha egy függvény kimenete kettő adatot tartalmaz, és minket egyik sem érdekel, de szeretnénk jelezni, hogy direkt nem rakjuk változóba.
#Q, X%      Ez nem fog működni, mert a változó neve nem tartalmazhat speciális karaktert, szóközt, vesszőt.

arlista="Alma\t200Ft\nSzilva\t650Ft\nDió\t999Ft" 
print(arlista)

# 4.
print("A szövegben aposztróf (') és idézőjel (\") használata is lehetséges, ha ügyik vagyunk :)")

# 5.
# Kör kerülete, területe 
# kerület: 2 * r * Pi
# terület: r^2 * Pi
r = 20
PI = 3.142

print("A kör kerülete:", (2*r*PI), "\nA kör területe:", (r**2*PI))