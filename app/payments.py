import sqlite3


def get_payment(conn: sqlite3.Connection, payment_id: int):
    cur = conn.cursor()
    cur.execute("SELECT * FROM payments WHERE id = ?", (payment_id,))
    return cur.fetchone()


def find_payments(conn: sqlite3.Connection, customer: str):
    """Finds payments for a given customer."""
    cur = conn.cursor()
    query = "SELECT * FROM payments WHERE customer = ?"
    cur.execute(query, (customer,))
    return cur.fetchall()
