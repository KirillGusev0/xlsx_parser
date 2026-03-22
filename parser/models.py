from django.db import models

# Create your models here.
# parser/models.py

class EmailTask(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("sent", "Sent"),
        ("error", "Error"),
    ]

    external_id = models.CharField(max_length=255, unique=True)
    user_id = models.IntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    error_message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["external_id"]),
        ]

    def __str__(self):
        return f"{self.external_id} - {self.email}"