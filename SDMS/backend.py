import sqlite3


def studentdatabase():
    con = sqlite3.connect("student.db")
    cur = con.cursor()


def add_data(std_id, std_fn, std_ln, std_dob, std_age, std_gender, std_address, std_phone):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",
        (std_id, std_fn, std_ln, std_dob, std_age, std_gender, std_address, std_phone))
    con.commit()
    con.close()


def display_data():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows


def delete_data(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()


def search_data(std_id="", std_fn="", std_ln="", std_dob="", std_age="", std_gender="", std_address="", std_phone=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM student WHERE std_id=? OR std_fn=? OR std_ln=? OR std_dob=? OR std_age=? OR std_gender=? OR std_address=? OR std_phone=?",
        (std_id, std_fn, std_ln, std_dob, std_age, std_gender, std_address, std_phone))
    rows = cur.fetchall()
    con.close()
    return rows


def update_data(std_id="", std_fn="", std_ln="", std_dob="", std_age="", std_gender="", std_address="", std_phone=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE student SET std_id=? OR std_fn=? OR std_ln=? OR std_dob=? OR std_age=? OR std_gender=? OR std_address=? OR std_phone=?",
        (std_id, std_fn, std_ln, std_dob, std_age, std_gender, std_address, std_phone))
    con.commit()
    con.close()
