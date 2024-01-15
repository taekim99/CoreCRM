# install Mysql on your computer
# pip install django
# pip install mysql
# pip install mysql-connector or pip install mysql-connector-python

import mysql.connector

# ! CAHNGE ACCORDING TO YOUR SETTINGS
dataBase = mysql.connector.connect(
    host = '', # Ex: localhost
    user = '', # Ex: root
    passwd = '' # Ex: onetwothreeFourFive
)

# prepare a cursot object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All done!")