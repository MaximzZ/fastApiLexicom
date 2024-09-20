import pytest
from fastapi.testclient import TestClient
from app.main import app
import fakeredis
import app.main as main

client = TestClient(app)

class TestRedisAPI:
    @pytest.fixture(autouse=True)
    def redis_client_mock(self):
        main.redis_client = fakeredis.FakeRedis()
        yield
        main.redis_client.flushall()

    def test_write_data(self):
        response = client.post("/write_data", json={"phone": "89090000000", "address": "Москва"})
        assert response.status_code == 200
        assert response.json() == {"message": "Data saved successfully"}

        stored_address = main.redis_client.hget("89090000000", "address")
        assert stored_address.decode() == "Москва"

    def test_check_data(self):
        main.redis_client.hset("89090000000", "address", "Москва".encode("utf-8"))

        response = client.get("/check_data?phone=89090000000")
        assert response.status_code == 200
        assert response.json() == {"phone": "89090000000", "address": "Москва"}

    def test_check_data_not_found(self):
        response = client.get("/check_data?phone=1234567890")
        assert response.status_code == 404
        assert response.json() == {"detail": "Phone number not found"}
