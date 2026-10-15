import sqlite3


def get_payment(conn: sqlite3.Connection, payment_id: int):
    cur = conn.cursor()
    cur.execute("SELECT * FROM payments WHERE id = ?", (payment_id,))
    return cur.fetchone()


def payment_amount(conn: sqlite3.Connection, payment_id: int) -> int:
    return get_payment(conn, payment_id)[2]
