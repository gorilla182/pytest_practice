import pytest

@pytest.mark.regression
def test_setting_access(admin_user):
    assert admin_user.role == "admin"
