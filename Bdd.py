import sqlite3
import hashlib
from flask_mail import Mail, Message
from Principal import *


"""def send(email):
   msg = Message('Bienvenue', sender = 'neuralink.pro@gmail.com', recipients = [email])
   msg.body = "Bonjour passer un agreable moment sur le site."
   mail.send(msg)
   return "Sent"
"""

def session_actu(pseudo,password,email):
    passw = password.encode('UTF-8')
    connexion = sqlite3.connect("Bdd/user.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM t_user WHERE pseudo = ? OR mail = ?",(pseudo,email))
    resultat = curseur.fetchall()
    if resultat:
        return "deja enregistrez"
    else:
        curseur.execute("INSERT INTO t_user (pseudo,pass,mail) values(?,?,?)",(pseudo,hashlib.sha256(passw).hexdigest(),email))
        connexion.commit()
    connexion.close()
"""def contacte(nom,email):
    connexion = sqlite3.connect("Bdd/user.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT mail FROM t_user WHERE pseudo = ?",(nom,))
    resultat = curseur.fetchall()
    if resultat:
        send(email)
    else:
        return "user non enregistrer"
    connexion.close()
   """
def pirate():
    connexion = sqlite3.connect("Bdd/user.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM t_user")
    resultat = curseur.fetchall()
    connexion.close()
    return resultat
