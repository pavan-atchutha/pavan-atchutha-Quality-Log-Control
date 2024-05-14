from django.db import models

# Create your models here.

class LogEntry(models.Model):
    LEVEL_CHOICES = [
        ('DEBUG', 'Debug'),
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error'),
        ('CRITICAL', 'Critical'),
        ('SUCCESS', 'Success')
    ]
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    log_string = models.TextField()
    timestamp = models.DateTimeField()
    metadata_source = models.JSONField()

    def __str__(self):
        return f"{self.timestamp} - {self.metadata_source}: {self.log_string}"

    class Meta:
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['level']),
            models.Index(fields=['metadata_source']),
        ]

