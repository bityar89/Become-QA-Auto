import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists():
    api = GitHub()
    user = api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_non_exists():
    api = GitHub()
    r = api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'