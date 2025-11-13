
from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask (__name__)


mydb = mysql.connector.connect(
    host="10.200.14.11",
    user="absolute_solver",
    password="silly",
    database="drone_db"
)
mycursor = mydb.cursor

# mycursor.execute("CREATE TABLE workerD (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), status VARCHAR(255))")
# mycursor.execute("CREATE TABLE disassemblyD (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), status VARCHAR(255))")

# OVERVIEW OF THE SITE

@app.route('/overview')
def drones():
    
    mydb = mysql.connector.connect(
    host="10.200.14.11",
    user="absolute_solver",
    password="silly",
    database="drone_db"
)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM workerD")
    workerD = mycursor.fetchall() #liste??
    
    mycursor.execute("SELECT * FROM disassemblyD")
    disassemblyD = mycursor.fetchall() #liste??
    
    return render_template('overview.html', workerD=workerD, disassemblyD=disassemblyD)



# WORKER DRONES

@app.route("/overview/add_wd", methods=["GET", "POST"])
def add_WD():
    
    if request.method == "POST":
        name = request.form["name"]
        status = request.form["status"]
        
        mydb = mysql.connector.connect(
        host="10.200.14.11",
        user="absolute_solver",
        password="silly",
        database="drone_db"
    )
        mycursor = mydb.cursor()
        mycursor.execute(
            "INSERT INTO workerD (name, status) VALUES (%s, %s)", (name, status))
        mydb.commit()
        return redirect("/overview")
    return render_template("add_WD.html")


    
@app.route("/overview/edit_WD/<int:cid>")
def edit_WD(cid):
    
    mydb = mysql.connector.connect(
    host="10.200.14.11",
    user="absolute_solver",
    password="silly",
    database="drone_db"
) 
    cursor = mydb.cursor()
    cursor.execute("SELECT id, name, address FROM workerD WHERE id=%s",(cid,))
    kunder = cursor.fetchone()
    mydb.close()
    return render_template("edit_Wdrones.html", kunder = kunder)


@app.route('/overview/delete_WD/<int:cid>')

def delete_WD(cid):
    mydb = mysql.connector.connect(
    host="10.200.14.11",
    user="absolute_solver",
    password="silly",
    database="drone_db"
) 
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM workerD WHERE id=%s", (cid,))
    mydb.commit()
    mydb.close()
    return redirect('/overview')
    

# DISASSEMBLY DRONES

@app.route("/overview/add_dd", methods=["GET", "POST"])
def add_DD():
    
    if request.method == "POST":
        name = request.form["name"]
        status = request.form["status"]
        
        mydb = mysql.connector.connect(
        host="10.200.14.11",
        user="absolute_solver",
        password="silly",
        database="drone_db"
    )
        mycursor = mydb.cursor()
        mycursor.execute(
            "INSERT INTO disassemblyD (name, status) VALUES (%s, %s)", (name, status))
        mydb.commit()
        return redirect("/overview")
    return render_template("add_DD.html")



@app.route("/overview/edit_DD/<int:cid>")
def edit_DD(cid):
    
    mydb = mysql.connector.connect(
    host="10.200.14.11",
    user="absolute_solver",
    password="silly",
    database="drone_db"
) 
    cursor = mydb.cursor()
    cursor.execute("SELECT id, name, address FROM disassemblyD WHERE id=%s",(cid,))
    kunder = cursor.fetchone()
    mydb.close()
    return render_template("edit_Ddrones.html", kunder = kunder)
    
    

@app.route('/overview/delete_DD/<int:cid>')
def delete_DD(cid):
    
    mydb = mysql.connector.connect(
    host="10.200.14.11",
    user="absolute_solver",
    password="silly",
    database="drone_db"
) 
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM disassemblyD WHERE id=%s", (cid,))
    mydb.commit()
    mydb.close()
    return redirect('/overview')

if __name__ == "__main__":
    app.run(debug=True)