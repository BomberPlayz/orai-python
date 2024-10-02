elso_ev,elso_esemeny=int(input("Első évszám: ")),input("Első esemény:")
masodik_ev,masodik_esemeny=int(input("masodik évszám: ")),input("masodik esemény:")

if masodik_ev<elso_ev:
    t=masodik_ev
    masodik_ev=elso_ev
    elso_ev=t

if masodik_ev-elso_ev > 200:
    print("Túl sok év telt el!")
else:
    if masodik_ev>elso_ev:
        print(elso_ev,":",elso_esemeny)
        print(masodik_ev,":",masodik_esemeny)
    else:
        print(masodik_ev,":",masodik_esemeny)
        print(elso_ev,":",elso_esemeny)
