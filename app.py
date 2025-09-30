from flask import Flask, render_template
import os, socket, getpass
from datetime import datetime
import platform

app = Flask(__name__)

@app.route("/")
def index():
    usuario = os.environ.get("USER") or getpass.getuser() 
    carpeta = os.getcwd()
    so = platform.system() + " " + platform.release()
    ip_local = socket.gethostbyname(socket.gethostname())
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html",
                           usuario=usuario,
                           carpeta=carpeta,
                           so=so,
                           ip_local=ip_local,
                           fecha_hora=fecha_hora)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

