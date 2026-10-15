import sqlite3

from app.payments import get_payment
from app.utils import find_user


def greeting(user_id):
    user = find_user(user_id)
    return "Hello, " + user["name"]


def payment_report(conn: sqlite3.Connection, payment_ids):
    rows = []
    for payment_id in payment_ids:
        rows.append(get_payment(conn, payment_id))
    return rows
