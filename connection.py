import sqlite3
def create_db():
    con = sqlite3.connect(database = "Result_Manage.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, Name text, Duration text, Charges text, Description text )")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, dob text, contact text, admission text, course text, state text, city text, pin text, address text )")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text, name text, course text, marks_ob text, full_marks text, percent text  )")
    con.commit()




create_db()