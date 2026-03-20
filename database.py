#to use various database in our python we will have to download various modules in python
import sqlite3 as db
conn = db.connect("sms.db")
qry = "Create table if does not exist already: "



conn.close()