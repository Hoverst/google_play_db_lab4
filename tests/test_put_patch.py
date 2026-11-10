import uuid
import pytest
from my_project import create_app

@pytest.fixture(scope='module')
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

@pytest.fixture
def category_id(client):
    name = f"tmp_cat_{uuid.uuid4().hex[:12]}"
    created = client.post('/categories', json={'name': name})
    assert created.status_code == 201, created.get_json()
    cat_id = created.get_json()['id']
    yield cat_id
    client.delete(f'/categories/{cat_id}')

def test_put_full_body_success(client, category_id):
    new_name = f"put_full_{uuid.uuid4().hex[:8]}"
    response = client.put(f'/categories/{category_id}', json={'name': new_name})
    assert response.status_code == 200
    body = response.get_json()
    assert body['id'] == category_id
    assert body['name'] == new_name

def test_put_missing_field_400(client, category_id):
    response = client.put(f'/categories/{category_id}', json={})
    assert response.status_code == 400
    assert 'Missing required fields' in response.get_json()['error']

def test_put_unknown_field_400(client, category_id):
    response = client.put(
        f'/categories/{category_id}',
        json={'name': 'ok_name', 'unknown_field': 'x'},
    )
    assert response.status_code == 400
    assert 'Unknown fields' in response.get_json()['error']

def test_put_readonly_field_400(client, category_id):
    response = client.put(
        f'/categories/{category_id}',
        json={'name': 'ok_name', 'id': 999},
    )
    assert response.status_code == 400
    assert 'Read-only' in response.get_json()['error']

def test_put_nonexistent_404(client):
    response = client.put('/categories/2147483646', json={'name': 'ghost'})
    assert response.status_code == 404

def test_patch_one_field_others_unchanged(client, category_id):
    before = client.get(f'/categories/{category_id}').get_json()
    new_name = f"patch_one_{uuid.uuid4().hex[:8]}"
    response = client.patch(f'/categories/{category_id}', json={'name': new_name})
    assert response.status_code == 200
    body = response.get_json()
    assert body['name'] == new_name
    assert body['id'] == before['id']

def test_patch_empty_body_400(client, category_id):
    response = client.patch(f'/categories/{category_id}', json={})
    assert response.status_code == 400
    assert 'Empty body' in response.get_json()['error']

def test_patch_null_on_nullable_and_non_nullable(client):
    companies = client.get('/companies').get_json()
    assert companies, 'seed data must include at least one company'
    company_id = companies[0]['id']
    title = f"tmp_app_{uuid.uuid4().hex[:12]}"
    created = client.post(
        '/apps',
        json={
            'title': title,
            'caption': 'keep me',
            'price': 1.0,
            'currency': 'USD',
            'company_id': company_id,
        },
    )
    assert created.status_code == 201, created.get_json()
    app_id = created.get_json()['id']
    try:
        ok = client.patch(f'/apps/{app_id}', json={'caption': None})
        assert ok.status_code == 200
        assert ok.get_json()['caption'] is None
        assert ok.get_json()['title'] == title

        bad = client.patch(f'/apps/{app_id}', json={'title': None})
        assert bad.status_code == 400
        assert 'cannot be null' in bad.get_json()['error']
    finally:
        client.delete(f'/apps/{app_id}')

def test_patch_nonexistent_404(client):
    response = client.patch('/categories/2147483646', json={'name': 'ghost'})
    assert response.status_code == 404
