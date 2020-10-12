from django.db import models


class Task(models.Model):
    action = models.ForeignKey(
        "action.Action",
        verbose_name="action",
        on_delete=models.PROTECT
    )
    reaction = models.ForeignKey(
        "reaction.Reaction",
        verbose_name="reaction",
        on_delete=models.PROTECT
    )
    subject = models.CharField(
        verbose_name='subject',
        max_length=255,
        unique=True
    )
    enable = models.BooleanField(
        verbose_name='enable',
        default=True
    )

