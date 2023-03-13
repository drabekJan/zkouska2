import zaverecny_projekt


print("------------------------------------------")
print("Evidence pojištěných")
print("------------------------------------------")
    

print("Vyberte si akci: ")
print("1 - Pridat noveho pojisteneho")
print("2 - Vypsat vsechny pojistene ")
print("3 - Vyhledat pojisteneho ")
print("4 - Konec ")


volba = int(input(""))
print("")
if volba == 4:
    zaverecny_projekt.konec()
elif volba == 3:
    jmeno = input("zadej jmeno: ")
    prijmeni = input("zadej prijmeni: ")


    zaverecny_projekt.hledej(jmeno, prijmeni)
elif volba == 2:
    zaverecny_projekt.vypis_vsechno()
elif volba == 1:
    zaverecny_projekt.pridat_klienta()
else:
    print("Zadej prosím číslo od 1 - 4 pro volbu akce")
    zaverecny_projekt.konec()


