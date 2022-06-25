from pydoc import cli
from fastapi.testclient import TestClient
from fastapi import Path
import pytest

from main import app

client = TestClient(app)

# @pytest.mark.skip
def test_add_faces_in_bulk():
    with open("../images/images_compress_test_2.zip", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/add_faces_in_bulk/",
            files={"file": ("images_compress_test_2.zip", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "OK",
        "body": " Successfully added 3 images"
    }

# @pytest.mark.skip
def test_add_faces_in_bulk_not_zip_file():
    with open("../images/biden.jpeg", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/add_faces_in_bulk/",
            files={"file": ("biden.jpeg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "body": "Not a zip file"
    }

# @pytest.mark.skip
def test_add_faces_in_bulk_no_image():
    with open("../images/no_faces.zip", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/add_faces_in_bulk/",
            files={"file": ("no_faces.zip", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "body": "No image file in given zip file"
    }