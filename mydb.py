# install Mysql on your computer
# pip install django
# pip install mysql
# pip install mysql-connector or pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'onetwothree'
)

# prepare a cursot object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All done!")