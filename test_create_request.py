import pytest
from src.services.request_service import RequestService


class FakeRepository:
    def exists(self, student_id, topic):
        return False

    def save(self, request):
        return 1


class FakeNotifier:
    def send(self, student_id, message):
        pass


class FakeLogger:
    def write(self, message):
        pass


class FakeResponseGenerator:
    def generate(self, topic):
        return "Request accepted"


def test_create_new_request():
    service = RequestService(
        repository=FakeRepository(),
        notifier=FakeNotifier(),
        logger=FakeLogger(),
        response_generator=FakeResponseGenerator()
    )

    result = service.process(
        student_id=1,
        topic="schedule",
        text="Need help",
        urgent=False
    )

    assert result == "Request accepted"
