import sqlite3

def run_query(cursor, query, params=()):
    """
    Execute a single SQL query.
    """
    cursor.execute(query, params)

def run_many(cursor, query, data):
    """
    Execute a query multiple times with a list of data.
    """
    cursor.executemany(query, data)

def table_empty(cursor, count_query):
    """
    Check if a table is empty.
    Returns True if the table has no rows.
    """
    cursor.execute(count_query)
    return cursor.fetchone()[0] == 0

def fetch_all(cursor, select_query, params=()):
    """
    Execute a SELECT query and return all results as a list of tuples.
    """
    cursor.execute(select_query, params)
    return cursor.fetchall()
