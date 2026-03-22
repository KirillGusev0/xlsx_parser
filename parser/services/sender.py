# mailer/services/sender.py

import logging
import time
import random

from parser.models import EmailTask

logger = logging.getLogger(__name__)


def send_email(task: EmailTask):
    delay = random.randint(5, 20)
    time.sleep(delay)

    logger.info(
        f"Send EMAIL to={task.email} subject={task.subject} delay={delay}s"
    )


def process_pending_emails(limit: int = 10):
    tasks = list(
        EmailTask.objects.filter(status="pending")[:limit]
    )

    if not tasks:
        return 0

    for task in tasks:
        try:
            send_email(task)

            task.status = "sent"
            task.save(update_fields=["status"])

        except Exception as e:
            task.status = "error"
            task.error_message = str(e)
            task.save(update_fields=["status", "error_message"])

    return len(tasks)