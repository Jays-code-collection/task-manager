import psycopg2

# Very simple for now, will add verification and complexity later. May not even use psycopg2
class DBAccessor:
    def __init__(
        self,
        cursor,
    ):
        self.cursor = cursor

    def send_query(self, query: str, params: dict = {}):
        # Return requested data if required, otherwise simply execute query
        uppercase = query.upper()
        if "SELECT" in uppercase or "RETURNING" in uppercase:
            return returning_data_query(self.cursor, query, params)
        return non_returning_data_query(self.cursor, query, params)


def returning_data_query(cursor, query: str, params: dict = {}):
    cursor.execute(query, params)
    return cursor.fetchall()


def non_returning_data_query(cursor, query: str, params: dict = {}):
    cursor.execute(query, params)
    return []
