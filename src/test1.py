from pydoc import cli
from fastapi.testclient import TestClient
from fastapi import Path
import pytest

from main import app

client = TestClient(app)

# @pytest.mark.skip
def test_search_faces():
    with open("../images/Charlton_Heston_0003.jpg", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            data={
                "k": 5,
                "confidence": 0.4
            },
            files={"file": ("Charlton_Heston_0003.jpg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "OK",
        "body": {
            "faces0": [
            [
                1932,
                "Charlton_Heston/Charlton_Heston_0003.jpg",
                0
            ],
            [
                1933,
                "Charlton_Heston/Charlton_Heston_0004.jpg",
                0.29567989196822436
            ],
            [
                1930,
                "Charlton_Heston/Charlton_Heston_0001.jpg",
                0.3592006747058906
            ],
            [
                1935,
                "Charlton_Heston/Charlton_Heston_0006.jpg",
                0.45020899752744814
            ],
            [
                1934,
                "Charlton_Heston/Charlton_Heston_0005.jpg",
                0.5080982798751723
            ]
            ]
        }
    }

# @pytest.mark.skip
def test_search_faces2():
    with open("../images/bill_and_steve.jpg", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            data={
                "k": 2,
                "confidence": 0.4
            },
            files={"file": ("bill_and_steve.jpg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "OK",
        "body": {
            "faces0": [
                [
                    1247,
                    "Bill_Gates/Bill_Gates_0007.jpg",
                    0.4573050551446419
                ],
                [
                    1259,
                    "Bill_Gates/Bill_Gates_0009.jpg",
                    0.4617277375507851
                ]
            ],
            "faces1": [
                [
                    1364,
                    "Bob_Beauprez/Bob_Beauprez_0001.jpg",
                    0.4924815577320129
                ],
                [
                    1365,
                    "Bob_Beauprez/Bob_Beauprez_0002.jpg",
                    0.5610322253327884
                ]
            ]
        }
    }

# @pytest.mark.skip
def test_search_faces3():
    with open("../images/many_faces.jpg", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            data={
                "k": 3,
                "confidence": 0.4
            },
            files={"file": ("many_faces.jpg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
    "status": "OK",
    "body": {
            "faces0": [
            [
                368,
                "Alison_Lohman/Alison_Lohman_0001.jpg",
                0.16671321669500067
            ],
            [
                3501,
                "Estella_Warren/Estella_Warren_0001.jpg",
                0.5405532583443025
            ],
            [
                369,
                "Alison_Lohman/Alison_Lohman_0002.jpg",
                0.5455997929487307
            ]
            ],
            "faces1": [
            [
                656,
                "Angelina_Jolie/Angelina_Jolie_0003.jpg",
                0.10145352937197119
            ],
            [
                667,
                "Angelina_Jolie/Angelina_Jolie_0014.jpg",
                0.39523352553474894
            ],
            [
                668,
                "Angelina_Jolie/Angelina_Jolie_0015.jpg",
                0.40409535763027254
            ]
            ],
            "faces2": [
            [
                657,
                "Angelina_Jolie/Angelina_Jolie_0004.jpg",
                0.14451047972478592
            ],
            [
                666,
                "Angelina_Jolie/Angelina_Jolie_0013.jpg",
                0.4078771974006808
            ],
            [
                673,
                "Angelina_Jolie/Angelina_Jolie_0020.jpg",
                0.4453792421841781
            ]
            ],
            "faces3": [
            [
                668,
                "Angelina_Jolie/Angelina_Jolie_0015.jpg",
                0.11548446496046647
            ],
            [
                667,
                "Angelina_Jolie/Angelina_Jolie_0014.jpg",
                0.22810651788943248
            ],
            [
                659,
                "Angelina_Jolie/Angelina_Jolie_0006.jpg",
                0.3427292939492505
            ]
            ],
            "faces4": [
            [
                669,
                "Angelina_Jolie/Angelina_Jolie_0016.jpg",
                0.1241087718695698
            ],
            [
                673,
                "Angelina_Jolie/Angelina_Jolie_0020.jpg",
                0.4112938169921129
            ],
            [
                666,
                "Angelina_Jolie/Angelina_Jolie_0013.jpg",
                0.4127764140635788
            ]
            ],
            "faces5": [
            [
                641,
                "Angela_Bassett/Angela_Bassett_0002.jpg",
                0.12473316506393817
            ],
            [
                643,
                "Angela_Bassett/Angela_Bassett_0004.jpg",
                0.3991619802588723
            ],
            [
                644,
                "Angela_Bassett/Angela_Bassett_0005.jpg",
                0.40763618570856436
            ]
            ],
            "faces6": [
            [
                775,
                "Antonio_Palocci/Antonio_Palocci_0005.jpg",
                0.5726511655050908
            ],
            [
                2055,
                "Christopher_Conyers/Christopher_Conyers_0001.jpg",
                0.5737184657123697
            ],
            [
                2981,
                "Donald_Hays/Donald_Hays_0001.jpg",
                0.5752561955687154
            ]
            ],
            "faces7": [
            [
                4601,
                "Ghassan_Elashi/Ghassan_Elashi_0001.jpg",
                0.5465459310266092
            ],
            [
                4813,
                "Gregor_Gysi/Gregor_Gysi_0001.jpg",
                0.5515723872950867
            ],
            [
                775,
                "Antonio_Palocci/Antonio_Palocci_0005.jpg",
                0.5655784539297006
            ]
            ],
            "faces8": [
            [
                645,
                "Angela_Bassett/Angela_Bassett_0006.jpg",
                0.11327291215371489
            ],
            [
                644,
                "Angela_Bassett/Angela_Bassett_0005.jpg",
                0.449015223986958
            ],
            [
                641,
                "Angela_Bassett/Angela_Bassett_0002.jpg",
                0.46485916232001223
            ]
            ],
            "faces9": [
            [
                371,
                "Allan_Houston/Allan_Houston_0001.jpg",
                0.14269017431692158
            ],
            [
                1719,
                "Carlos_Paternina/Carlos_Paternina_0001.jpg",
                0.5214104879423139
            ],
            [
                4864,
                "Guillermo_Coria/Guillermo_Coria_0020.jpg",
                0.5263515752005458
            ]
            ],
            "faces10": [
            [
                2110,
                "Claire_Hentzen/Claire_Hentzen_0002.jpg",
                0.5360201542325502
            ],
            [
                2109,
                "Claire_Hentzen/Claire_Hentzen_0001.jpg",
                0.5373083312126241
            ],
            [
                2055,
                "Christopher_Conyers/Christopher_Conyers_0001.jpg",
                0.563371685179078
            ]
            ],
            "faces11": [
            [
                2893,
                "Diane_Ladd/Diane_Ladd_0001.jpg",
                0.5140340632777378
            ],
            [
                1061,
                "Barbara_Walters/Barbara_Walters_0001.jpg",
                0.5198929440215878
            ],
            [
                2892,
                "Diane_Green/Diane_Green_0001.jpg",
                0.53446895047766
            ]
            ],
            "faces12": [
            [
                4649,
                "Glenn_Plummer/Glenn_Plummer_0001.jpg",
                0.49635813886249297
            ],
            [
                686,
                "Anil_Ramsook/Anil_Ramsook_0001.jpg",
                0.5054921024418272
            ],
            [
                371,
                "Allan_Houston/Allan_Houston_0001.jpg",
                0.5355733886277602
            ]
            ]
        }
    }

# @pytest.mark.skip
def test_search_faces_no_face():
    with open("../images/no_faces.jpeg", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            data={
                "k": 2,
                "confidence": 0.4
            },
            files={"file": ("no_faces.jpeg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "body": "No face in the given image"
    }

# @pytest.mark.skip
def test_search_faces_not_an_image_file():
    with open("../images/testfile.txt", "rb") as f:
        response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            data={
                "k": 2,
                "confidence": 0.4
            },
            files={"file": ("testfile.txt", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "body": "Not an image file"
    }