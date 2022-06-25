from pydoc import cli
from fastapi.testclient import TestClient
from fastapi import Path
import pytest

from main import app

client = TestClient(app)

# @pytest.mark.skip
def test_get_face_info():
    response = client.post(
        "http://127.0.0.1:8000/get_face_info/",
        data={
            "api_key": "asdCfrgjkK",
            "face_id": "1000"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "status": "OK",
        "body": {
            "face ID": 1000,
            "photo_name": "Astrid_Eyzaguirre/Astrid_Eyzaguirre_0001.jpg",
            "person_name": "Astrid Eyzaguirre",
            "version": 1,
            "date_of_photo": "2020-02-02"
        }
    }

# @pytest.mark.skip
def test_get_face_info_no_face_id():
    response = client.post(
        "http://127.0.0.1:8000/get_face_info/",
        data={
            "api_key": "asdCfrgjkK",
            "face_id": "10000"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "body": "No face with the given id"
    }