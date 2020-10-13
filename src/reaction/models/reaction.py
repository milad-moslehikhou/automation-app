from django.db import models


class Reaction(models.Model):
    subject = models.CharField(
        verbose_name='subject',
        max_length=255,
        unique=True
    )
    script = models.TextField(
        verbose_name='script',
    )
    description = models.CharField(
        verbose_name='description',
        max_length=255,
        null=True,
        blank=True
    )
