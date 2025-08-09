import sqlite3
from datetime import datetime

def log_query(form_data, raw_html):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, case_type TEXT, case_number TEXT, year TEXT, time TEXT, raw_response TEXT)''')
    c.execute("INSERT INTO logs (case_type, case_number, year, time, raw_response) VALUES (?, ?, ?, ?, ?)",
              (form_data['case_type'], form_data['case_number'], form_data['year'], datetime.now(), raw_html))
    conn.commit()
    conn.close()
