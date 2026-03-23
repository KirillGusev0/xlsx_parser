# parser/management/commands/send_emails.py

from django.core.management.base import BaseCommand
from parser.services.sender import process_pending_emails


class Command(BaseCommand):
    help = "Send pending emails"

    def add_arguments(self, parser):
        parser.add_argument("--limit", type=int, default=10)

    def handle(self, *args, **options):
        limit = options["limit"]

        self.stdout.write(f"Processing {limit} emails...")
        process_pending_emails(limit=limit)
        self.stdout.write(self.style.SUCCESS("Done"))
