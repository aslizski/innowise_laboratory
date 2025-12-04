import sqlite3


def run_query(db_path, query):
    """
    Runs a SQL query and returns all fetched results.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def execute_script(db_path, script_path):
    """
    Executes all SQL commands from a .sql file.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(script_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
