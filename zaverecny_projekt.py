import sqlite3


conn = sqlite3.connect('evidence_pojistenych.db')


c = conn.cursor()


def vypis_vsechno():
    print("JMENO" + "\t\t" + "PRIJMENI" + "\t" + "VEK" + "\t\t\t" + "EMAIL" + "\t\t\t" + "TELEFON")
    print("----" + "\t\t" + "--------" + "\t" + "------" + "\t\t\t" + "---" + "\t\t\t" + "-------")
    c.execute("SELECT * FROM klient") 
    items = (c.fetchall())
    for item in items:
        print(item[0] + "\t\t" + item[1] + "\t\t" + str(item[2]) + "\t\t" + item[3] + "\t\t" + str(item[4]))




def hledej(jmeno, prijmeni):
    c.execute("SELECT * from klient WHERE jmeno = (?) AND přijmení = (?)", (jmeno, prijmeni))
    items = c.fetchall()

    for item in items:
        print("JMENO" + "\t\t" + "PRIJMENI" + "\t" + "VEK" + "\t\t\t" + "EMAIL" + "\t\t\t" + "TELEFON")
        print("----" + "\t\t" + "--------" + "\t" + "------" + "\t\t\t" + "---" + "\t\t\t" + "-------")


    for item in items:
        print(item[0] + "\t\t" + item[1] + "\t\t" + str(item[2]) + "\t\t" + item[3] + "\t\t" + str(item[4]))


def pridat_klienta():
    jmeno = input("Zadej jméno: ")
    prijmeni = input("Zadej příjmení: ")
    email = input("Zadej email: ")
    vek = input("Zadej věk: ")
    telefon = input("Zadej telefon: ")
        
    c.execute("""
    INSERT INTO klient (jmeno, přijmení, věk, email, telefon)
    VALUES (?,?,?,?, ?)
    """, (jmeno, prijmeni, vek, email, telefon))

    conn.commit ()

    print(f"Přidán nový klient: {jmeno}\t{prijmeni}\t{vek}\t{email}\t{telefon}")


def konec():
    import os
    os.system("cls")






