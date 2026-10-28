import sqlite3

conn = sqlite3.connect("day27.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS departments")
cur.execute("CREATE TABLE departments(id INTEGER, name TEXT)")
cur.execute("DROP TABLE IF EXISTS employees")
cur.execute("CREATE TABLE employees(id INTEGER, name TEXT, dept_id INTEGER, salary INTEGER)")
cur.execute("INSERT INTO departments VALUES(1, '営業')")
cur.execute("INSERT INTO departments VALUES(2, '開発')")
cur.execute("INSERT INTO employees VALUES(1, '田中', 1, 300000)")
cur.execute("INSERT INTO employees VALUES(2, '佐藤', 2, 250000)")
cur.execute("INSERT INTO employees VALUES(3, '鈴木', 1, 280000)")
cur.execute("SELECT * FROM departments")
print(cur.fetchall())
cur.execute("SELECT * FROM employees")
print(cur.fetchall())
cur.execute("""SELECT e.name, d.name
                FROM employees AS e
                INNER JOIN departments AS d ON e.dept_id = d.id                
                """)
print(cur.fetchall())
cur.execute("""SELECT d.name, COUNT(*), SUM(e.salary), AVG(e.salary)
                FROM employees AS e
                INNER JOIN departments AS d ON e.dept_id = d.id
                GROUP BY d.name                
                """)
print(cur.fetchall())
cur.execute("INSERT INTO employees VALUES(4, '高橋', 2, 270000)")
cur.execute("UPDATE employees SET salary == 320000 WHERE name = '田中'")
cur.execute("DELETE FROM employees WHERE name = '鈴木'")
cur.execute("SELECT * FROM employees")
print(cur.fetchall())

conn.commit()
conn.close()