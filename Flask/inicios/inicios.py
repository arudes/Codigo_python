from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("index.html")

@app.route("/desarrollo")
def contacto():
    return "Programador Mauricio Maldonado"

@app.route('/poemas')
def poemas():
    return render_template("poemas.html")

#para ejecutar el archivo
if __name__ == "__main__":
    app.run(debug=True)