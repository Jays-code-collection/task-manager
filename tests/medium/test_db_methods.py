import pytest

from backend.db_access import DBAccessor


@pytest.mark.medium
def test_get_all_data(cursor):
    # GIVEN
    db = DBAccessor(cursor)
    fetch_query = "SELECT * FROM test ORDER BY numbers;"

    # WHEN
    result = db.send_query(fetch_query)

    # THEN
    assert result
    assert len(result) == 6
    assert result[0] == (3, "Unlucky")


# cursor.execute('SELECT * from table where id = %(some_id)d', {'some_id': 1234})
# cursor.fetchmany(2) # Limit how many rows selected
# db = DBAccessor(cursor)
# select_all = db.send_query("SELECT * FROM test;")
# print(select_all)

# delete_rows = db.send_query("DELETE FROM test WHERE numbers = 3")
# print(delete_rows)

# select_all = db.send_query("SELECT * FROM test;")
# print(select_all)

# inserted = db.send_query("INSERT INTO test (numbers, luckiness) VALUES (1, 'Unlucky');")
# print(inserted)

# select_all = db.send_query("SELECT * FROM test;")
# print(select_all)

# updated = db.send_query("UPDATE test SET luckiness = 'Lucky' WHERE numbers = '77';")
# print(updated)

# select_all = db.send_query("SELECT * FROM test;")
# print(select_all)

# # DB.commit() need to commit changes for them to be written to the DB

# # Close connection
# cursor.close()
# connection.close()

# Connect to DB
# connection = psycopg2.connect(
#     host="DESKTOP-RAMNUB0",  # Need to change this to your machines name
#     database="postgres",
#     user="postgres",
#     password="postgres",
# )

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM test;")

# for row in cursor.fetchall():
#     print(row)
