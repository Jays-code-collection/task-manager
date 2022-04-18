import pytest

import psycopg2


@pytest.fixture
def lucky_number():
    yield 42


@pytest.fixture
def connection():
    conn = psycopg2.connect(
        host="DESKTOP-RAMNUB0",  # Need to change this to your machines name
        database="postgres",
        user="postgres",
        password="postgres",
    )
    yield conn
    conn.commit()
    conn.close()


@pytest.fixture
def cursor(connection):
    cursor = connection.cursor()
    yield cursor
    cursor.close()
