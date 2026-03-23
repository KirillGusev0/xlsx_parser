from django.test import TestCase
from parser.services.importer import validate_row
from parser.models import EmailTask


class TestImporter(TestCase):

    def test_validate_row_success(self):
        data = {
            "external_id": "1",
            "user_id": 123,
            "email": "test@test.com",
            "subject": "Hello",
            "message": "World",
        }

        validate_row(data)

    def test_validate_row_invalid_email(self):
        data = {
            "external_id": "1",
            "user_id": 123,
            "email": "bad_email",
            "subject": "Hello",
            "message": "World",
        }

        with self.assertRaises(ValueError):
            validate_row(data)

    def test_deduplication(self):
        EmailTask.objects.create(
            external_id="1",
            user_id=1,
            email="a@test.com",
            subject="s",
            message="m",
        )

        exists = EmailTask.objects.filter(external_id="1").exists()
        self.assertTrue(exists)
