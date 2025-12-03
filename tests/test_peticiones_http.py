from datetime import datetime
import requests
import pytest
from faker import Faker
import pytest_check as check
from conftest import logger
fake = Faker()


class Test_GetUser:
    @pytest.mark.get
    def test_get_response_code(self, api_url):
        response = requests.get(api_url + "users")
        assert response.status_code == 200

    @pytest.mark.get
    def test_response_data(self, api_url):
        response = requests.get(api_url + "users")
        data = response.json()
        assert isinstance(data, list)


class TestPostUser:
    @pytest.mark.post
    def test_post_response_code(self, api_url):
        new_user = {
            "user_name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "createdAt": datetime.now()
        }
        response = requests.post(api_url + "users", new_user)
        data = response.json()
        assert "id" in data
        assert response.status_code == 201
        if "createdAt" in data:
            created_at = data["createdAt"]
            current_year = datetime.now().year
            assert str(current_year) in created_at


class TestPatchUser:
    @pytest.mark.patch
    def test_patch_response_code(self, api_url):
        user_update = {
            "id": 2,
            "email": fake.email()
        }
        response = requests.patch(api_url + "users/2", user_update)
        assert response.status_code == 200


class TestPutUser:
    @pytest.mark.put
    def test_put_response_code(self, api_url):
        user_update = {
            "id": 1,
            "user_name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number()
        }
        response = requests.put(api_url + "users/1", user_update)
        assert response.status_code == 200


class TestDeleteUser:
    @pytest.mark.delete
    def test_delete_response_code(self, api_url):
        response = requests.delete(api_url + "users/3")
        assert response.status_code == 200


class TestUserWorkflow:
    @pytest.mark.api
    def test_users_completo(self, api_url):
        logger.info("TEST ENCADENADOS : GET, POST, PUT, PATCH, DELETE")
        logger.info("GET: Obetener usuarios")
        response = requests.get(api_url + "users")
        data = response.json()
        check.equal(response.status_code, 200)
        check.is_true(len(data) > 0)
        check.is_true(isinstance(data, list))

        logger.info("POST: Crear usuario")
        new_user = {
            "user_name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "createdAt": datetime.now()
        }
        response = requests.post(api_url + "users", new_user)
        data = response.json()
        check.is_in("id", data)
        check.equal(response.status_code, 201)
        if "createdAt" in data:
            created_at = data["createdAt"]
            current_year = datetime.now().year
            check.is_in(str(current_year), created_at)
        logger.info("Patch: Modificar un dato de un usuario en particular")
        user_update = {
            "id": 2,
            "email": fake.email()
        }
        response = requests.patch(api_url + "users/2", user_update)
        check.equal(response.status_code, 200)
        logger.info("Put: Modificar todos los datos de un usuario en particular")
        user_update = {
            "id": 1,
            "user_name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number()
        }
        response = requests.put(api_url + "users/1", user_update)
        check.equal(response.status_code, 200)
        logger.info("delete: borrar un usuario en particular")
        response = requests.delete(api_url + "users/3")
        check.equal(response.status_code, 200)
