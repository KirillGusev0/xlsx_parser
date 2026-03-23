from django.db import models

# Create your models here.
# parser/models.py


class EmailTask(models.Model):

    STATUS_CHOICES = (
        ("pending", "pending"),
        ("processing", "processing"),
        ("sent", "sent"),
        ("error", "error"),
    )

    external_id = models.CharField(
        max_length=255,
        unique=True,
    )

    user_id = models.IntegerField()

    email = models.EmailField()

    subject = models.CharField(
        max_length=255,
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    error_message = models.TextField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        verbose_name = "Email task"
        verbose_name_plural = "Email tasks"

        indexes = [
            models.Index(fields=["external_id"]),
            models.Index(fields=["status"]),
        ]

        ordering = ("-created_at",)

    def __str__(self):

        return f"{self.external_id} {self.email}"
