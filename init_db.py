import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_type TEXT,
    case_number TEXT,
    year TEXT,
    parties TEXT,
    filing_date TEXT,
    hearing_date TEXT,
    pdf_link TEXT
)''')

c.execute('''
INSERT INTO cases (case_type, case_number, year, parties, filing_date, hearing_date, pdf_link)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    'W.P.(C)', '7425', '2019',
    'Akshay Kumar vs Govt. of Delhi',
    '2019-05-14',
    '2025-08-10',
    'https://example.com/order7425.pdf'
))

conn.commit()
conn.close()
