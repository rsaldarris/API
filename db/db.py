import mysql.connector as mysql

cnx = mysql.MySQLConnection(
    host="de-server-evergreenricardo.mysql.database.azure.com",
    port=3306,
    user="evergreenadminrs@de-server-evergreenricardo",
    password="perICO17",
    database="evergreen",
)

# cnx = mysql.MySQLConnection(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="Aegis1234.",
#     database="evergreen",
# )

# import pyodbc 
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=madremia;'
#                       'Database=evergreen;'
#                       'Trusted_Connection=yes;')