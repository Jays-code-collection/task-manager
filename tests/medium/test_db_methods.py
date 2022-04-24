from unittest import result
import pytest

from backend.db_access import DBAccessor


@pytest.mark.medium
def test_get_all_data(cursor, fetch_all_rows_query):
    # GIVEN
    db = DBAccessor(cursor)

    # WHEN
    result = db.send_query(fetch_all_rows_query)

    # THEN
    assert result
    assert len(result) == 6
    assert result[0] == (3, "Unlucky")


@pytest.mark.medium
def test_delete_query(cursor, fetch_all_rows_query):
    # GIVEN
    db = DBAccessor(cursor)

    # WHEN
    before = db.send_query(fetch_all_rows_query)
    db.send_query("DELETE FROM test WHERE numbers = 3")
    after = db.send_query(fetch_all_rows_query)

    # THEN
    assert len(before) - 1 == len(after)
    for row in after:
        if row[0] == 3:
            assert False


@pytest.mark.medium
def test_insert_query(cursor, fetch_all_rows_query):
    # GIVEN
    db = DBAccessor(cursor)

    # WHEN
    before = db.send_query(fetch_all_rows_query)
    db.send_query("INSERT INTO test (numbers, luckiness) VALUES (1, 'Unlucky');")
    after = db.send_query(fetch_all_rows_query)

    # THEN
    assert len(before) + 1 == len(after)
    assert after[0] == (1, "Unlucky")


@pytest.mark.medium
def test_update_query(cursor, fetch_all_rows_query):
    db = DBAccessor(cursor)

    # WHEN
    before = db.send_query(fetch_all_rows_query)
    db.send_query("UPDATE test SET luckiness = 'Lucky' WHERE numbers = '77';")
    after = db.send_query(fetch_all_rows_query)

    # THEN
    assert before[3] == (77, "Neutral")
    assert after[3] == (77, "Lucky")
