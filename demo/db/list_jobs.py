import sqlite3


con = sqlite3.connect(r"c:\classroom\mar16\hr.db")
cur = con.cursor()
cur.execute("select * from jobs order by minsalary")

for row in cur.fetchall():
    print(f"{row[1]:20} {row[2]:6}")

con.close()
