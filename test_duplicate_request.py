from src.services.request_service import RequestService


class DuplicateRepository:
    def exists(self, student_id, topic):
        return True


class FakeNotifier:
    def send(self, student_id, message):
        pass


class FakeLogger:
    def write(self, message):
        pass


class FakeResponseGenerator:
    def generate(self, topic):
        return "Duplicate"


def test_duplicate_request():
    service = RequestService(
        repository=DuplicateRepository(),
        notifier=FakeNotifier(),
        logger=FakeLogger(),
        response_generator=FakeResponseGenerator()
    )

    result = service.process(
        student_id=1,
        topic="password",
        text="reset",
        urgent=False
    )

    assert result == "Already exists"
