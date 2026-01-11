import sqlite3

def init_db():
    conn = sqlite3.connect("replies.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS replies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            comment TEXT,
            reply TEXT
        )
    """)

    conn.commit()
    conn.close()
