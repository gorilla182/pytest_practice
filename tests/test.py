import pytest

# Этот список используется для подсчета вызовов фикстуры
call_log = []


@pytest.fixture(scope="function")
def transaction_data():
    call_log.append(1)
    return {"id": 123}

@pytest.mark.function
def test_one(transaction_data):
    assert transaction_data['id'] == 123

@pytest.mark.function
def test_two(transaction_data):
    assert transaction_data['id'] == 123

@pytest.mark.function
def test_fixture_called_once():
    assert len(call_log) == 2


@pytest.fixture(scope="session")
def db_connection():
    call_log.append(1)
    return "connection string"

@pytest.mark.session
def test_users(db_connection):
    assert db_connection == "connection string"

@pytest.mark.session
def test_products(db_connection):
    assert db_connection == "connection string"

@pytest.mark.session
def test_fixture():
    assert len(call_log) == 1