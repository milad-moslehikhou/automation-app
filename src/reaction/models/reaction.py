from django.db import models


class Reaction(models.Model):
    subject = models.CharField(
        verbose_name='subject',
        max_length=255,
    )
    script = models.FileField(
        upload_to='scripts'
    )
    description = models.CharField(
        verbose_name='description',
        max_length=255,
        null=True,
        blank=True
    )
