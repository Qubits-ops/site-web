
from flask import *
from datetime import *
from Bdd import *
from flask_mail import Mail, Message

app = Flask(__name__)
#mail= Mail(app)

"""app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'neuralink.pro@gmail.com'
app.config['MAIL_PASSWORD'] = 'Neura9807!!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)"""


@app.route("/")
def Formulaire():
    return render_template("formulaire.html")
@app.route("/recherche")
def recherche():

    return render_template("recherche.html")
@app.route("/hack",methods=['GET','POST'])
def hack():
    dechiffrage = request.form.get('dechi')
    if dechiffrage == "Piratage":
        pirates = pirate()
        return render_template("hack2.html",pirates=pirates)
    else:
        return "pas le bon dechiffrage"

@app.route("/secret",methods=['GET','POST'])
def secret():
    secrets = request.form.get('secret')
    if secrets == "Pirate":
        return render_template("hack.html")
    else:
        return render_template("recherche.html")

@app.route("/site",methods=['GET','POST'])
def bienvenue():
    nom_user = request.form["nom"]
    password = request.form["pass"]
    email = request.form["mail"]
    session_actu(nom_user,password,email)
    date_du_jour2 = datetime.utcnow()

    return render_template("index.html",date=date_du_jour2,nom=nom_user)
@app.route("/acceuil")
def acceuil():

    return render_template("acceuil.html")
@app.route("/puces")
def puces():
    return render_template("puces.html")
@app.route("/new")
def new():
    return render_template("explication.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, debug=True)
    
