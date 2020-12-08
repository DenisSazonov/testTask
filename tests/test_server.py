import pytest


@pytest.mark.parametrize('value', [0, 5, 10])
# test for checking equivalence class and boundary values
def test_with_valid_values(client, value):
    res = client.post(data={"test":value})
    assert 200 == res.status_code
    print(res)
    assert 'OK' in res.get_data(as_text=True)


@pytest.mark.parametrize('value', [-1, -9999999999])
# test for checking negative digit
def test_with_small_value(client, value):
    res = client.post(data={"test": value})
    assert 500 == res.status_code
    assert 'Value is too small' in res.get_data(as_text=True)


@pytest.mark.parametrize('value', [11, 9999999999])
# test for checking value biggest than 10
def test_with_large_value(client, value):
    res = client.post(data={"test": value})
    assert 502 == res.status_code
    assert 'Value is too large' in res.get_data(as_text=True)


# checking response for get request
def test_get(client):
    res = client.get()
    assert res.status_code == 222
    assert "I'm only postable" in res.get_data(as_text=True)


# ----------------------------- negative cases ----------------------------------------
@pytest.mark.parametrize('value', [-5.5, '-0x19323L', 45.j, 'six'.encode('utf-32-le')])
# test with float, long, complex digits and string
def test_post_with_unsupported_values(client, value):
    res = client.post(data={"test": value})
    assert res.status_code == 501
    assert "Non integer data passed in request form" in res.get_data(as_text=True)


def test_post_without_parameters(client):
    res = client.post(data={"test": ''})
    assert res.status_code == 501
    assert "Non integer data passed in request form" in res.get_data(as_text=True)


def test_post_with_empty_json(client):
    res = client.post(data={})
    assert res.status_code == 501
    assert "Non integer data passed in request form" in res.get_data(as_text=True)

