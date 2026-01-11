import sqlite3
from ai.reply_generator import generate_reply

def process_comments(comments):
    conn = sqlite3.connect("replies.db")
    cursor = conn.cursor()

    for item in comments:
        reply = generate_reply(item["comment"])

        cursor.execute("""
            INSERT INTO replies (user, comment, reply)
            VALUES (?, ?, ?)
        """, (item["user"], item["comment"], reply))

        print(f"Replied to {item['user']}: {reply}")

    conn.commit()
    conn.close()
