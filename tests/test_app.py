from src.app import health
from src.utils import add, service_name


def test_health():
    result = health()
    assert result["status"] == "ok"
    assert result["service"] == "port-ocean-github-demo"


def test_add():
    assert add(2, 3) == 5


def test_service_name():
    assert service_name() == "port-ocean-github-demo"
