import sqlite3
import json

jobs = []
con = sqlite3.connect(r"c:\classroom\mar16\hr.db")
cur = con.cursor()
cur.execute("select * from jobs")

for row in cur.fetchall():
    jobs.append({'id': row[0], 'title': row[1], 'minsalary': row[2]})

f = open("jobs.json", "wt")
json.dump(jobs, f)
print("Wrote jobs to jobs.json")
con.close()
