import pytest

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def is_admin(self):
        return self.role == "admin"

@pytest.fixture(scope="module")
def admin_user():
    return User(name='Admin', role='admin')
