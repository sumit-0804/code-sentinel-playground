import sqlite3

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"


def get_payment(conn: sqlite3.Connection, payment_id: int):
    cur = conn.cursor()
    cur.execute("SELECT * FROM payments WHERE id = ?", (payment_id,))
    return cur.fetchone()


def search_payments(conn, customer):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM payments WHERE customer = '{customer}'")
    return cur.fetchall()
