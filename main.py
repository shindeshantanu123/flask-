from flask import *
from DBM import * 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/new")
def new_user():
    return render_template("register.html")

@app.route("/home")
def profile():
    return render_template("profile.html")

@app.route("/addEmp",methods=["POST"])
def add_emp():
    ids = request.form["id"]#request
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    passw=request.form["passw"]

    t=(ids,name,contact,email,passw)
    addEmp(t)
    return redirect("/")

@app.route("/emplist")
def emp_list():
    data = selectAllEmp()
    return render_template("emplist.html",elist=data)



@app.route("/lg",methods=["POST"])
def lg():
    name=request.form["uname"]
    passw=request.form["password"]
    t=(name,passw)
    t1=log(t)
    if t in t1:
       return redirect("/home")
    else:
        return redirect("/")

@app.route("/deleteEmp")
def delete_emp():
    ids = request.args.get("id")
    deleteEmp(ids)
    return redirect("emplist")

@app.route("/editEmp")
def edit_emp():
    ids = request.args.get("id")
    data = selectEmpById(ids)
    return render_template("update.html", row=data)


@app.route("/updateEmp", methods=["POST"])
def update_emp():
    ids = request.form["id"]#request
    name = request.form["name"]
    contact = request.form["contact"]
    email = request.form["email"]
    passw = request.form["passw"]

    t= (name, contact, email, passw, ids)
    updateEmp(t)
    return redirect("emplist")




if __name__ == "__main__":
    app.run(debug=True)


