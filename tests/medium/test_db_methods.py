from unittest import result
import pytest

from backend.db_access import send_query


@pytest.mark.medium
def test_get_all_data(cursor, fetch_all_rows_query):
    # GIVEN / WHEN
    result = send_query(cursor, fetch_all_rows_query)

    # THEN
    assert result
    assert len(result) == 6
    assert result[0] == (3, "Unlucky")


@pytest.mark.medium
def test_delete_query(cursor, fetch_all_rows_query):
    # GIVEN / WHEN
    before = send_query(cursor, fetch_all_rows_query)
    send_query(cursor, "DELETE FROM test WHERE numbers = 3")
    after = send_query(cursor, fetch_all_rows_query)

    # THEN
    assert len(before) - 1 == len(after)
    for row in after:
        if row[0] == 3:
            assert False


@pytest.mark.medium
def test_insert_query(cursor, fetch_all_rows_query):
    # GIVEN / WHEN
    before = send_query(cursor, fetch_all_rows_query)
    send_query(cursor, "INSERT INTO test (numbers, luckiness) VALUES (1, 'Unlucky');")
    after = send_query(cursor, fetch_all_rows_query)

    # THEN
    assert len(before) + 1 == len(after)
    assert after[0] == (1, "Unlucky")


@pytest.mark.medium
def test_update_query(cursor, fetch_all_rows_query):
    # GIVEN / WHEN
    before = send_query(cursor, fetch_all_rows_query)
    send_query(cursor, "UPDATE test SET luckiness = 'Lucky' WHERE numbers = '77';")
    after = send_query(cursor, fetch_all_rows_query)

    # THEN
    assert before[3] == (77, "Neutral")
    assert after[3] == (77, "Lucky")
