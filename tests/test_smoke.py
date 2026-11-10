import pytest
from my_project import create_app

TABLES = [
    'accounts',
    'devices',
    'accounts_devices',
    'companies',
    'apps',
    'installations',
    'apps_versions',
    'apps_discounts',
    'categories',
    'apps_categories',
    'reviews',
    'payment_cards',
    'bills',
    'library',
]

@pytest.fixture(scope='module')
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

@pytest.mark.parametrize('table', TABLES)
def test_get_all_returns_list(client, table):
    response = client.get(f'/{table}')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
