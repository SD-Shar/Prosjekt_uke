
from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask (__name__)

@app.route("/")
def index():
    return redirect("/overview")

def get_connection():
    return mysql.connector.connect(
        host="10.200.14.11",
        user="absolute_solver",
        password="silly",
        database="drone_db"
    )

# mycursor.execute("CREATE TABLE workerD (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), status VARCHAR(255))")
# mycursor.execute("CREATE TABLE disassemblyD (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), status VARCHAR(255))")

# OVERVIEW OF THE SITE

@app.route('/overview')
def drones():
    
    mydb = get_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM workerD")
    workerD = mycursor.fetchall() #liste??
    
    mycursor.execute("SELECT * FROM disassemblyD")
    disassemblyD = mycursor.fetchall() #liste??
    
    return render_template('overview.html', workerD=workerD, disassemblyD=disassemblyD)



# WORKER DRONES

@app.route("/overview/add_WD", methods=["GET", "POST"])
def add_WD():
    
    if request.method == "POST":
        name = request.form["name"]
        status = request.form["status"]
        
        mydb = get_connection()
        
        mycursor = mydb.cursor()
        mycursor.execute(
            "INSERT INTO workerD (name, status) VALUES (%s, %s)", (name, status))
        mydb.commit()
        return redirect("/overview")
    return render_template("add_WD.html")


    
@app.route("/overview/edit_WD/<int:cid>")
def edit_WD(cid):
    
    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id, name, status FROM workerD WHERE id=%s",(cid,))
    kunder = cursor.fetchone()
    mydb.close()
    return render_template("edit_WD.html", kunder = kunder)



@app.route("/overview/update_WD", methods=["POST"])
def update_WD():
    cid = request.form["id"]
    name = request.form["name"]
    status = request.form["status"]
    
    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute("UPDATE workerD SET name=%s, status=%s WHERE id=%s", (name, status, cid))
    mydb.commit()
    mydb.close()
    return redirect("/overview")



@app.route('/overview/delete_WD/<int:cid>')

def delete_WD(cid):
    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM workerD WHERE id=%s", (cid,))
    mydb.commit()
    mydb.close()
    return redirect('/overview')
    

# DISASSEMBLY DRONES

import random
# s er listen av number, x_pos står for x position som velger random plass i listen,
# så settes x_pos inn i s
def serialNumber():
    s = list(''.join(random.choice('01') for _ in range(9)))
    x_pos = random.randrange(9)
    s[x_pos]= 'X'
    return ''.join(s)

@app.route("/overview/add_DD", methods=["GET", "POST"])
def add_DD():
    
    if request.method == "POST":
        name = request.form["name"]
        number = serialNumber()
        status = request.form["status"]
        
        mydb = get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(
            "INSERT INTO disassemblyD (name, serial, status) VALUES (%s, %s, %s)", (name, number, status))
        mydb.commit()
        return redirect("/overview")
    return render_template("add_DD.html")



@app.route("/overview/edit_DD/<int:cid>")
def edit_DD(cid):
    
    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id, name, serial, status FROM disassemblyD WHERE id=%s",(cid,))
    kunder = cursor.fetchone()
    mydb.close()
    return render_template("edit_DD.html", kunder = kunder)
    
    
@app.route("/overview/update_DD", methods=["POST"])
def update_DD():
    cid = request.form["id"]
    name = request.form["name"]
    status = request.form["status"]
    
    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute("UPDATE disassemblyD SET name=%s, status=%s WHERE id=%s", (name, status, cid))
    mydb.commit()
    mydb.close()
    return redirect("/overview")



@app.route('/overview/delete_DD/<int:cid>')
def delete_DD(cid):
    
    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM disassemblyD WHERE id=%s", (cid,))
    mydb.commit()
    mydb.close()
    return redirect('/overview')

if __name__ == "__main__":
    app.run(debug=True)