import sqlite3
import time

def login():
    while True:
        username = input("Entrez votre login: ")
        password = input("Entrez votre mot de passe: ")
        with sqlite3.connect("yourdb.db") as db:
	        cursor = db.cursor()
        find_user = ("SELECT * FROM contact WHERE mail = ? AND phone = ?")
        cursor.execute(find_user, [(mail),(phone)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Bienvenue " +i[2])
                break
        else:
            print ("username ou password erroné !!!")
            encore = input("Essayer encore (o/n): ")
            if encore.lower() =="n" or encore.lower() =="@":
                print("Au revoir ....")
                time.sleep(1)
                break

login()