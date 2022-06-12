from project.weather_flask import app as flask_app


def test_default_page_get_status_code_is_ok():
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Krakow' in response.data


def test_wrong_page_get_status_code_is_bad_request():
    with flask_app.test_client() as test_client:
        response = test_client.get('/dummy')
        assert response.status_code == 404


def test_diff_city_page_get_status_code_is_ok():
    with flask_app.test_client() as test_client:
        response = test_client.get('/different-city')
        assert response.status_code == 200
        assert b'Tarn\\u00f3w' in response.data


def test_default_page_delete_is_not_allowed():
    with flask_app.test_client() as test_client:
        response = test_client.delete('/')
        assert response.status_code == 405


def test_diff_city_post():
    with flask_app.test_client() as test_client:
        response = test_client.post('/different-city?city=London')
        assert response.status_code == 204

        response = test_client.get('/different-city')
        assert response.status_code == 200
        assert b'London' in response.data
        assert b'Krakow' not in response.data


def test_essential_data_view():
    with flask_app.test_client() as test_client:
        response = test_client.post('/?custom=essential')
        assert response.status_code == 204

        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Krakow' in response.data
        assert b'pressure' not in response.data


def test_unknown_data_view():
    with flask_app.test_client() as test_client:
        response = test_client.post('/?custom=unknown')
        assert response.status_code == 204

        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Krakow' in response.data
        assert b'pressure' in response.data
