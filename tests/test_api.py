import pytest

from src.api import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Hello World"
    }


def test_calc_addition(client):
    response = client.post(
        "/calc",
        json={"expression": "2 + 3"}
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "result": "5"
    }


def test_calc_multiplication(client):
    response = client.post(
        "/calc",
        json={"expression": "4 * 5"}
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "result": "20"
    }


def test_calc_complex_expression(client):
    response = client.post(
        "/calc",
        json={"expression": "2 + 3 * 4"}
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "result": "14"
    }


def test_calc_missing_expression(client):
    response = client.post(
        "/calc",
        json={}
    )

    assert response.status_code == 400


def test_calc_without_json(client):
    response = client.post("/calc")

    assert response.status_code == 400


def test_calc_expression_not_string(client):
    response = client.post(
        "/calc",
        json={"expression": 123}
    )

    assert response.status_code == 400


def test_calc_rejects_malicious_expression(client):
    response = client.post(
        "/calc",
        json={
            "expression": '__import__("os").system("ls")'
        }
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "invalid expression"
    }


def test_calc_rejects_function_call(client):
    response = client.post(
        "/calc",
        json={"expression": "print('hello')"}
    )

    assert response.status_code == 400


def test_calc_rejects_variable(client):
    response = client.post(
        "/calc",
        json={"expression": "x + 1"}
    )

    assert response.status_code == 400