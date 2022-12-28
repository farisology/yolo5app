from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)
"""the unit test require pytest & httpx to be installed so install them before running the test
"""

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "you are here for a reason, follow your heart."}

def test_detect():
    response = client.get("/detect_objects?image_url=https://www.hdnicewallpapers.com/Walls/Big/Cat/Cat_Image_Free_Download.jpg")
    assert response.status_code == 200
    assert response.json() == {
                                "detected_objects": [
                                    {
                                    "xmin": 6.24591064453125,
                                    "ymin": 29.948410034179688,
                                    "xmax": 1380.0406494140625,
                                    "ymax": 997.60693359375,
                                    "confidence": 0.5177698731422424,
                                    "class": 15,
                                    "name": "cat"
                                    }
                                ]
                                }
