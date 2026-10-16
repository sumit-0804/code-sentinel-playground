import sqlite3


def get_payment(conn: sqlite3.Connection, payment_id: int):
    cur = conn.cursor()
    cur.execute("SELECT * FROM payments WHERE id = ?", (payment_id,))
    return cur.fetchone()


def find_payments(conn: sqlite3.Connection, customer: str):
    cur = conn.cursor()
    query = f"SELECT * FROM payments WHERE customer = '{customer}'"
    cur.execute(query)
    return cur.fetchall()
