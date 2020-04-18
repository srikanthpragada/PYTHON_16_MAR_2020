import sqlite3

con = sqlite3.connect(r"c:\classroom\mar16\hr.db")
cur = con.cursor()

id = int(input("Enter job id : "))

try:
    cur.execute("delete from jobs where id = ?", (id,))

    if cur.rowcount == 1:
        print("Delete Job Successfully!")
        con.commit()
    else:
        print("Job Id Not Found!")

except Exception as ex:
    print("Error : ", ex)

con.close()
