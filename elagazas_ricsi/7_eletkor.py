nev,kor=input("Neved: "),int(input("korod: "))
(kor < 1 or kor > 100) and (print("Kornak 1-100 közt kell lennie") or exit())

if kor > 90:
    print(nev, kor,"éves agg")
elif kor > 60:
    print(nev, kor,"éves öreg")
elif kor > 40:
    print(nev, kor,"éves középkorú")
elif kor > 15:
    print(nev, kor,"éves fiatal felnőtt")
elif kor >= 1:
    print(nev, kor,"éves gyerek")