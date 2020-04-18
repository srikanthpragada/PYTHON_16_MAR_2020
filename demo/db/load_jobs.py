import sqlite3
import json

con = sqlite3.connect(r"c:\classroom\mar16\hr.db")
cur = con.cursor()

f = open("newjobs.json", "rt")
jobs = json.load(f)

count = 0
for job in jobs:
    try:
        cur.execute("insert into jobs(title, minsalary) values(?,?)",
                    (job['title'], job['minsalary']))
        count += 1
    except Exception as ex:
        pass

con.commit()
print(f"Loaded {count}  job(s)")
con.close()
