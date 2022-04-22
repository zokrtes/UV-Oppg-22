import pyodbc as pyo
import os


def clear():
    os.system('cls')

# Funskjon for å skrive hovedmenyen til skjerm
def skriv_meny():
    print("\nHovedmeny for beregning av areal\n")
    print("1. Alle medlemmer")
    print("2. Vis alle registrert info om et enkelt medlem")
    print("3. Spørringer")
    print("4. Vedlikehold medlemmer")
    print("5. Vedlikehold")
    print("6. Avslutt")

def undermeny3():
    print("Undermeny\n")
    print("3.1. Lag en liste over medlemmer som ikke har betalt medlemskontingenten")
    print("3.2. Lag en liste over medlemmer som er pensjonister, eldre enn 67 år")
    print("3.3. Lag en liste over unge voksne, de som er mellom 18 og 30 år gamle")
    print("3.4. Lag en liste over alle medlemmer som er eldre enn en viss alder. Denne alderen skal skrives inn hver gang spørringen kjøres")
    print("3.5. Lag en medlemsliste overde som bor på et valgfritt sted")
    print("3.6. Lag en spørring som viser gjennomsnittlig alder for alle medlemmene")
    print("3.7. Lag en liste over de som bor i Vestfold og Telemark")
    print("3.8. Tilbake til Hovedmenyen")

def undermeny4():
    print("Undermeny\n")
    print("4.1.Legg til et nytt medlem")
    print("4.2.Slett et medlem")
    print("4.3.Registrere om et medlem harbetalt kontigenten")
    print("4.4.Endre data for et medlem, f.eks. endre adresse")
    print("4.5.Tilbake til Hovedmenyen")

def undermeny5():
    print("Undermeny\n")
    print("5.1.Legg til en medlemstype (Fullt medlem, støttemedlem osv)")
    print("5.2.Slett en medlemstype")
    print("5.3.Øk kontingentenmed 10%")
    print("5.4.Skrive medlemslisten ut til en csv-fil")
    print("5.5.Tilbake til Hovedmenyen")

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\repo\UV-Oppg-22\Medlemsregister.accdb;'
    conn = pyo.connect(con_string)
    cursor = conn.cursor()
    print('Koblet til database!')

    
    clear()
    skriv_meny()

    bla="Start"
    
    ans=input("Hva ønsker du å gjøre. Velg tall? ") 

    # dette er funksjonen som henter ut alle medlemmer
    if ans=="1":
        clear()

    elif ans=="2":
        clear()


    elif ans=="3":
        clear()

        undermeny3()
        bla=input("Hva ønsker du å gjøre. Velg tall? ") 

        if bla == "3.1":
            clear()
            
        elif bla == "3.2":
            clear()
            
        elif bla == "3.3":
            clear()
            
        elif bla == "3.4":
            clear()

        elif bla == "3.5":
            clear()

        elif bla == "3.6":
            clear()

        elif bla == "3.7":
            clear()

        elif bla == "3.8":
            clear()
        
        if bla != "3.8":
            venter=input("Trykk ENTER for å fortsette!")   

    elif ans=="4":
        clear()

        undermeny4()
        bla=input("Hva ønsker du å gjøre. Velg tall? ")
        mine_medlemmer = (
            (34,"Martin","Leerstang", "Bergsbygdavegen 695", "3949", "11111111", "97493561", "marblee@online.no", "07.02.04", "1", False)
        )

        cursor.executemany("INSERT INTO medlemmer VALUES (?,?,?,?,?,?,?,?,?,?,?)",mine_medlemmer)
        conn.commit()
    
        print("Data lagt til!")

        if bla == "4.1":
            clear()
            print("\nHer kan du legge til en ny medlem")

            medlemsid=input("Legg til medlemsID: ")
            fornavn=input("Legg til fornavn: ")
            etternavn=input("Legg til etternarvn: ")
            adresse=input("Legg til adresse: ")
            postnr=input("Legg til postnr: ")
            tlf=input("Legg til telefon nummer: ")
            mobil=input("Legg til mobil nummer: ")
            epost=input("Legg til E-post: ")
            fødselsdato=input("Legg til fødselsdato: ")
            medlemstype=input("Legg til medlemstype (1 eller 2): ")
            betalt=input("Legg til om brukeren har betalt eller ikke (True eller False): ")

            cursor.executemany(f"INSERT INTO medlemmer VALUES '{medlemsid}', '{fornavn}', '{etternavn}', '{adresse}', '{postnr}', '{tlf}', '{mobil}', '{epost}', '{fødselsdato}', '{medlemstype}''{betalt}'",mine_medlemmer)
            conn.commit()
    
            print("Data lagt til!")

        

        elif bla == "4.2":
            clear()
            print("\nHer kan du slette en medlem")

            medlemsnr=int(input("Oppgi medlemsID til den du ønsker å fjerne: ")) 

            cursor.execute(f"DELETE FROM medlemmer WHERE MedlemsID = ?", (medlemsnr))
            cursor.commit()
            print("Data slettet!")
            
        elif bla == "4.3":
            clear()
            medlemnr=int(input=("Oppgi medlemsID: "))
            betaltendring=input("Har medlemmet betalt kontigenten? True eller False: ")
            
            cursor = conn.cursor()

            cursor.execute(f"UPDATE medlemmer SET betalt = ? WHERE MedlemsID = '{medlemnr}'", (betaltendring))
            cursor.commit()
            print("Data er oppdatert!")
            
        elif bla == "4.4":
            clear()
            medlemnr = 20
            nytt_nummer = "44444444"
            

            cursor = conn.cursor()

            cursor.execute("UPDATE medlemmer SET mobil = ? WHERE MedlemsID = ?", (nytt_nummer, medlemnr))
            cursor.commit()
            print("Data er oppdatert!")

        if bla != "4.5":
            venter=input("Trykk ENTER for å fortsette!")   

    elif ans=="5":
        clear()
        undermeny5()
        bla=input("Hva ønsker du å gjøre. Velg tall? ") 

        if bla == "5.1":
            clear()
            MyTypeID = int(input("Leg til MyTypeID : "))
            MyTypeNavn = input("Legg til MyTypeNavn : ")
            Kontigent = int(input("Legg til kontigent : "))

            cursor = conn.cursor()

            cursor.executemany(f"INSERT INTO medlemstyper VALUES '{MyTypeID}', '{MyTypeNavn}', '{Kontigent}' ")
            cursor.commit()
            print("Data er lagt til!")

        elif bla == "5.2":
            clear()
            medlemstyper_ID=int(input("Oppgi MyTypeID til den du ønsker å fjerne: ")) 

            cursor.execute(f"DELETE FROM medlemstyper WHERE MedlemsID = ?", (medlemstyper_ID))
            cursor.commit()
            print("Data slettet!")

        elif bla == "5.3":
            clear()
            

        elif bla == "5.4":
            clear()

        if bla != "5.5":
            venter=input("Trykk ENTER for å fortsette!")   

    elif ans=="6":
        clear()     
        print("\nTakk for at du brukte areal-programmet! Velkommen igjen!\n")    

    
            
except pyo.Error as e:
    print("Feil i kobling: ", e)
