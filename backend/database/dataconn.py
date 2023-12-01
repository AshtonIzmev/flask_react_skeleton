import sqlite3
from flask import g

def get_db_conn():
    db_conn = getattr(g, '_db_conn', None)
    if db_conn is None:
        db_conn = g._db_conn = sqlite3.connect('database.db')
        db_conn.row_factory = sqlite3.Row
    return db_conn
