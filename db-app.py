import pyodbc as pyo

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\repo\UV-Oppg-22\Medlemsregister.accdb;'
    conn = pyo.connect(con_string)
    cursor = conn.cursor()
    print('Koblet til database!')
<<<<<<< Updated upstream

    pStart()
=======
    def clear():
        os.system('cls')
>>>>>>> Stashed changes

# Funskjon for å skrive hovedmenyen til skjerm
    def skriv_meny():
        print("\nHovedmeny for beregning av areal\n")
        print("1. Alle medlemmer")
        print("2. Vis alle registrert info om et enkelt medlem")
        print("3. Spørringer")
        print("4. Vedlikehold medlemmer")
        print("5. Vedlikehold")
        print("6. Avslutt")



except pyo.Error as e:
    print("Feil i kobling: ", e)
