import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="social_user",
        password="1234",
        database="social_network",
        ssl_disabled=True
    )
