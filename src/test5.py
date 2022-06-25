from pydoc import cli
from fastapi.testclient import TestClient
from fastapi import Path
import pytest

from main import app

client = TestClient(app)

# @pytest.mark.skip
def test_add_meta_data():
    response = client.post(
        "http://127.0.0.1:8000/add_meta_data/",
        data={
            "person_name": "Astrid Eyzaguirre",
            "face_id": "1000",
            "version_face": 1,
            "date": "2020-02-02"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "status": "OK",
        "body": "Meta Data added for 1000"
    }

# @pytest.mark.skip
def test_add_meta_data_no_face_with_id():
    response = client.post(
        "http://127.0.0.1:8000/add_meta_data/",
        data={
            "person_name": "Astrid Eyzaguirre",
            "face_id": "10000",
            "version_face": 1,
            "date": "2020-02-02"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "body": "No face with the given id"
    }