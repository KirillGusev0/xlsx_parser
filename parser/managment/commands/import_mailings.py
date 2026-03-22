# parser/management/commands/import_mailings.py

from django.core.management.base import BaseCommand, CommandError

from parser.services.importer import import_from_xlsx
from parser.services.sender import process_pending_emails


class Command(BaseCommand):
    help = "Import mailings from XLSX file and send emails"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)
        parser.add_argument(
            "--send",
            action="store_true",
            help="Send emails after import",
        )
        parser.add_argument(
            "--batch-size",
            type=int,
            default=50,
            help="Batch size for sending emails",
        )

    def handle(self, *args, **options):
        file_path = options["file_path"]
        send = options["send"]
        batch_size = options["batch_size"]

        self.stdout.write(f"Starting import from: {file_path}")

        try:
            result = import_from_xlsx(file_path)

            self.stdout.write(self.style.SUCCESS("Import completed"))
            self.stdout.write(f"Total rows: {result.total}")
            self.stdout.write(f"Created: {result.created}")
            self.stdout.write(f"Skipped: {result.skipped}")
            self.stdout.write(f"Errors: {result.errors}")
            self.stdout.write(f"Duration: {result.duration:.2f} sec")

            if send:
                self.stdout.write("Starting email sending...")

                while True:
                    processed = process_pending_emails(limit=batch_size)

                    if processed == 0:
                        break

                self.stdout.write(self.style.SUCCESS("All emails processed"))

        except FileNotFoundError:
            raise CommandError(f"File not found: {file_path}")

        except Exception as e:
            raise CommandError(f"Import failed: {e}")