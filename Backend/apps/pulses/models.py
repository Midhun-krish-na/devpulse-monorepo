from django.db import models
from django.conf import settings


class DailyPulses(models.Model):
    # Link each submission to a specific user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,  # Prevent accidental deletion of operational logs
        related_name='pulses'
    )

    # Daily pulse details
    energy_score = models.PositiveSmallIntegerField()  # Rating: 1–5
    has_blocker = models.BooleanField(default=False)   # Blocker checkbox
    comment = models.TextField(blank=True, null=True)  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    class Meta:
        # Show latest entries first
        ordering = ['-created_at']

    def __str__(self):
        return f"Pulse by {self.user.email} on {self.created_at.date()}"