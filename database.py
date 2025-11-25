import mysql.connector
from mysql.connector import Error

def abrir_database():
    return mysql.connector.connect(
        host="190.228.29.68",
        user="g24",
        password="Enero01..",
        database="saig24", "cadenag24",     # O la BD que necesites
        autocommit=True
    )

