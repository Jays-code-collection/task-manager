import pytest

import psycopg2


@pytest.fixture
def lucky_number():
    yield 42


@pytest.fixture
def connection():
    conn = psycopg2.connect(
        host="YOUR MACHINE HERE",  # Need to change this to your machines name
        database="postgres",
        user="postgres",
        password="postgres",
    )
    yield conn
    conn.close()


@pytest.fixture
def cursor(connection):
    cursor = connection.cursor()
    yield cursor
    cursor.close()


@pytest.fixture
def fetch_all_rows_query():
    yield "SELECT * FROM test ORDER BY numbers"
