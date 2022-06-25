from pydoc import cli
from fastapi.testclient import TestClient
from fastapi import Path
import pytest

from main import app

client = TestClient(app)

# @pytest.mark.skip
def test_add_face():
    with open("../images/lincoln.jpeg", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/add_face/",
            files={"file": ("lincoln.jpeg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "OK",
        "body": "successfully added lincoln.jpeg"
    }

# @pytest.mark.skip
def test_add_face_not_image_file():
    with open("../images/testfile.txt", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/add_face/",
            files={"file": ("testfile.txt", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "body": "Not an image file"
    }

# @pytest.mark.skip
def test_add_face_no_faces():
    with open("../images/no_faces.jpeg", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/add_face/",
            files={"file": ("no_faces.jpeg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "body": "No face in the given image"
    }

# @pytest.mark.skip
def test_add_face_multiple_faces():
    with open("../images/bill_people.jpg", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/add_face/",
            files={"file": ("bill_people.jpg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "body": "Multiple faces found"
    }