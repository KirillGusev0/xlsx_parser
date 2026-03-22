from django.test import TestCase
from parser.models import EmailTask
from parser.services.sender import process_pending_emails


class TestSender(TestCase):

    def test_send_email_flow(self):
        task = EmailTask.objects.create(
            external_id="1",
            user_id=1,
            email="test@test.com",
            subject="Test",
            message="Hello",
        )

        process_pending_emails(limit=1)

        task.refresh_from_db()
        self.assertEqual(task.status, "sent")