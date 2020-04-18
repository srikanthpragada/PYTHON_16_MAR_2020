import sqlite3

con = sqlite3.connect(r"c:\classroom\mar16\hr.db")
cur = con.cursor()

id = int(input("Enter job id : "))
minsalary = int(input("Enter min salary :"))

try:
    cur.execute("update jobs set minsalary = ? where id = ?", (minsalary, id) )

    if cur.rowcount == 1:
        print("Updated Job Successfully!")
        con.commit()
    else:
        print("Job Id Not Found!")

except Exception as ex:
    print("Error : ", ex)

con.close()
