from flask import Flask,render_template,request

app=Flask(__name__)




@app.route("/")
def start():
    return render_template("index.html")




@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":

        name=request.form.get("name")
        password=request.form.get("password")
        print(name,password)
    return render_template("register.html")
@app.route("/login",methods=["GEt","POST"])
def login():
    return render_template("login.html")
























if __name__=="__main__" :
    app.run(debug=True)