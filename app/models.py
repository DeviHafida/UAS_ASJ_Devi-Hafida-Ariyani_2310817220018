import sqlite3

DB_NAME = 'cerita_horor.db'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS cerita (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                judul TEXT NOT NULL,
                penulis TEXT NOT NULL,
                genre TEXT NOT NULL,
                link_wattpad TEXT NOT NULL
            )
        ''')

def get_all_cerita():
    with get_connection() as conn:
        return conn.execute('SELECT * FROM cerita').fetchall()

def get_cerita_by_id(id):
    with get_connection() as conn:
        return conn.execute('SELECT * FROM cerita WHERE id = ?', (id,)).fetchone()

def add_cerita(judul, penulis, genre, link):
    with get_connection() as conn:
        conn.execute(
            'INSERT INTO cerita (judul, penulis, genre, link_wattpad) VALUES (?, ?, ?, ?)',
            (judul, penulis, genre, link)
        )

def update_cerita(id, judul, penulis, genre, link):
    with get_connection() as conn:
        conn.execute('''
            UPDATE cerita
            SET judul = ?, penulis = ?, genre = ?, link_wattpad = ?
            WHERE id = ?
        ''', (judul, penulis, genre, link, id))

def delete_cerita(id):
    with get_connection() as conn:
        conn.execute('DELETE FROM cerita WHERE id = ?', (id,))
