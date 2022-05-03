import psycopg2

# Very simple for now, will add verification and complexity later. May not even use psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host="YOUR MACHINE HERE" # Need to change this to your machines name
        database="postgres",
        user="postgres",
        password="postgres",
    )
    return conn


def send_query(cursor, query: str, params: dict = {}):
    # Return requested data if required, otherwise simply execute query
    uppercase = query.upper()
    if "SELECT" in uppercase or "RETURNING" in uppercase:
        return returning_data_query(cursor, query, params)
    return non_returning_data_query(cursor, query, params)


def returning_data_query(cursor, query: str, params: dict = {}):
    cursor.execute(query, params)
    return cursor.fetchall()


def non_returning_data_query(cursor, query: str, params: dict = {}):
    cursor.execute(query, params)
    return []
