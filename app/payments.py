import sqlite3


def get_payment(conn: sqlite3.Connection, payment_id: int):
    cur = conn.cursor()
    cur.execute("SELECT * FROM payments WHERE id = ?", (payment_id,))
    return cur.fetchone()


def find_payments(conn: sqlite3.Connection, customer: str):
    """Finds all payments associated with a customer.

    Args:
        conn (sqlite3.Connection): The database connection.
        customer (str): The customer identifier.

    Returns:
        list: A list of payment records matching the customer.
    """
    cur = conn.cursor()
    query = "SELECT * FROM payments WHERE customer = ?"
    cur.execute(query, (customer,))
    return cur.fetchall()
