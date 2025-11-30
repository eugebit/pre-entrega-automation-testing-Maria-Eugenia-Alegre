from datetime import datetime
from http.client import responses
import requests
import pytest
from faker.contrib.pytest.plugin import faker
from faker import Faker

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
