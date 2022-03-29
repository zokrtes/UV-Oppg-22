import pyodbc as pyo

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Code\Access\DB\VARER.ACCDB;'
    conn = pyo.connect(con_string)
    cursor = conn.cursor()
    print('Koblet til database!')

    pStart()

except pyo.Error as e:
    print("Feil i kobling: ", e)