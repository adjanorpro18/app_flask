# Importations des librairies

from flask import Flask, render_template, request

# Creation de l'application

app = Flask(__name__)

# Creation de page d'accueil de l'application

@app.route("/")
def home():
    return render_template("home.html", message="Flask_App")


#Exécution de l'application

if __name__ == '__main__':
    app.run()
    


