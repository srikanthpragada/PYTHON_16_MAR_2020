import sqlite3

con = sqlite3.connect(r"c:\classroom\mar16\hr.db")
cur = con.cursor()

title = input("Enter job title : ")
minsalary = int(input("Enter min salary :"))

try:
    cur.execute("insert into jobs(title, minsalary) values(?,?)", (title, minsalary))

    if cur.rowcount == 1:
        print("Added Job Successfully!")
        con.commit()

except Exception as ex:
    print("Error : ", ex)

con.close()
