import sqlite3

def fetch_case_details(case_type, case_number, year):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT parties, filing_date, hearing_date, pdf_link FROM cases WHERE case_type=? AND case_number=? AND year=?", 
              (case_type, case_number, year))
    rows = c.fetchall()
    conn.close()
    
    if rows:
        result_list = []
        for row in rows:
            result_list.append({
                'parties': row[0],
                'filing_date': row[1],
                'hearing_date': row[2],
                'pdf_link': row[3]
            })

        return {
            'results': result_list,
            'error': None
        }
    else:
        return {
            'error': 'No matching case found in DB',
            'results': []
        }
