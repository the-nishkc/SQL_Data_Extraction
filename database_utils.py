import sqlite3
import pandas as pd


def connect_db():
    return sqlite3.connect("supermarket.db")


def execute_query(query):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    return rows


def load_dataframe(query):
    conn = connect_db()

    df = pd.read_sql(query, conn)

    conn.close()

    return df