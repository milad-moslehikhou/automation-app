from django.db import models


class Action(models.Model):
    subject = models.CharField(
        verbose_name='subject',
        max_length=255,
        unique=True
    )
    match_case = models.CharField(
        verbose_name='match case',
        max_length=255
    )
    description = models.CharField(
        verbose_name='description',
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return '{}_{}'.format(self.id, self.subject)
