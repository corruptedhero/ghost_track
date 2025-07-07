import sqlite3
import datetime

conn = sqlite3.connect("data/ghostbot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS processes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT,
    is_active INTEGER,
    start_time TEXT
)
""")
conn.commit()

def get_processes(user_id):
    cursor.execute("SELECT id, name, is_active FROM processes WHERE user_id = ?", (user_id,))
    return cursor.fetchall()

def toggle_process(pid):
    cursor.execute("SELECT is_active FROM processes WHERE id = ?", (pid,))
    current = cursor.fetchone()
    if not current:
        return
    new_state = 0 if current[0] else 1
    start_time = datetime.datetime.now().isoformat() if new_state else None
    cursor.execute("UPDATE processes SET is_active = ?, start_time = ? WHERE id = ?", (new_state, start_time, pid))
    conn.commit()

def delete_process(pid):
    cursor.execute("DELETE FROM processes WHERE id = ?", (pid,))
    conn.commit()
