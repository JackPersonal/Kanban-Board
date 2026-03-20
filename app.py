from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #default
def index():
    return render_template("board.html"), 200

@app.route("/board") 
def board():
    return render_template("board.html"), 200

#for local host
if __name__ == "__main__":
    app.run("0.0.0.0", port=7652) 